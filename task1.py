def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure, I can help! What do you need assistance with?"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Happy to help."
    elif "weather" in user_input:
        return "Currently, I can't provide real-time weather updates, but you can check your local weather app for the latest forecast."
    elif "who are you" in user_input:
        return "I am a simple chatbot designed to assist you with basic tasks."
    else:
        return "Sorry, I don't understand your query. Can you please rephrase it?"
def chat():
    print("Chatbot: Hello! I am your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    chat()
