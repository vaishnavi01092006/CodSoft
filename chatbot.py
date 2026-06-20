# ==========================================
# AI RULE-BASED CHATBOT
# CODSOFT - Task 1
# ==========================================

print("=================================")
print("      AI RULE-BASED CHATBOT")
print("=================================")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").strip().lower()

    if user == "hello":
        print("Bot: Hello! Welcome.")

    elif user == "hi":
        print("Bot: Hi! How are you?")

    elif user == "how are you":
        print("Bot: I am doing great! How about you?")

    elif user == "what is your name":
        print("Bot: My name is CodSoft AI Chatbot.")

    elif user == "who created you":
        print("Bot: I was created using Python for the CODSOFT AI Internship.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions based on predefined rules.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand. Please try another question.")