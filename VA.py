# VOICE ASSISTANT

import datetime

def respondToCommand(command):
    command = command.strip().lower()

    if command == "hello":
        print("Hello! How can I help you?")
    elif command == "what's the time":
        currentTime = datetime.datetime.now()
        print("Current time:", currentTime.strftime("%H:%M"))
    elif command == "what's the date":
        currentDate = datetime.datetime.now()
        print("Current date:", currentDate.strftime("%d/%m/%Y"))
    elif command.startswith("search for"):
        query = command[11:].strip()
        print("Searching the web for:", query)
    else:
        print("I'm sorry, I don't understand that command.")
        print("Voice Assistant: Say a command...")
        userCommand = input()
        respondToCommand(userCommand)