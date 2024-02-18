from cryptography.fernet import Fernet
import os


filee = "text.txt"
enc_file = "text.xyz"


def key_gen():
    return Fernet.generate_key()


def load_key(k):
    with open(k, "rb") as file:
        return file.read()


def enc(filee, key):
    f = Fernet(key)
    with open(filee, "rb") as file:
        data = file.read()
    encc = f.encrypt(data)
    enc_filee = filee.replace(".txt", ".xyz")
    with open(enc_filee, "wb") as file:
        file.write(encc)
    os.remove(filee)
    print("enc done!")


def dec(k, enc_file):
    with open(enc_file, "rb") as file:
        data = file.read()
    f = Fernet(k)
    decc = f.decrypt(data)
    def_filee = enc_file.replace(".xyz", ".txt")
    with open(def_filee, "wb") as file:
        file.write(decc)
    os.remove(enc_file)
    print("decc deone")


password = input("enter pass: ")

if password == "enc":
    key = key_gen()
    with open("gen.key", "wb") as file:
        file.write(key)
    enc(filee, key)
elif password == "dec":
    key_generated = "gen.key"
    k = load_key(key_generated)
    dec(k, enc_file)
else:
    print("none")
