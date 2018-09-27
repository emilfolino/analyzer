#!/usr/bin/env python3
import sys

import menu
import analyzer

def main():
    """
    Main function with command loop
    """
    current_file = ""

    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")

        input_text = menu.show_menu(current_file)
        choice = input(input_text)

        if choice == "quit":
            break
        elif choice == "change":
            current_file = ""
        elif choice == "lines":
            analyzer.lines(current_file)
        elif choice == "words":
            analyzer.words(current_file)
        elif choice == "letters":
            analyzer.letters(current_file)
        elif choice == "word_frequency":
            analyzer.word_frequency(current_file)
        elif choice == "letter_frequency":
            analyzer.letter_frequency(current_file)
        elif choice == "all":
            analyzer.all(current_file)
        elif not current_file:
            current_file = choice
        else:
            print(choice + " matchar inget val")

        print()
        input("Tryck enter för att komma vidare")

    sys.exit(0)


if __name__ == "__main__":
    main()
