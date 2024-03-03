from tkinter import *

root = Tk()
root.title("Testing")

input_label = Label(root, text="Input text")
input_label.grid(row=0, column=0)

input_entry = Entry(root)
input_entry.grid(row=1, column=0)

output_label = Label(root, text="Output text")
output_label.grid(row=0, column=2)

output_entry = Entry(root)
output_entry.grid(row=1, column=2)


def decrypted_text_output():
    output_entry.delete(0, END)
    output_entry.insert(0, input_entry.get())


def encrypted_text_output():
    input_entry.delete(0, END)
    input_entry.insert(0, output_entry.get())


encrypt_button = Button(root, text="Encrypt", command=decrypted_text_output)
encrypt_button.grid(row=2, column=0)

decrypt_button = Button(root, text="Decrypt", command=encrypted_text_output)
decrypt_button.grid(row=2, column=2)

root.mainloop()
