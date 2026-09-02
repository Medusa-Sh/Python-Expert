import re, random
from colourmara import Fore,init

init(autoreset=True)
destination={"Beaches:"["Bali","Madivals","Phuket"],
             "moutains:"["Swiss Alps","Rocky mountains","Himarayas"],
             "Cities:"["Tokyo","Paris","New York"]}

Jokes=["Why don't programmers like nature? Too many bags",
       "Why do computers go to doctor? Because they have VIRUS",
       "Why do travellers always feel warm? because of hot spots"]

def normalize_input(text):
    return re.sub(r"\s+","",text.strip().lower())
def recommand():
    print(Fore.CYAN+"TravelBot:beaches,mountains or cities")
    preference=input(Fore.YELLOW+"YOU:")
    preference=(normalize_input(preference))
    answer=input(Fore.YELLOW+"You:")
    
    if preference in destination:
        suggestion=random.choice(destination[preference])
        print(Fore.GREEN+f"Travelbot: How about {suggestion}")
        if answer=="yes":
            print(Fore.GREEN+f"Travelbot:Awsome! Enjoy your vacation to {suggestion}!")
        elif answer=="no":
            print(Fore.RED+"Travelbot:No worries! I can suggest another destination.")
            recommand()
        else:
            print(Fore.RED+"Travelbot:Sorry, I don't have that type of destination.")
            recommand()

def paking_tips():
    print(Fore.CYAN+"TravelBot:Where to?")
    location=normalize_input(input(Fore.YELLOW+"YOU:"))
    print(Fore.CYAN+"TravelBot: For how many days?")
    days=int(input(Fore.YELLOW+"YOU:")) 

    print(Fore.GREEN+f"Packing tips for {location} for {days}days:")
    print(Fore.GREEN+"1. Pack versatile cloth.")
    print(Fore.GREEN+"2. Bring chargers/adapters.")
    print(Fore.GREEN+"3.Check weather forecast.")

def tell_joke():
    joke=random.choice(Jokes)
    print(Fore.GREEN+f"Travelbot: {joke}")

def show_help():
    print(Fore.MAGENTA+"Travelbot: \nI can:")
    print(Fore.GREEN+"Sugget travel destinations say 'recommand'")
    print(Fore.GREEN+"Give packing tips say 'packing tips'")
    print(Fore.GREEN+"Tell a joke say 'joke'")
    print(Fore.CYAN+"YOu can finish the conversation by saying 'exit' or 'quit'")

def chat():
        print(Fore.CYAN+"Hi, I'm travell bot")
        name=input(Fore.YELLOW+"What's your name?")
        print(Fore.GREEN+"Nice to meet you, {name}!")
        while True:
            user_input=input(Fore.YELLOW+f"{name}:")
            user_input=normalize_input(user_input)
            if "recommand" in user_input:
                recommand()
            elif "packing tips" in user_input:
                paking_tips()
            elif "joke" in user_input:
                tell_joke()
            elif "help" in user_input:
                show_help()
            elif user_input in ["exit","quit"]:
                print(Fore.CYAN+"Travelbot: Goodbye!")
                break
            else:
                print(Fore.RED+"Travelbot:Could you rephrasethat?")

if __name__=="__main__":
    chat()