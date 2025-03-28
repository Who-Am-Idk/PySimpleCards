import sys

def main():
    #Welcome the user to the program
    print("Flashcards!")
    flashcards = menu()
    print(flashcards)


def menu():
    user_input = input("CSV to flashcards (c)\nNew flashcard set (n)\nQuit application (q)\n\t> ")
    if user_input[0].lower() == 'q':
        exit(0)
    elif user_input[0].lower() == 'c':
        return csv_to_dict()
    elif user_input[0].lower() == 'n':
        #TODO: new flashcards
        return
    else:
        print("Unexpected input: " + user_input, file=sys.stderr)
        exit(1)

def csv_to_dict():
    """
    Ask user for csv file location, splits each line of file into 2 parts.

    Uses the first part of the split line as the key to each dictionary entry.
    returns dictionary.
    """
    #Ask user for file location
    file_location = input("Please enter the exact file location of your csv file:\n\t> ")
    file = open(file_location)
    temp = {}
    for line in file:
        if ',' not in line:
            continue
        line = (line.split(',', 1))
        temp[line[0]] = line[1].strip('\n')

    file.close()
    return temp



if __name__ == '__main__':
    main()