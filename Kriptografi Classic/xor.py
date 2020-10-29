'''
    encrypt:
    plain: angkasa biru pagi yang indah
    pass: miku hatsune

    angkasa biru pagi yang indah
    miku hatsunemiku hatsunemiku
    ----------------------------- xor
    [12, 7, 12, 30, 65, 27, 0, 84, 17, 28, 28, 16, 77, 25, 10, 18, 73, 72, 24, 21, 29, 18, 78, 12, 3, 13, 10, 29]

    decrypt:
    [12, 7, 12, 30, 65, 27, 0, 84, 17, 28, 28, 16, 77, 25, 10, 18, 73, 72, 24, 21, 29, 18, 78, 12, 3, 13, 10, 29]
      m, i,  k,  u,   ,  h, a,  t,  s,  u,  n,  e,  m,  i,  k,  u,   ,  h,  a,  t,  s,  u,  n,  e, m,  i,  k,  u
    -------------------------------------------------------------------------------------------------------------- xor
    angkasa biru pagi yang indah
    

'''


def encrypt(plain,password):
    plain_int_vector = []
    for i in range(len(plain)):
        plain_int_vector.append(ord(plain[i]))
    password_int_vector = []
    for i in range(len(password)):
        password_int_vector.append(ord(password[i]))

    plain_index = 0
    cipher_int_vector = []
    while plain_index < len(plain):
        for i in range(len(password)):
            if plain_index == len(plain):
                break
            one_char_cipher = plain_int_vector[plain_index]^password_int_vector[i]
            cipher_int_vector.append(one_char_cipher)
            plain_index += 1
    return cipher_int_vector

def decrypt(cipher_int_vector,password):
    password_int_vector = []
    for i in range(len(password)):
        password_int_vector.append(ord(password[i]))
    cipher_index = 0
    plain_int_vector = []
    while cipher_index < len(cipher_int_vector):
        for i in range (len(password)):
            if cipher_index == len(cipher_int_vector):
                break
            one_char_plain = cipher_int_vector[cipher_index]^password_int_vector[i]
            plain_int_vector.append(one_char_plain)
            cipher_index += 1
    plain = ''
    for i in range(len(plain_int_vector)):
        plain = plain + chr(plain_int_vector[i])
    return plain

plain = input("Plain text: ")
password = input("Password: ")

cipher = encrypt(plain, password)
print ("Cipher: ", end='')
print(cipher)

print("Plain: " + decrypt(cipher,password))