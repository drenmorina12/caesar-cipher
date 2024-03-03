from tkinter import *

root = Tk()
root.title("Testing")

input_label = Label(root, text="Input text")
input_label.grid(row=0, column=0)

input_text = Text(root)
input_text.grid(row=1, column=0)

key_label = Label(root, text="Key")
key_label.grid(row=0, column=1)

key_entry = Entry(root, width=4)
key_entry.insert(0, "5")
key_entry.grid(row=1, column=1, padx=5, pady=5)

output_label = Label(root, text="Output text")
output_label.grid(row=0, column=2)

output_text = Text(root)
output_text.grid(row=1, column=2)


def decrypted_text_output():
    output_text.delete("1.0", END)
    output_text.insert("1.0", input_text.get("1.0", END))


def encrypted_text_output():
    input_text.delete("1.0", END)
    input_text.insert("1.0", output_text.get("1.0", END))


encrypt_button = Button(root, text="Encrypt", command=decrypted_text_output)
encrypt_button.grid(row=2, column=0)

decrypt_button = Button(root, text="Decrypt", command=encrypted_text_output)
decrypt_button.grid(row=2, column=2)

root.mainloop()
