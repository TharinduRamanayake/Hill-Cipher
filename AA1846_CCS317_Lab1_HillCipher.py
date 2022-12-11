import string
import numpy as np

def encrypt():
    plainText = input("\nInput Your Plain Text: ").lower().replace(" ", "")
    print(f"\nPlain Text (No Spaces) : {plainText}")
    alphabet_list = list(string.ascii_lowercase)
    plainText_list = [alphabet_list.index(val) for i, val in enumerate(plainText)]
    if len(plainText_list)%2 != 0:
        plainText_list.append(0)
        print(f"\nLetter Position In alphabet:  {plainText_list}")

    while True:
        print("\nKey value should be in 4 characters")
        key = str(input("\nInput Key : ").lower())
        key_list = [alphabet_list.index(val) for i, val in enumerate(key)]
        key_matrix = np.array(key_list)
        if len(key) != 4:
            continue
        else:
            upper = [plainText_list[index] for index in range(0, len(plainText_list), 2)]
            lower = [plainText_list[index] for index in range(1, len(plainText_list), 2)]
            joined_plainText_list = upper + lower

            new_plainText_matrix = np.reshape(joined_plainText_list, (2, len(plainText_list) // 2))
            k_mat = np.reshape(key_matrix, (2, 2))
            cipher_matrix = np.matmul(k_mat, new_plainText_matrix)
            mod_matrix = np.mod(cipher_matrix, 26)

            two_mod_matrix = len(mod_matrix)
            mod_matrix_arr = np.array(mod_matrix).flatten()

            mod_upper = [mod_matrix_arr[index] for index in range(0, len(mod_matrix_arr)//2, 1)]
            mod_lower = [mod_matrix_arr[index] for index in range(len(mod_matrix_arr)//2, len(mod_matrix_arr), 1)]

            concat_matrix = np.stack((mod_upper, mod_lower), axis=1)
            flatten_concat_matrix = concat_matrix.flatten()
            cipher_list = [alphabet_list[val % 26] for index, val in enumerate(flatten_concat_matrix)]
            print(f'\nCipher List is : {cipher_list}')
            cipher_text = ""
            print(f"\nCipher Text is : {cipher_text.join(cipher_list)}")
            print("\n\n")
            break



if __name__ == '__main__':
    encrypt()



