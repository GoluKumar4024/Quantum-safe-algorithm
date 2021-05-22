def poly_multi_modulo(poly_one, poly_two, irreducible_polynomial):
    product = 0
    while poly_one > 0 and poly_two > 0:
        if poly_two & 1:
            product ^= poly_one
        if poly_one & 0x80:
            poly_one = (poly_one << 1) ^ irreducible_polynomial
        else:
            poly_one <<= 1
        poly_two >>= 1
    return product


def matrix_modulo(mds_matrix, input_vector, irreducible_polynomial):
    output_vector = []
    for i in range(4):
        value = 0
        for j in range(4):
            value ^= poly_multi_modulo(input_vector[i], mds_matrix[j][i], irreducible_polynomial)
        output_vector.append(value)
    return output_vector


def MDS_function(input_vector):
    irreducible_poly = 0x169  # irreducible polynomial
    mds_matrix = [[0x01, 0x5B, 0x5B, 0x5B], [0x5B, 0xEF, 0xEF, 0x01],
                  [0xEF, 0x5B, 0x01, 0xEF], [0xEF, 0x01, 0xEF, 0x5B]]
    output_vector = matrix_modulo(mds_matrix, input_vector, irreducible_poly)
    return output_vector


if __name__ == '__main__':
    print("Here i will be using only MDS matrix as function g()")
    input_vector = [0xAB, 0xD4, 0x43, 0xE2]
    print(MDS_function(input_vector))
