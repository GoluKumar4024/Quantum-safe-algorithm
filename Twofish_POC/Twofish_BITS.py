import struct
import sys

WORD_BIGENDIAN = 0
if sys.byteorder == 'big':
    WORD_BIGENDIAN = 1


def reverse_bytewise_32bits(num):
    # reverse a 32 bit number by bytes
    # abcd => dcba, where a,b,c,d are 4 bytes together making 32 bit number abcd
    return ((num & 0xff) << 24) | (((num >> 8) & 0xff) << 16) | (((num >> 16) & 0xff) << 8) | ((num >> 24) & 0xff)


def rotate_left_32bit(num, n):
    # rotates number "num" by "n" bits left
    return (num << n & 0xfFFFFFFFF) | (num >> (32 - n))


def rotate_right_32bit(num, n):
    # rotates number "num" by "n" bits right
    return (num >> n) | ((num << (32 - n)) & 0xFFFFFFFF)


def nth_byte(x, n):
    # extracts n-th byte from the number given
    return (x >> 8 * n) & 0xff


def create_number_from_bytes(number_list):
    num = 0
    for i in range(len(number_list)):
        num = num | (number_list[i] << (8 * i))
    return num


if __name__ == '__main__':
    print("checking different operations with bytes")
    num = 2345
    number_list = [nth_byte(num, i) for i in range(4)]
    number_new = create_number_from_bytes(number_list)
    assert num == number_new
