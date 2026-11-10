# BAKERY HELP DESK SORTER
# ---------- SETUP (given to you) ----------
URGENT_WORDS = {
    "refund": 3, "broken": 3, "late": 2, "missing": 2, "wrong": 2,
    "cancel": 2, "never": 2, "again": 1, "now": 1,
}
THRESHOLD = 4
PUNCTUATION = ".,!?:;\"'()"

TEST_MESSAGES = [
    ("My cake arrived broken and I want a refund now!", "URGENT"),
    ("The delivery is late again, and my order is missing", "URGENT"),
    ("Thank you, the cupcakes were delicious", "NORMAL"),
    ("Do you sell gluten free bread?", "NORMAL"),
    ("Can I cancel my order? I ordered the wrong size", "URGENT"),
    ("I never had a late delivery before, great service!", "NORMAL"),
]

# ---------- PART 1: clean the words ----------
def tokenize(message):
    # YOUR CODE HERE
    # Split the message, make each word lowercase, strip PUNCTUATION from both ends,
    # keep only words that are not empty, and return the list.
    return []


print("PART 1: Clean words")
print(tokenize("Where is my REFUND?!"))

# ---------- PART 2: score the message ----------
def urgency_score(message):
    # YOUR CODE HERE
    # Add up URGENT_WORDS.get(word, 0) for every word from tokenize(message).
    return 0


print("\nPART 2: Score")
print(urgency_score("My cake arrived broken and I want a refund now!"))

# ---------- PART 3: label the message ----------
def label(message):
    # YOUR CODE HERE
    # Return "URGENT" if the score is at least THRESHOLD, otherwise "NORMAL".
    return "NORMAL"


print("\nPART 3: Label")
print(label("Thank you, the cupcakes were delicious"))

# ---------- PART 4: check every test message ----------
print("\nPART 4: Test all messages")
mistakes = 0
# YOUR CODE HERE
# For each (message, expected) pair: get the label, add 1 to mistakes if it is not the expected one,
# and print the label, the score and the message on one line.
# After the loop, print: Mistakes: <number> out of <total>
