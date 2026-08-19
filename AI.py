print("Hello, I'm AI BOT. What is your name:")
name=input()
print(f"Hello {name}, Nice to meet you.")
print("How are you feeling today?(good/bad)") 
mood=input().lower()

if mood=="good":
    print("I'm glad to hear that!")
elif mood=="bad":
    print("I'm sorry to hear that. I hope your day gets better!")
else:
    print("I see. sometimes it's hard to put our feelings into words.")

print(f"It was nice chatting you,{name}.Have a great day!")