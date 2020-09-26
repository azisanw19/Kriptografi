"""
vignere
plain: angkasa biru pagi
password: b i n  t  a n  g
          1 8 13 19 0 13 6
a n g  k  a s  a _ b i  r  u _  p a g i
1 8 13 19 0 13 6 1 8 13 19 0 13 6 1 8 13

cipher
bvt2a4g0jv9ucvbov

rectangle
plain: bvt2a4g0jv9ucvbov
len(bintang) = 7

bvt2a4g
0jv9ucv
bov

cipher
b0bvjo29 au 4c gv

"""

letters = "abcdefghijklmnopqrstuvwxyz 0123456789"
inv_letters = {}
n_letters = len(letters)

for i in range(n_letters):
    inv_letters[letters[i]] = i

def encrypt_vigenere(plain, password):
    global letters, inv_letters, n_letters
    cipher = ""
    password_index = 0
    for i in range(len(plain)):
        shift = inv_letters[password[password_index]]
        index = (inv_letters[plain[i]] + shift) % n_letters
        cipher = cipher + letters[index]
        password_index = (password_index + 1) % len(password)
    return cipher

def decrypt_vigenere(cipher, password):
    global letters, inv_letters, n_letters
    plain = ""
    password_index = 0
    for i in range(len(cipher)):
        shift = inv_letters[password[password_index]]
        index = (inv_letters[cipher[i]] - shift) % n_letters
        plain = plain + letters[index]
        password_index = (password_index + 1) % len(password)
    return plain

def encrypt_rectangle(plain, cols):
    cipher = ""
    n_lines = len(plain) // cols + (len(plain) % cols > 0)
    for i in range(cols):
        temp = i
        for _ in range(n_lines):
            cipher += plain[temp] if temp < len(plain) else "*"
            temp += cols
    return cipher

def decrypt_rectangle(cipher, cols):
    plain = ""
    n_lines = len(cipher) // cols + (len(cipher) % cols > 0)
    for i in range(n_lines):
        temp = i
        for _ in range(cols):
            if cipher[temp] != "*":
                plain += cipher[temp] if temp < len(cipher) else ""
            temp += n_lines
    return plain

plain = input("Plain text: ")
password = input("Password: ")
cipher_vignere = encrypt_vigenere(plain, password)
cipher_rectangle = encrypt_rectangle(cipher_vignere, len(password))
print("Cipher: ", cipher_rectangle)
print("cipher vignere = ", cipher_vignere)
plain_rectangle = decrypt_rectangle(cipher_rectangle, len(password))
print("plain rectangle = ", plain_rectangle)
plain_vignere = decrypt_vigenere(plain_rectangle, password)
print("plain: ", plain_vignere)