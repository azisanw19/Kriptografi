"""
vigenere
plain: rajin pangkal pandai
password: baca
          1030
rajin pangkal pandai
10301030103010301030
salio raogmam raodci
"""

letters = "abcdefghijklmnopqrstuvwxyz "
inv_letters = {}
n_letters = len(letters)

for i in range(n_letters):
    inv_letters[letters[i]] = i

def encrypt(plain, password):
    global letters, inv_letters, n_letters
    cipher = ""
    password_index = 0
    for i in range(len(plain)):
        shift = inv_letters[password[password_index]]
        index = (inv_letters[plain[i]] + shift) % n_letters
        cipher = cipher + letters[index]
        password_index = (password_index + 1) % len(password)
    return cipher

def decrypt(cipher,password):
    global letters, inv_letters, n_letters
    plain = ""
    password_index = 0
    for i in range(len(cipher)):
        shift = inv_letters[password[password_index]]
        index = (inv_letters[cipher[i]] - shift) % n_letters
        plain = plain + letters[index]
        password_index = (password_index + 1) % len(password)
    return plain

plain = input("Plain text: ")
password = input("Password: ")
cipher = encrypt(plain,password)
print("Cipher: " + cipher)
plain = decrypt(cipher,password)
print("Plain: "+plain)