#!/usr/bin/env python3
import sys
import subprocess
import readline
import time
from .assistant import get_command_suggestions

def main():
    last_tab_time = 0
    last_command = ""
    suggestions = []
    suggestion_index = 0

    while True:
        try:
            command = input("$ ")
            if command.strip() == "":
                continue

            if command == last_command and time.time() - last_tab_time < 0.5:
                if suggestions:
                    suggestion_index = (suggestion_index + 1) % len(suggestions)
                    print(f"\nCompleted command: {suggestions[suggestion_index]}")
                    readline.insert_text(suggestions[suggestion_index])
                    readline.redisplay()
            else:
                suggestions = get_command_suggestions(command)
                suggestion_index = 0
                print("\nSuggestions:")
                for i, suggestion in enumerate(suggestions, 1):
                    print(f"{i}. {suggestion}")

            last_command = command
            last_tab_time = time.time()

        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)
        except EOFError:
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    main()