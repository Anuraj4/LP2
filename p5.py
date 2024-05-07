import random

# Dictionary of predefined responses
responses = {
    "greeting": ["Hello!", "Hi!", "Welcome!"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
    "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"]
}
def generate_response(user_input):
    user_input = user_input.lower()
    # Check for common keywords in user input
    if any(word in user_input for word in ["hello", "hi"]):
        return random.choice(responses["greeting"])
    elif any(word in user_input for word in ["goodbye", "bye"]):
        return random.choice(responses["farewell"])
    elif "thank" in user_input:
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["default"])

# Main interaction loop
while True:
    # Get user input
    user_input = input("User: ")
    # Generate and display bot response
    bot_response = generate_response(user_input)
    print("Bot:", bot_response)
