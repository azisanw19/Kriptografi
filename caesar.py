letters = "abcdefghijklmnopqrstuvwxyz "
inv_letters = {}
n_letters = len(letters)

for i in range(n_letters):
    inv_letters[letters[i]] = i

def encrypt(plain, shift):
    global letters, inv_letters, n_letters
    cipher = ""
    for i in range(len(plain)):
        index = (inv_letters[plain[i]] + shift) % n_letters
        cipher += letters[index]
    return cipher

def decrypt(cipher, shift):
    global letters, inv_letters, n_letters
    plain = ""
    for i in range(len(cipher)):
        index = (inv_letters[cipher[i]] - shift) % n_letters
        plain += letters[index]
    return plain

plain = input("Enter plain text: ")
shift = int(input("Shift: "))

cipher = encrypt(plain, shift)
plain = decrypt(cipher, shift)

print("Cipher text: " + cipher)
print("Plain text: " + plain)