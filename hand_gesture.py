import cv2
import numpy as np
import os
import urllib.request
import screen_brightness_control as sbc
import mediapipe as mp

# Pycaw（音量制御）の安全な初期化
volctl = None
minv, maxv = 0.0, 100.0
try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    devices = AudioUtilities.GetSpeakers()
    # デバイスオブジェクトから直接エンドポイントボリュームを取得
    if hasattr(devices, "EndpointVolume"):
        volctl = devices.EndpointVolume
    else:
        volctl = devices.Activate(IAudioEndpointVolume._iid_, 23, None) # CLSCTX_ALL = 23
    minv, maxv = volctl.GetVolumeRange()[:2]
    print("Volume control initialized successfully.")
except Exception as e:
    print(f"Pycaw notice: Volume control is disabled ({e}). Brightness control will still work.")

# 1. モデルファイル（hand_landmarker.task）の自動ダウンロード
model_path = 'hand_landmarker.task'
if not os.path.exists(model_path):
    print("Downloading MediaPipe hand landmarker model...")
    urllib.request.urlretrieve(
        'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task',
        model_path
    )
    print("Download completed.")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible.")
    exit()

WIN = "Hand Gesture Control"
cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)

# MediaPipe Tasks API のセットアップ
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

options = vision.HandLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=model_path),
    num_hands=2,
    min_hand_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
detector = vision.HandLandmarker.create_from_options(options)

TH, IX = 4, 8  # 親指の先端と人差し指の先端のインデックス

while True:
    ok, img = cap.read()
    if not ok:
        break
    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_img)

    detection_result = detector.detect(mp_image)

    if detection_result.hand_landmarks and detection_result.handedness:
        for i, hand_landmarks in enumerate(detection_result.hand_landmarks):
            label = detection_result.handedness[i][0].category_name

            lm_th = hand_landmarks[TH]
            lm_ix = hand_landmarks[IX]

            tp = (int(lm_th.x * w), int(lm_th.y * h))
            ip = (int(lm_ix.x * w), int(lm_ix.y * h))

            cv2.circle(img, tp, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, ip, 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, ip, tp, (0, 255, 0), 3)

            dist = float(np.hypot(ip[0] - tp[0], ip[1] - tp[1]))

            # 左手：音量制御（利用可能な場合のみ）
            if label == "Left":
                if volctl is not None:
                    try:
                        v = float(np.interp(dist, [30, 300], [minv, maxv]))
                        volctl.SetMasterVolumeLevel(v, None)
                    except Exception:
                        pass
                bar = int(np.interp(dist, [30, 300], [400, 150]))
                pct = int(np.interp(dist, [30, 300], [0, 100]))
                cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)
                cv2.rectangle(img, (50, bar), (85, 400), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, f"{pct}%", (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

            # 右手：明るさ制御
            if label == "Right":
                b = int(np.interp(dist, [30, 300], [0, 100]))
                try:
                    sbc.set_brightness(b)
                except Exception as e:
                    print(f"Brightness error: {e}")
                bar = int(np.interp(dist, [30, 300], [400, 150]))
                x1 = w - 85
                cv2.rectangle(img, (x1, 150), (w - 50, 400), (0, 250, 0), 2)
                cv2.rectangle(img, (x1, bar), (w - 50, 400), (0, 250, 0), cv2.FILLED)
                cv2.putText(img, f"{b}%", (w - 110, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 250, 0), 3)

    cv2.imshow(WIN, img)
    k = cv2.waitKey(1) & 0xff
    if k == ord("q"):
        break
    try:
        if cv2.getWindowProperty(WIN, cv2.WND_PROP_VISIBLE) < 1:
            break
    except cv2.error:
        break

cap.release()
cv2.destroyAllWindows()