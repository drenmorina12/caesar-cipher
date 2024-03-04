from tkinter import *
from main import encrypter, decrypter, simple_decrypter, decrypter_success_rate

root = Tk()
root.title("Caesar Cipher")
# Input
input_label = Label(root, text="Input text")
input_label.grid(row=0, column=0)

input_text = Text(root, width=30, height=7, padx=5, pady=5)
input_text.grid(row=1, column=0, padx=10, pady=10)


def validate_input(char):  # Input INT validation
    return char.isdigit() or char == ""


key_label = Label(root, text="Key")
key_label.grid(row=0, column=1)

validation = root.register(validate_input)

# Key Frame
frame = LabelFrame(root, borderwidth=0, highlightthickness=0)
frame.grid(row=1, column=1)

key_entry = Entry(frame, width=4, validate="key", validatecommand=(validation, '%S'))
key_entry.insert(0, "5")
key_entry.grid(row=0, column=1)


def increment(op):
    key = key_entry.get()
    key_entry.delete(0, END)
    if key == '':
        key = "0"
    if op == 2:
        key_entry.insert(0, str(int(key) + 1))
    elif op == 1 and int(key) > 1:
        key_entry.insert(0, str(int(key) - 1))
    else:
        key_entry.insert(0, str(int(key)))


sub_button = Button(frame, text="-", width=2, height=1, command=lambda: increment(1))
sub_button.grid(row=0, column=0, padx=20, pady=10)

add_button = Button(frame, text="+", width=2, height=1, command=lambda: increment(2))
add_button.grid(row=0, column=2, padx=20, pady=10)


def key_state():
    if decrypt.get() == 2:
        key_entry.delete(0, END)
        key_entry.config(state="disabled")
    else:
        key_entry.config(state="normal")


decrypt = IntVar()
decrypt.set(1)
Radiobutton(root, text="Simple Decrypt", variable=decrypt, value=1, command=key_state).grid(row=2, column=1)
Radiobutton(root, text="Smart Decrypt", variable=decrypt, value=2, command=key_state).grid(row=3, column=1, pady=10)

# Output
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


def test_sample():
    decrypted_sample_result = decrypter_success_rate(test_entry.get())
    for msg in decrypted_sample_result:
        input_text.delete("1.0", END)
        input_text.insert("1.0", msg + "\n")


# testing_frame_label = Label(root, text="-Test the success rate of list of sentences")
# testing_frame_label.grid(row=4, column=1)

testing_frame = LabelFrame(root, padx=20, pady=20, text="Test the success rate of list of sentences")
testing_frame.grid(row=5, column=1, pady=20)

test_label = Label(testing_frame, text="Write file path:")
test_label.grid(row=4, column=1)

test_entry = Entry(testing_frame, width=30)
test_entry.grid(row=5, column=1, pady=5)

test_button = Button(testing_frame, text="Test", command=test_sample)
test_button.grid(row=6, column=1, pady=5)

root.mainloop()
