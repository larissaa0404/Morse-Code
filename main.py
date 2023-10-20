print("Welcome to the Morse Code Translator")
phrase = input("Please type what do you want to say: \n")
alphabet = {"a": ".--", "b": "--...",  "c": "--.--.", "d": "--..", "e": ".", "f": "..--.", "g": "----.", "h": "....",
            "i": "..", "j": ".------", "k": "--.--", "l": ".--..", "m": "----", "n": "--.", "o": "------", "p": ".----.",
            "q": "----.--", "r": ".--.", "s": "...", "t": "--", "u": "..--", "v": "...--", "w": ".----", "x": "--..--",
            "y": "--.----", "z": "----..", "1": ".--------", "2": "..------", "3": "...----", "4": "....--", "5": ".....",
            "6": "--....", "7": "----...", "8": "------..", "9": "--------.", "0": "----------", ', ': '--..--', '.': '.-.-.-',
            '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}


def encode():
    morse_code = ""
    for letter in phrase:
        if letter in alphabet:
            morse_code += alphabet[letter]
        else:
            if letter == " ":
                morse_code += "  "
    sentence = " ".join(map(str, morse_code))
    print(f"Here's the encoded sentence: {sentence}")

encode()
