"""
abcdefghijklmnopqrstuvwxyz 
012345678911111111112222222
          01234567890123456

"secret" length -> 6
 042561
used 04251
replace angka 6 (length password) dengan yang belum terpakai
hasil permutation vector 042531

rajin pangkal pandai
042531042531042531042531
------++++++------++++++
r jnaipankag....
"""

letters = "abcdefghijklmnopqrstuvwxyz "
invers_letters = {}
n_letters = len(letters)

for i in range(n_letters):
    invers_letters[letters[i]] = i

def permutation_vector(password):
    global invers_letters,n_letters
    cols = len(password)

    permutation = [cols]*cols
    inpw = []
    for i in range(cols):
        n = invers_letters[password[i]] % cols
        if n not in inpw:
            inpw.append(n)
            permutation[i] = n
    spare = []
    for i in range(cols):
        if i not in inpw:
            spare.append(i)
    
    spare_index = 0
    for i in range(cols):
        if permutation[i] == cols:
            permutation[i] = spare[spare_index]
            spare_index +=1

    return permutation

def encrypt(plain,password):
    permutation = permutation_vector(password)
    part_length = len(permutation)
    cipher =""
    parts = len(plain) // part_length
    if len(plain) > (parts * part_length):
        parts += 1

    plain_index = 0
    for i in range(parts):
        partCipher = [" "]*part_length
        for j in range(part_length):
            partCipher[permutation[j]] = plain[plain_index]
            plain_index +=1
            if plain_index == len(plain):
                break
        cipher = cipher + "".join(partCipher)

    return cipher

def decrypt(cipher,password):
    permutation = permutation_vector(password)
    part_length = len(permutation)
    invers_permutation = [0]*part_length

    for i in range(part_length):
        invers_permutation[permutation[i]] = i

    plain =""
    parts = len(cipher) // part_length
    if len(cipher) > (parts * part_length):
        parts += 1

    cipher_index = 0
    for i in range(parts):
        part_plain = [" "]*part_length
        for j in range(part_length):
            part_plain[invers_permutation[j]] = cipher[cipher_index]
            cipher_index +=1
            if cipher_index == len(cipher):
                break
        plain = plain + "".join(part_plain)

    return plain

plain = input("Plain text: ")
password = input("Password: ")

cipher = encrypt(plain,password)
print ("Cipher :" + cipher)
print ("Plain: " + decrypt(cipher,password))