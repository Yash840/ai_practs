
import re

def chatbot_response(user_input):


    user_input = user_input.lower()

    if re.search(r"\b(hello|hi|hey)\b", user_input):
        return "Hello! How can I help you?"

    elif re.search(r"\b(your name|who are you)\b", user_input):
        return "I am a simple Python chatbot."

    elif re.search(r"\bhow are you\b", user_input):
        return "I am doing great! Thanks for asking."

    elif re.search(r"\b(your purpose|what can you do)\b", user_input):
        return "I can answer simple questions using predefined rules."

    elif re.search(r"\b(weather)\b", user_input):
        return "I cannot check live weather, but I hope it is nice today!"

    elif re.search(r"\b(thank you|thanks)\b", user_input):
        return "You're welcome!"

    elif re.search(r"\b(bye|goodbye|exit)\b", user_input):
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."


print("Chatbot: Hello! Type 'bye' to exit.")

while True:

    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    if re.search(r"\b(bye|goodbye|exit)\b", user_input.lower()):
        break
