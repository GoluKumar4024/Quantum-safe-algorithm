import Twofish_BITS as bts

q_t0 = [[8, 1, 7, 13, 6, 15, 3, 2, 0, 11, 5, 9, 14, 12, 10, 4],
        [2, 8, 11, 13, 15, 7, 6, 14, 3, 1, 9, 4, 0, 10, 12, 5]]
q_t1 = [[14, 12, 11, 8, 1, 2, 3, 5, 15, 4, 10, 6, 7, 0, 9, 13],
        [1, 14, 2, 11, 4, 12, 3, 7, 6, 13, 10, 5, 15, 9, 0, 8]]
q_t2 = [[11, 10, 5, 14, 6, 13, 9, 0, 12, 8, 15, 3, 2, 4, 7, 1],
        [4, 12, 7, 5, 1, 6, 9, 10, 0, 14, 13, 8, 2, 11, 3, 15]]
q_t3 = [[13, 7, 15, 4, 1, 2, 6, 14, 9, 11, 3, 0, 8, 5, 12, 10],
        [11, 9, 5, 1, 12, 3, 13, 14, 6, 4, 7, 15, 2, 0, 8, 10]]


def substitution(word_32_bits):
    byte_0 = bts.nth_byte(word_32_bits, 0)
    byte_1 = bts.nth_byte(word_32_bits, 1)
    byte_2 = bts.nth_byte(word_32_bits, 2)
    byte_3 = bts.nth_byte(word_32_bits, 3)

    # performing the permutations with substitution
    byte_0_encode = q_t0[byte_0 % 2][byte_0 % 16]
    byte_1_encode = q_t1[byte_1 % 2][byte_1 % 16]
    byte_2_encode = q_t2[byte_2 % 2][byte_2 % 16]
    byte_3_encode = q_t3[byte_3 % 2][byte_3 % 16]

    bytes_list = [byte_0_encode, byte_1_encode, byte_2_encode, byte_3_encode]

    return bts.create_number_from_bytes(bytes_list)
