"""
Rule-Based AI Chatbot
A simple conversational chatbot using if-else logic for predefined responses.
Author: Internship Project
Date: June 2026
"""


def display_welcome_message():
    """Display welcome message when chatbot starts."""
    print("=" * 60)
    print("Welcome to the Rule-Based AI Chatbot!")
    print("=" * 60)
    print("I'm here to assist you with basic questions.")
    print("Type 'help' to see what I can do, or 'exit' to quit.")
    print("=" * 60)
    print()


def display_farewell_message():
    """Display farewell message when user exits."""
    print("\nThank you for chatting with me!")
    print("Goodbye! Have a great day!")
    print("=" * 60)


def get_bot_response(user_input):
    """
    Process user input and return appropriate response.

    Args:
        user_input (str): The user's message in lowercase

    Returns:
        str: The chatbot's response
        None: If user wants to exit
    """

    # Handle greeting messages
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"

    elif user_input in ["good morning"]:
        return "Good morning! Hope you're having a wonderful day!"

    elif user_input in ["good afternoon"]:
        return "Good afternoon! How can I assist you?"

    elif user_input in ["good evening"]:
        return "Good evening! What can I do for you?"

    # Handle exit commands
    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        return None  # Signal to exit the chatbot

    # Handle predefined questions
    elif user_input == "what is your name":
        return "I'm a Rule-Based Chatbot, created to assist you with basic queries!"

    elif user_input == "how are you":
        return "I'm just a program, but I'm functioning perfectly! Thanks for asking. How are you?"

    elif user_input == "who created you":
        return "I was created as part of an AI internship project using Python!"

    elif user_input == "what can you do":
        return ("I can respond to greetings, answer basic questions about myself, "
                "and provide help. Type 'help' to see all available commands!")

    elif user_input == "help":
        help_text = """
Available Commands:
-------------------
Greetings:
  - hi, hello, hey
  - good morning, good afternoon, good evening

Questions I can answer:
  - what is your name
  - how are you
  - who created you
  - what can you do
  - help

Exit commands:
  - bye, exit, quit, goodbye

Try asking me any of these questions!
        """
        return help_text

    # Handle unknown inputs
    else:
        return "Sorry, I don't understand that. Please try another question."


def run_chatbot():
    """Main function to run the chatbot in a continuous loop."""

    # Display welcome message
    display_welcome_message()

    # Main conversation loop
    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Skip empty inputs
        if not user_input:
            print("Bot: Please enter a message.\n")
            continue

        # Convert to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()

        # Get bot response
        response = get_bot_response(user_input_lower)

        # Check if user wants to exit
        if response is None:
            display_farewell_message()
            break

        # Display bot response
        print(f"Bot: {response}\n")


# Entry point of the program
if __name__ == "__main__":
    run_chatbot()
