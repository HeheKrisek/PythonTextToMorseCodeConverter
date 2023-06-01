textsymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
         '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
         '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']


def tomorsecode(ipt):
    text_to_convert = ipt.lower()
    morse_text = ''
    for letter in text_to_convert:
        if letter in textsymbols:
            i = textsymbols.index(letter)
            morse_text = morse_text + morse[i]

        else:
            morse_text = morse_text + letter

        morse_text = morse_text + " "

    return morse_text


def tochar(ipt):
    morse_to_convert = ipt.lower()
    if morse_to_convert in morse:
        i = morse.index(morse_to_convert)
        return textsymbols[i]

    else:
        return 'Invalid morse code symbol'


def morsetoletters(letters):
    user_input = input("Enter a piece of morse code (.-, -..., etc.): ")
    print(f"This is letter: {tochar(user_input)}")
    letters.append(tochar(user_input))
    print(f"Your letters: {letters}")
    again = input("Do you want to check another letter? (y - yes, another answer - no)")
    if again.lower() == 'y':
        morsetoletters(letters)

    else:
        choice()

def choice():
    ch = input("What do you want to do? (1 - Convert a string to morse code,"
                   " 2 - convert morse code symbols to letters, "
                   "3 - exit)")

    if ch == '1':
        user_input = input("Enter a string: ")
        print(tomorsecode(user_input))
        choice()

    elif ch == '2':
        letters = []
        morsetoletters(letters)

    elif ch == '3':
        exit()

    else:
        print("invalid choice, try again")
        choice()


choice()
