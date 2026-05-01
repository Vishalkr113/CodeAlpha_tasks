import random
from datetime import datetime
import os

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot:", random.choice(["Hi!", "Hello!", "Hey there!"]))

        elif "how are you" in user_input:
            print("Chatbot:", random.choice(["I'm fine!", "Doing great!", "All good!"]))

        elif "your name" in user_input or "who are you" in user_input:
            print("Chatbot: I am CodeAlpha Bot, your friendly assistant!")

        elif "what can you do" in user_input:
            print("Chatbot: I can chat, tell time/date, jokes, and more!")

        elif "time" in user_input:
            print("Chatbot:", datetime.now().strftime("%H:%M:%S"))

        elif "date" in user_input:
            print("Chatbot:", datetime.now().strftime("%d-%m-%Y"))

        elif "joke" in user_input:
            jokes = [
                "Why do programmers hate nature? Too many bugs!",
                "Why did Python go to school? To become a better script!"
            ]
            print("Chatbot:", random.choice(jokes))

        elif "fact" in user_input:
            facts = [
                "Python was created by Guido van Rossum.",
                "The first computer bug was an actual moth.",
                "AI is transforming the world rapidly."
            ]
            print("Chatbot:", random.choice(facts))

        elif "motivation" in user_input:
            print("Chatbot: Keep learning, you're doing great! 💪")

        # ✅ SAFE CALCULATOR
        elif user_input.startswith("calculate"):
            parts = user_input.split()

            if len(parts) == 4:
                num1 = parts[1]
                op = parts[2]
                num2 = parts[3]

                if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
                    num1 = float(num1)
                    num2 = float(num2)

                    if op == "+":
                        print("Chatbot:", num1 + num2)
                    elif op == "-":
                        print("Chatbot:", num1 - num2)
                    elif op == "*":
                        print("Chatbot:", num1 * num2)
                    elif op == "/":
                        if num2 != 0:
                            print("Chatbot:", num1 / num2)
                        else:
                            print("Chatbot: Cannot divide by zero")
                    else:
                        print("Chatbot: Invalid operator (+, -, *, /)")
                else:
                    print("Chatbot: Invalid numbers")
            else:
                print("Chatbot: Use format → calculate 2 + 3")

        elif user_input.startswith("repeat"):
            text = user_input.replace("repeat", "").strip()
            print("Chatbot:", text)

        elif user_input == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')

        elif user_input == "bye":
            print("Chatbot: Goodbye! 👋")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()