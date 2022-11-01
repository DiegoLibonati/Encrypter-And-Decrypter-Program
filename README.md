# Encrypter-And-Decrypter-Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Install requirements.txt
4. Use `python encrypt_decrypt_program.py` to execute program

## Description

I made a python program using tkinter as user interface. This program allows to encrypt text files, and also to decrypt them as long as we know a password.

## Feel free to edit my code

We get the file from here

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

We get the text of the that file from here

```
def get_text(self, path):
    text = open(path, "r")
    final_text_to_write = text.read()
    text.close()

    return final_text_to_write
```

We change letter by letter to encrypt and to decrypt like this

```
for letter in text:
    new_letter = ord(letter) + 1
    new_letter = chr(new_letter)
    final_text += new_letter

for letter in text:
    new_letter = ord(letter) - 1
    new_letter = chr(new_letter)
    final_text += new_letter
```

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

