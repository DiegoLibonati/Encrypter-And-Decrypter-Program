# coding: utf8
from tkinter import *
from tkinter import filedialog

class Program():
    def __init__(self, master):
        master.title("Encrypter And Decrypter")
        master.geometry("800x300+0+0")
        master.config(bg="#fff")
        master.resizable(False, False)

        self.font_family = "Times"
        self.path = ""
        self.entry_password = StringVar(value="Password")
        self.text_import_file = StringVar()
        self.text_operation_result = StringVar()

        Button(width=20, height=1, text="Import File", relief="raised", bg="white",borderwidth=1, command=lambda:self.select_file()).place(x=10, y=10)
        Label(font=(self.font_family, 12), textvariable=self.text_import_file, bg="white", fg="black").place(x=200, y=10)

        Entry(width=20,bg="#fff", font=(self.font_family, 14), textvariable=self.entry_password, show="*").place(x=400, y=100,anchor="center")

        Button(width=20, height=1,font=(self.font_family, 15), text="ENCRYPT", relief="raised", bg="RED",fg="#FFF",borderwidth=1, command=lambda:self.encrypt_file(self.path)).place(x=150, y=150)
        Button(width=20, height=1,font=(self.font_family, 15), text="DECRYPT", relief="raised", bg="GREEN",fg="#FFF",borderwidth=1, command=lambda:self.decrypt_file(self.path)).place(x=400, y=150)
        Label(font=(self.font_family, 12), textvariable=self.text_operation_result, bg="white", fg="black").place(x=400, y=250, anchor="center")

    def select_file(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

        self.text_import_file.set(filename)
        self.path = filename

    def get_text(self, path):
        text = open(path, "r")
        final_text_to_write = text.read()
        text.close()

        return final_text_to_write

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

root = Tk()

program = Program(root)

root.mainloop()