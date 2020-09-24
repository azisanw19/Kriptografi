"""
    example:
plain: rajin pangkal pandai
rajin
 pang
kal p
andai
cipher: r kaapanjaldin angpi

r ka
apan
jald
in a
ngpi

plain: rajin pangkal pandai
"""

def encrypt(plain, cols):
    cipher = ""
    n_lines = len(plain) // cols
    for i in range(cols):
        temp = i
        for _ in range(n_lines):
            cipher += plain[temp] if temp < len(plain) else " "
            temp += cols
    
    return cipher

def decrypt(cipher, cols):
    plain = ""
    n_lines = len(cipher) // cols
    for i in range(n_lines):
        temp = i
        for _ in range(cols):
            plain += cipher[temp] if temp < len(cipher) else " "
            temp += n_lines

    return plain

plain = input("Plain text: ")
cols = input("Cols: ")
cols = int(cols)

cipher = encrypt(plain, cols)
print ("Ciper: "+ cipher)
plain = decrypt(cipher, cols)
print ("Plain: " + plain)