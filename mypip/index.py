#!/usr/bin/env python3

from cryptography.fernet import Fernet


def gen_key():
    return Fernet.generate_key()


def main(filename, key):
    with open(filename, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    eync_data = fernet.encrypt(data)
    with open(filename + ".encrypted", "wb") as file:
        file.write(eync_data)
    print("done! ")


def passd(filename, key):
    paddf = input("enter the pass!: ")
    if paddf == "passed":
        gen_key()
        main(filename, key)
        with open("gen.key", "wb") as file:
            file.write(key)
        print(f"key gen sucessfull into gen.key as key = {key}")
    else:
        print("fuck off")


key = gen_key()
filename = "text.txt"
passd(filename, key)
