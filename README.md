# Caesar Cipher with GUI :lock::key:

This is a graphical user interface (GUI) application for encoding and decoding text using the Caesar Cipher technique. The application is built using Python and the Tkinter library, with additional dependencies on the art and Pillow libraries.

## Features
- **Encrypt Text:** Encode your message using a shift value.
- **Decrypt Text:** Decode your encrypted message using the same shift value.
- **Dynamic Alphabet Extension:** Automatically extends the alphabet if certain letters are present in the text.

## Usage
1.   Run the application:
```sh
python encrypt-decrypt.py
```
2. Using the GUI:
- **Type your message:** Enter the text you want to encrypt or decrypt in the provided input field.
- **Type the shift number:** Enter the numerical shift value for the Caesar Cipher.
- **Encrypt or Decrypt:** Click the "ENCRYPT" button to encode the message or the "DECRYPT" button to decode the message.
- The result will be displayed in the text area below the buttons.

&emsp; ![](https://github.com/emrenos/encrypt-decrypt/blob/main/crpyt-gif.gif)

## Installation
1. Clone the repository: 
```sh
git clone https://github.com/yourusername/encrypt-decrypt.git
cd encrypt-decrypt
```
2. Install the required libraries:
```sh 
pip install Pillow
```
3. Ensure Tkinter is installed:
Tkinter is usually included with Python, but if you need to install it manually, you can do so with your package manager. For example:
- &emsp; **On Ubuntu:**
```sh
sudo apt-get install python3-tk
```
- &emsp;  **On macOS with Homebrew:**
```sh
brew install python-tk
```

## Upcoming Updates
1. **GUI Integration** :white_check_mark:
2. **Advanced Encryption Method**: The encryption method will be upgraded from the Caesar Cipher to a more sophisticated algorithm to enhance security.

##
