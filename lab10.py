import string

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'  # '/' represents space between words
}

def clean_text(text):
    """Removes invalid characters and converts text to lowercase."""
    return ''.join(char.lower() for char in text if char in MORSE_CODE_DICT)

def text_to_morse(text):
    """Converts cleaned text to Morse code."""
    return ' '.join(MORSE_CODE_DICT[char] for char in text)

# Get user input and process it
user_input = input("Enter a sentence: ")
cleaned_text = clean_text(user_input)
morse_code = text_to_morse(cleaned_text)

print(f"Morse Code: {morse_code}")
