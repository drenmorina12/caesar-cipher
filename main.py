ALPHABET_LETTERS = 26
UPPERCASE_Z_ASCI = 90

# user_sentence = input("Type the senctence you want to encrypt/decrypt: ").upper()
# user_key = int(input("Type the key you want it to be encrypted/decrypted with: "))

# user_sentence = "Zrgubq va juvpu rnpu yrggre va gur cynvagrkg vf ercynprq".upper()
# user_key = 7


def encrypter(sentence, key):
    encrypted_sentence = ""
    for letter in sentence.upper():
        if letter.isalpha():
            shifted_letter = chr((ord(letter) + key - ord('A')) % ALPHABET_LETTERS + ord('A'))
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
            if counter == 2:
                return current_sentence, i

    return "No solution found!", False


def decrypter_success_rate(file_path):
    with open(file_path, 'r') as file:
        sentence_list = file.read().splitlines()
    sentences_to_test = set(sentence_list)
    # print(sentences_to_test)

    list_length = len(sentences_to_test)
    succesful_decryption = 0
    error_messages = []

    for s in sentences_to_test:
        print(s)
        decrypted_sentence = decrypter(s.upper())
        # print(decrypted_sentence[0])
        if decrypted_sentence[1] is not False:
            succesful_decryption += 1
            print(decrypted_sentence)
            print("\n")
        else:
            error_messages.append(f"Couldnt decrypt: {s}")
            print(f"---Couldnt decrypt: {s}")

    error_messages.append(f"Success rate: {succesful_decryption/list_length * 100}%")
    error_messages.append(f"{succesful_decryption}/{list_length}")
    print(f"Success rate: {succesful_decryption/list_length * 100}%")
    print(f"{succesful_decryption}/{list_length}")

    return error_messages


def main():
    # user_sentence = "Dren Morina"
    # user_key = 43
    # encrypted_sentence = encrypter(user_sentence, user_key)
    # print(encrypted_sentence)

    # for i in range(1, 26):
    # decrypted_sentence = simple_decrypter(user_sentence, user_key)
    # print(decrypted_sentence)

    # decrypted = decrypter(user_sentence)
    # print(f"The decrypted cipher is: {decrypted[0]}")
    # print(f"The key used is is: {decrypted[1]}")

    decrypter_success_rate("sample.txt")
    return


main()
