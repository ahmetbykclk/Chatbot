from nltk.chat.util import Chat, reflections

# Define the chatbot responses using patterns and corresponding replies
chatbot_responses = [
    # Greetings
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    # Inquire about chatbot's well-being
    ['how are you', ['I am doing well, thank you!', 'I am good, how about you?']],
    # Farewells
    ['bye|goodbye', ['Goodbye!', 'See you later!', 'Take care!']],
    # Respond to questions about chatbot's identity
    ['name', ['I am just a chatbot.', 'I am an AI chatbot.']],
    # Offer assistance
    ['help', ['How can I assist you?', 'I am here to help.']]
]

# Create a chatbot instance
chatbot = Chat(chatbot_responses, reflections)

def main():
    print("Chatbot: Hi, I'm your friendly chatbot. Type 'bye' to exit.")
    while True:
        # Get user input
        user_input = input("You: ")
        # Check if user wants to exit
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            # Provide a response based on user input
            response = chatbot.respond(user_input)
            if response:
                print("Chatbot:", response)
            else:
                print("Chatbot: I'm sorry, I don't understand. Could you please rephrase that?")

# Run the chatbot
if __name__ == "__main__":
    main()
