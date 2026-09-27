# Simple Rule-Based Chatbot
# This is a beginner-friendly example of an AI-style application.
# It uses predefined rules rather than machine learning.

print("Simple Chatbot")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower().strip()

    if user == "bye":
        print("Bot: Goodbye!")
        break
    elif "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")
    elif "name" in user:
        print("Bot: I am a simple Python chatbot.")
    elif "python" in user:
        print("Bot: Python is a beginner-friendly programming language.")
    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: AI enables computers to perform tasks that normally require human intelligence.")
    else:
        print("Bot: Sorry, I don't understand that yet.")
