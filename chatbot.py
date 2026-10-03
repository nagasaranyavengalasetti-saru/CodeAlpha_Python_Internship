def chatbot_response(message):

    message = message.lower()

    if message == "hello":
        return "Hi! How can I help you?"

    elif message == "hi":
        return "Hello!"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "My name is Python Chatbot."

    elif message == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


print("===== SIMPLE PYTHON CHATBOT =====")
print("Type 'bye' to exit.")

while True:

    user = input("\nYou: ")

    response = chatbot_response(user)

    print("Chatbot:", response)

    if user.lower() == "bye":
        break