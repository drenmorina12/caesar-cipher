ALPHABET_LETTERS = 26
LAST_LETTER = 90

user_sentence = input("Type the senctence you want to encrypt/decrypt: ").upper()
user_key = int(input("Type the key you want it to be encrypted/decrypted with: "))


def encrypter(sentence, key):
    encrypted_sentence = ""
    for letter in sentence:
        if letter.isalpha():
            shifted_letter = chr(ord(letter) + key if ord(letter) + key <= LAST_LETTER
                                 else ord(letter) + key - ALPHABET_LETTERS)
            encrypted_sentence += shifted_letter
        else:
            encrypted_sentence += letter

    return encrypted_sentence.lower()


def simple_decrypter(sentence, key):
    return encrypter(sentence, -key)


def main():
    # encrypted_sentence = encrypter(user_sentence, user_key)
    # print(encrypted_sentence)

    decrypted_sentence = simple_decrypter(user_sentence, user_key)
    print(decrypted_sentence)


main()
