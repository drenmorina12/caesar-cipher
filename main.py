ALPHABET_LETTERS = 26
LAST_LETTER = 90

# user_sentence = input("Type the senctence you want to encrypt/decrypt: ").upper()
# user_key = int(input("Type the key you want it to be encrypted/decrypted with: "))

user_sentence = "am toawzm wg pwu".upper()
# user_key = 5

def encrypter(sentence, key):
    encrypted_sentence = ""
    for letter in sentence:
        if letter.isalpha():
            shifted_letter = chr(ord(letter) + key if ord(letter) + key <= LAST_LETTER
                                 else ord(letter) + key - ALPHABET_LETTERS)
            # Makes it so it only works with A-Z chars
            encrypted_sentence += shifted_letter
        else:
            encrypted_sentence += letter

    return encrypted_sentence.lower()


def simple_decrypter(sentence, key):
    return encrypter(sentence, ALPHABET_LETTERS - key)


def decrypter(sentence):
    with open("word_list.txt", 'r') as file:
        word_list = file.read().splitlines()
    common_words = set(word_list)

    for i in range(1, 26):
        current_sentence = simple_decrypter(sentence, i)
        # print(current_sentence)
        counter = 0
        for word in current_sentence.split():
            if word in common_words:
                counter += 1
            if counter == 3:
                return current_sentence, i

        counter = 0

    return "No solution found!"




def main():
    # encrypted_sentence = encrypter(user_sentence, user_key)
    # print(encrypted_sentence)

    # for i in range(1, 26):
    #     decrypted_sentence = simple_decrypter(user_sentence, i)
    #     print(decrypted_sentence)

    decrypted = decrypter(user_sentence)
    print(f"The decrypted cipher is: {decrypted[0]}")
    print(f"The key used is is: {decrypted[1]}")

main()
