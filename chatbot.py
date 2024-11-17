import random

def get_greeting():
    
    greetings = ["Hi there!", "Hello!", "Greetings!", "Welcome!", "What can I do for you today?"]
    return random.choice(greetings)

def get_goodbye():
    """Returns a random goodbye message."""
    goodbyes = ["Goodbye!", "Have a great day!", "Talk to you soon!", "See you later!", "Best wishes!"]
    return random.choice(goodbyes)

def get_response(user_input):
   
    user_input = user_input.lower()

    if user_input in ("hello", "hi", "hey"):
        return get_greeting()
    elif user_input in ("how are you", "how's it going"):
        return "I'm doing well, thanks for asking! How are you?"
    elif "weather" in user_input:
        return "I apologize, but I don't have information about the weather. Would you like to ask me something else?"
    elif "top games of 2023" in user_input:
        return "Here are the top 5 games of 2023 (according to various sources):\n1. Grand Theft Auto V\n2. Elden Ring\n3. God of War Ragnarok\n4. Horizon Forbidden West\n5. The Legend of Zelda: Breath of the Wild 2"
    elif user_input.startswith("what is my name"):
       
        if "your name" in user_input or "you call me" in user_input:
            return "I apologize, I don't have your name stored yet. You can tell me your name if you'd like!"
        if  "My name is" in user_input:
            return "Your Name is Jidnesh ! "
        else:
            return "I'm sorry, I don't know your name."
    elif "exit" in user_input:
        return get_goodbye()
    else:
      
        suggestions = [
            "I'm still learning, but I can answer questions about various topics. What would you like to ask?",
            "I can't quite understand that yet. Can you rephrase or ask something else?",
            "Feel free to ask me anything you're curious about!"
        ]
        return random.choice(suggestions)

def main():

    print(get_greeting())

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        if user_input == "exit":
            break

if __name__ == "__main__":
    main()