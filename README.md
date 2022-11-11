# Encrypter-And-Decrypter-Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Install requirements.txt
4. Use `python encrypt_decrypt_program.py` to execute program

## Description

I made a python program using tkinter as user interface. This program allows to encrypt text files, and also to decrypt them as long as we know a password.

## Technologies used

1. Python

## Libraries used

1. Tkinter

## Galery

![Encrypter-And-Decrypter-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/encranddecr-0.jpg)

![Encrypter-And-Decrypter-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/encranddecr-1.jpg)

![Encrypter-And-Decrypter-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/encranddecr-2.jpg)

![Encrypter-And-Decrypter-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/encranddecr-3.jpg)

![Encrypter-And-Decrypter-program](https://raw.githubusercontent.com/DiegoLibonati/DiegoLibonatiWeb/main/data/projects/Python/Imagenes/encranddecr-4.jpg)

## Portfolio Link

`https://diegolibonati.github.io/DiegoLibonatiWeb/#/projects?q=Encrypter%20and%20Decrypter%20program`

## Video

https://user-images.githubusercontent.com/99032604/199141421-8723b21b-bc04-4c59-be1a-d1342800a1c0.mp4

## Documentation

In this `select_file()` function we get the file we are loading:

```
def select_file(self):
    filename = filedialog.askopenfilename(initialdir = "/",
                                        title = "Select a File",
                                        filetypes = (("Text files",
                                                    "*.txt*"),
                                                    ("all files",
                                                    "*.*")))

    self.text_import_file.set(filename)
    self.path = filename
```

In this function `get_text()` we get the text to edit:

```
def get_text(self, path):
    text = open(path, "r")
    final_text_to_write = text.read()
    text.close()

    return final_text_to_write
```

In this function `encrypt_file()` we are going to encrypt the file when we have entered the correct password, it will make an encryption with `ord and chr` letter by letter and when the button is clicked this function will be executed:

```
def encrypt_file(self, path):

    if self.entry_password.get() == "hola":
        try:
            final_text = ""
            text = self.get_text(path)

            for letter in text:
                new_letter = ord(letter) + 1
                new_letter = chr(new_letter)
                final_text += new_letter

            file_to_encrypt = open(path, "w")

            file_to_encrypt.write(final_text)

            file_to_encrypt.close()

            self.text_operation_result.set("Successfully encrypted")
        except:
            self.text_operation_result.set("You must insert a txt file to encrypt")
    else:
        self.text_operation_result.set("INVALID PASSWORD")
```

In this function `decrypt_file()` we are going to decrypt the file when we have entered the correct password, it will do a decryption with `ord and chr` letter by letter and when the button is clicked this function will be executed:

```
def decrypt_file(self, path):

    if self.entry_password.get() == "hola":
        try:
            final_text = ""
            text = self.get_text(path)

            for letter in text:
                new_letter = ord(letter) - 1
                new_letter = chr(new_letter)
                final_text += new_letter

            file_to_decrypt = open(path, "w")

            file_to_decrypt.write(final_text)

            file_to_decrypt.close()

            self.text_operation_result.set("Successfully decrypted")
        except:
            self.text_operation_result.set("You must insert a txt file to decrypt")
    else:
        self.text_operation_result.set("INVALID PASSWORD")
```
