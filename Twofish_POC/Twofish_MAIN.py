import sys
from sys import platform

import Twofish_MDS as mds
import Twofish_BITS as bts
import Twofish_PADDING as padd
import S_BOX as sbox
import struct


def function_F(input_0, input_1, key_i):
    tmp_r0 = [bts.nth_byte(input_0, i) for i in range(4)]
    tmp_r1 = [bts.nth_byte(input_1, i) for i in range(4)]

    tmp_t0 = mds.MDS_function(tmp_r0)
    tmp_t1 = mds.MDS_function(tmp_r1)

    key_i_0, key_i_1 = struct.unpack("<2L", key_i)

    tmp_t0 = bts.create_number_from_bytes(tmp_t0)
    tmp_t1 = bts.create_number_from_bytes(tmp_t1)

    # applying substitution now
    tmp_t0 = sbox.substitution(tmp_t0)
    tmp_t1 = sbox.substitution(tmp_t1)

    t0 = tmp_t0 ^ key_i_0
    t1 = tmp_t1 ^ key_i_1

    return t0, t1


def round_function(plaintext, keys, i):
    r0_i = plaintext[0]
    r1_i = plaintext[1]
    r2_i = plaintext[2]
    r3_i = plaintext[3]

    # Apply the function F
    f2_i, f3_i = function_F(r2_i, r3_i, keys[i])

    r2_i1 = f2_i ^ r0_i
    r3_i1 = f3_i ^ r1_i
    r0_i1 = r2_i
    r1_i1 = r3_i

    return [r0_i1, r1_i1, r2_i1, r3_i1]


def encrypt(plaintext, keys):
    ENCODE_PACK = '<4L'

    ciphertext = b''
    while plaintext:
        # print(enc_padded_plaintext[:16])
        a, b, c, d = struct.unpack("<4L", plaintext[:16])
        plaintext = plaintext[16:]
        temp_ciphertext = [a, b, c, d]  # This is the plain text represented as list of 4 32bit integer
        for i in range(16):
            temp_ciphertext = round_function(temp_ciphertext, keys, i)
        [a, b, c, d] = temp_ciphertext
        new_ciphertext = [c, d, a, b]
        ciphertext += struct.pack(ENCODE_PACK, *new_ciphertext)
    return ciphertext


if __name__ == '__main__':
    # plaintext = """I am golu kumar, and this is the messsage to be sent by me!! I am trying to broaden this message
    #             """
    # plaintext="""  书、杂志等中区 别于图片的  正文，文字材料 """
    plaintext=""" गग गडड जजजज    जजजजज जज"""
    print(
        "PLAINTEXT =======================================================================================================")
    print(plaintext)
    print(
        "ENCODED PLAINTEXT ================================================================================================")
    keys = padd.generate_keys(8, 16)
    enc_padded_plaintext = padd.create_plaintext_for_encryption(plaintext, 16)
    print(enc_padded_plaintext)
    print(
        "CIPHERTEXT========================================================================================================")

    # printing keys as left and right splitted
    # for key in keys:
    #     print(key)
    #     print(type(key))
    #     print("Key is :: ", type(key[:8]), " ", type(key[8:]))
    #     print("Key is :: ", key[:8], " ", key[8:])
    #     print("==========================================")
    ciphertext = encrypt(enc_padded_plaintext, keys)
    print(ciphertext)
    print(
        "DECRYPTED ENCODED PLAINTEXT=======================================================================================")
    keys.reverse()
    plain_again = encrypt(ciphertext, keys)
    print(plain_again)
    print(
        "ORIGINAL PLAINTEXT=================================================================================================")
    plain_again = padd.revive_plaintext_from_padding(plain_again)
    print(plain_again)
