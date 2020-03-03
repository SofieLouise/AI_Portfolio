morse_dictionary = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0'
}


def decrypt(message):
    output = ''
    words = message.split(sep=7 * ' ')
    for word in words:
        letters = word.split(sep=3 * ' ')
        for morse_letter in letters:
            letter = morse_dictionary.get(morse_letter, 'Not valid')
            output += letter
        output += ' '
    return output


def encrypt(message):
    output = ''
    words = message.upper().split()
    for word in words:
        for letter in word:
            morse_letter = list(morse_dictionary.keys())[list(morse_dictionary.values()).index(letter)]
            output += morse_letter + (3 * ' ')
        output += (7 * ' ')
    return output


finished = False
while not finished:
    user_input = input("Type 'encrypt' or 'decrypt' to choose translation direction: ").upper()
    if user_input == 'DECRYPT':
        morse_input = input('Please write a morse sequence: ')
        print(decrypt(morse_input))
    elif user_input == 'ENCRYPT':
        word_input = input('Please write a word sequence: ')
        print(encrypt(word_input))
    elif user_input == 'QUIT':
        finished = True
