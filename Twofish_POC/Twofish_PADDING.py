import random as rd
import sys


def create_plaintext_for_encryption(plaintext, base_length):
    encoded_plaintext = plaintext.encode('utf-8')  # encoded byte string text
    padding_needed = base_length - (len(encoded_plaintext) % base_length) - 1  # length of padding
    padding = padding_needed.to_bytes(padding_needed + 1, "big")
    padded_encoded_plaintext = encoded_plaintext + padding  # padded encoded plaintext to be sent for encryption now
    return padded_encoded_plaintext


def revive_plaintext_from_padding(padded_encoded_plaintext):
    again_unpadded_encoded_plaintext = padded_encoded_plaintext[:-(padded_encoded_plaintext[-1] + 1)]
    again_plaintext = again_unpadded_encoded_plaintext.decode('utf-8')
    # print(again_plaintext, " ---> ", len(again_plaintext))
    return again_plaintext


def byte_xor(a, b):
    return bytes([_a ^ _b for _a, _b in zip(a, b)])


def generate_keys(length, no_of_keys):
    hexadecimal_string = '0123456789ABCDEF'
    keys = []
    for i in range(no_of_keys):
        current_key = ''
        for j in range(2 * length):
            current_key = current_key + hexadecimal_string[rd.randint(0, 15)]
        keys.append(bytes.fromhex(current_key))
    return keys


def split(message):
    assert len(message) % 2 == 0
    length = int(len(message) / 2)
    return message[:length], message[length:]


# Mainly the fiestel skeleton
def cipher_algorithm(input_txt, keys, f):
    for key in keys:
        L, R = split(input_txt)
        Ln = byte_xor(L, f(key, R))
        input_txt = R + Ln
    return Ln + R


if __name__ == '__main__':
    print("I am golu kuamr, okay")
