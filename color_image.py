import cv2
import numpy as np
def apply_color_filter(image, filter_type):
    """Apply a color filter to the image"""
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Remove green channel
        filtered_image[:, :, 0] = 0  # Remove blue channel
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Remove green channel
        filtered_image[:, :, 2] = 0  # Remove red channel
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Remove blue channel
        filtered_image[:, :, 2] = 0  # Remove red channel

    elif filter_type == "increased_red":
        filtered_image[:, :, 2] =cv2.add(filtered_image[:, :, 2], 50)  # Increase red channel
    elif filter_type == "decreased_blue":
            filtered_image[:, :, 0] =cv2.subtract(filtered_image[:, :, 0], 50)  # Decrease blue channel
    elif filter_type == "sapphire":
       filtered_image[:,:,2]=cv2.subtract(filtered_image[:,:,2],50)
       filtered_image[:,:,0]=cv2.add(filtered_image[:,:,0],50)
       filtered_image[:,:,1]=cv2.subtract(filtered_image[:,:,1],30)
    return filtered_image

image_path='cat.jpg'  # Replace with your image path
image=cv2.imread(image_path)
if image is None:
     print("Error: Image not found!")

else:filter_type ='original'  # Default filter type
print("Select a color filter:")
print("r. Red Tint")
print("b. Blue Tint")
print("g. Green Tint")
print("i. Increased Red")
print("d. Decreased Blue")
print("s. Sapphire")

print("q. Quit")


while True:
     filtered_image = apply_color_filter(image, filter_type)
     cv2.imshow("Filtered Image", filtered_image)
     key=cv2.waitKey(0) & 0xFF
     if key == ord('r'):
            filter_type = "red_tint"
     elif key == ord('b'):
            filter_type = "blue_tint"
     elif key == ord('g'):
            filter_type = "green_tint"
     elif key == ord('i'):
            filter_type = "increased_red"
     elif key == ord('d'):
            filter_type = "decreased_blue"
     elif key == ord('s'):
            filter_type = "sapphire"
     elif key == ord('q'):
        print("Exiting...")
        break
     else:
           print("Invalid choice. Please select r, b, g, i, d, s, or q.")
cv2.destroyAllWindows()
