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
            shifted_letter = chr(ord(letter) + key if ord(letter) + key <= UPPERCASE_Z_ASCI
                                 else ord(letter) + key - ALPHABET_LETTERS * (max(1, key // ALPHABET_LETTERS)))
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


def decrypter_success_rate():
    sentences_to_test = [
        "Gur Frperg Vf Pbzr",
        "Abj vf gur fvkgu frn",
        "Fbzrbar fnlf vg vf zl fbpvrgl",
        "Lbh pna trg zr gb zl ubzr",
        "Lrf, guvf vf n frperg vachg",
        "Fb vf gur frperg nggenpgrq?",
        "V qvqa'g xabj guvf jnf noyr",
        "Gur arkg fvkgu frn vf jvyyrq",
        "Gur Tbyq Vf Pbzvat",
        "Gur Pbzvat vf gur Orfg",
        "Lbh pna trg gur fgbel",
        "Ubj vf guvf cbfg naq gurfr obqrf?",
        "Jung vf gur qvfgnapr bs gur Cnffjbeq?",
        "Lbh pna'g trg gur frperg bire gur obk",
        "Gur zlfgrel vf gur svefg tbbq qnl bs gur lrne",
        "Lbh pna trg zl frperg. Lbh qba'g unir gb xabj ubj.",
        "Gur frperg vf n uvag. Guvf vf n ovg.",
        "Gur Frperg vf njrfbzr",
        "Jr jvyy trg gur frperg naq qba'g unir gb bayl gur arkg",
        "Gur Fnyg Vf Pbzr",
        "Nzvgu vf gur frperg frn",
        "Fbzrbar fnlf vg vf zl qvfgnapr",
        "Lbh pna trg zr gb zl ubzr",
        "Lrf, guvf vf n frperg vachg",
        "Vg vf lbh'g ybatzragny",
        "Fb vf gur frperg nggenpgrq?",
        "V qvqa'g xabj guvf jnf noyr",
        "Gur arkg fvkgu frn vf jvyyrq",
        "Gur Tbyq Vf Pbzvat",
        "Gur Pbzvat vf gur Orfg",
        "Lbh pna trg gur fgbel",
        "Ubj vf guvf cbfg naq gurfr obqrf?",
        "Jung vf gur qvfgnapr bs gur Cnffjbeq?",
        "Lbh pna'g trg gur frperg bire gur obk",
        "Gur zlfgrel vf gur svefg tbbq qnl bs gur lrne",
        "Lbh pna trg zl frperg. Lbh qba'g unir gb xabj ubj.",
        "Gur frperg vf n uvag. Guvf vf n ovg.",
        "Gur Frperg vf njrfbzr",
        "Jr jvyy trg gur frperg naq qba'g unir gb bayl gur arkg",
        "Vg vf abg gur frperg"
    ]
    list_length = len(sentences_to_test)
    succesful_decryption = 0

    for s in sentences_to_test:
        decrypted_sentence = decrypter(s.upper())
        # print(decrypted_sentence[0])
        if decrypted_sentence[1] is not False:
            succesful_decryption += 1
        else:
            print(f"Couldnt decrypt: {s}")

    print(f"Success rate: {succesful_decryption/list_length * 100}%")


def main():
    # user_sentence = "Dren Morina"
    # user_key = 7
    # encrypted_sentence = encrypter(user_sentence, user_key)
    # print(encrypted_sentence)

    # for i in range(1, 26):
    # decrypted_sentence = simple_decrypter(user_sentence, user_key)
    # print(decrypted_sentence)

    # decrypted = decrypter(user_sentence)
    # print(f"The decrypted cipher is: {decrypted[0]}")
    # print(f"The key used is is: {decrypted[1]}")

    # decrypter_success_rate()
    return


main()
