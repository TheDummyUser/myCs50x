#!/usr/bin/env python3
import os

from cryptography.fernet import Fernet


def load_key(k):
    with open(k, "rb") as file:
        return file.read()


def dec_file(k, enc_f):
    with open(enc_f, "rb") as file:
        enc_data = file.read()

        fernet = Fernet(k)
        dec_data = fernet.decrypt(enc_data)

        def_filee = enc_f.replace(".encrypted", "")
        with open(def_filee, "wb") as file:
            file.write(dec_data)
            os.remove(enc_f)


enc_f = "text.txt.encrypted"
k_file = "gen.key"

k = load_key(k_file)
dec_file(k, enc_f)
