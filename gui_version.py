from tkinter import *
from main import encrypter, decrypter, simple_decrypter, decrypter_success_rate

root = Tk()
root.title("Testing")

input_label = Label(root, text="Input text")
input_label.grid(row=0, column=0)

input_text = Text(root, width=30, height=7, padx=5, pady=5)
input_text.grid(row=1, column=0, padx=10, pady=10)

key_label = Label(root, text="Key")
key_label.grid(row=0, column=1)


def validate_input(char):  # Input INT validation
    return char.isdigit() or char == ""


validation = root.register(validate_input)

key_entry = Entry(root, width=4, validate="key", validatecommand=(validation, '%S'))
key_entry.insert(0, "5")
key_entry.grid(row=1, column=1, padx=5, pady=5)


def key_state():
    if decrypt.get() == 2:
        key_entry.config(state="disabled")
    else:
        key_entry.config(state="normal")


decrypt = IntVar()
decrypt.set(1)
Radiobutton(root, text="Simple Decrypt", variable=decrypt, value=1, command=key_state).grid(row=2, column=1)
Radiobutton(root, text="Smart Decrypt", variable=decrypt, value=2, command=key_state).grid(row=3, column=1)

output_label = Label(root, text="Output text")
output_label.grid(row=0, column=2)

output_text = Text(root, width=30, height=7)
output_text.grid(row=1, column=2, padx=10, pady=10)


def decrypted_text_output():
    output_text.delete("1.0", END)
    output_text.insert("1.0", encrypter(input_text.get("1.0", 'end-1c'), int(key_entry.get())))
#     end-1c instead of END to avoid adding new line


def encrypted_text_output():
    input_text.delete("1.0", END)
    if decrypt.get() == 1:
        input_text.insert("1.0", simple_decrypter(output_text.get("1.0", 'end-1c'), int(key_entry.get())))
    else:
        decrypted_message = decrypter(output_text.get("1.0", "end-1c"))
        input_text.insert("1.0", decrypted_message[0])
        key_entry.config(state="normal")
        key_entry.delete(0, END)
        key_entry.insert(0, decrypted_message[1])
        key_entry.config(state="disabled")
        return


encrypt_button = Button(root, text="Encrypt", command=decrypted_text_output)
encrypt_button.grid(row=2, column=0)

decrypt_button = Button(root, text="Decrypt", command=encrypted_text_output)
decrypt_button.grid(row=2, column=2)

root.mainloop()
