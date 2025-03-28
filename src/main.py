import sys

def main():
    #Welcome the user to the program
    print("Flashcards!")
    menu()


def menu():
    user_input = input("CSV to flashcards (c)\nNew flashcard set (n)\nQuit application (q)")
    if user_input[0].lower() == 'q':
        exit(0)
    elif user_input[0].lower() == 'c':
        csv_to_dict()
    elif user_input[0].lower() == 'n':
        #TODO: new flashcards
        return
    else:
        print("Unexpected input: " + user_input, file=sys.stderr)
        exit(1)

def csv_to_dict():
    return


if __name__ == '__main__':
    main()