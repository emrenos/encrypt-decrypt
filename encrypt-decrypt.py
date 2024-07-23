import tkinter as tk
from art import logo
from PIL import Image, ImageTk
from a import alphabet

def extend_alphabet(text, shift):
    if any(letter in {'v', 'w', 'x', 'y', 'z'} for letter in text):
        alphabet.extend(alphabet)

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % len(alphabet)
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift) % len(alphabet)
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += letter
    return decrypted_text

def on_encrypt():
    text = input_text.get()
    shift = int(shift_entry.get())
    extend_alphabet(text, shift)
    encrypted = encrypt(text, shift)
    update_result_text(f"Encoded Text: {encrypted}")

def on_decrypt():
    text = input_text.get()
    shift = int(shift_entry.get())
    extend_alphabet(text, shift)
    decrypted = decrypt(text, shift)
    update_result_text(f"Decoded Text: {decrypted}")

def update_result_text(message):
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, message, "bold")
    result_text.config(state=tk.DISABLED)

def validate_entry(action, value_if_allowed, text, prior_value, insertion_index, event_type, *args):
    if action == '1' and not text.isdigit():
        return False
    return True

# GUI Setup
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("500x400")
window.resizable(False, False)

# Set window icon
icon_image = Image.open("caesar-cipher.png")
icon_photo = ImageTk.PhotoImage(icon_image)
window.iconphoto(False, icon_photo)

# Define custom fonts and colors
font_title = ("Helvetica", 12, "bold")
font_text = ("Helvetica", 10)
bg_color = "#1E1E1E"
fg_color = "#FFFFFF"
lg_color = "#A1BD2F"
lbl_color = "#D9D9D9"
en_btn_color = "#3E7EAC"

# Set background color for the window
window.configure(bg=bg_color)

# Display the logo
logo_label = tk.Label(window, text=logo, font=("Courier", 2), fg=lg_color, bg=bg_color)
logo_label.pack(pady=10)

# Input Text
input_label = tk.Label(window, text="Type your message:", font=font_text, bg=bg_color, fg=fg_color)
input_label.pack(pady=5)
input_text = tk.Entry(window, width=50, font=font_text, bg=lbl_color)
input_text.pack(pady=5)

# Shift Number
shift_label = tk.Label(window, text="Type the shift number:", font=font_text, bg=bg_color, fg=fg_color)
shift_label.pack(pady=5)

vcmd = (window.register(validate_entry), '%d', '%P', '%S', '%s', '%i', '%V')
shift_entry = tk.Entry(window, width=5, font=font_text, bg=lbl_color, validate='key', validatecommand=vcmd)
shift_entry.pack(pady=5)

# Result Text
result_text = tk.Text(window, height=5, width=50, font=font_text, bg=lbl_color)
result_text.pack(pady=20)
result_text.tag_configure("bold", font=("Helvetica", 10, "bold"))
result_text.config(state=tk.DISABLED)

# Encrypt and Decrypt Buttons
button_frame = tk.Frame(window, bg=bg_color)
button_frame.pack(pady=20)

encrypt_button = tk.Button(button_frame, text="ENCRYPT", command=on_encrypt, width=10, font=font_title, bg=en_btn_color, fg=bg_color)
encrypt_button.pack(side=tk.LEFT, padx=35)

decrypt_button = tk.Button(button_frame, text="DECRYPT", command=on_decrypt, width=10, font=font_title, bg=lg_color, fg=bg_color)
decrypt_button.pack(side=tk.RIGHT, padx=35)

window.mainloop()
