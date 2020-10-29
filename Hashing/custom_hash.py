'''
    data: angkasa biru pagi yang indah
    blocksize: 16
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
     a, n, g, k, a, s, a,  , b, i, r, u,  , p, a, g
     i,  , y, a, n, g,  , i, n, d, a, h
    ------------------------------------------------- xor
    [8, 78, 30, 10, 15, 20, 65, 73, 12, 13, 19, 29, 65, 30, 6, 12]

    convert to ascii (alphabet + numeric)
    084e1e0a0f1441490c0d131d411e060c


'''

def myhash(data):
    blocksize = 16
    digest = [0]*blocksize
    
    data_index = 0
    end = False
    for i in range(blocksize):
        while data_index < len(data) and not end:
            for i in range(blocksize):
                if data_index == len(data):
                    data_index = 0
                    end = True
                digest[i] = digest[i]^ord(data[data_index])
                data_index += 1
        return digest
    
data = input("Data: ")
h = (myhash(data))

for i in range(len(h)):
    print('{:02x}'.format(h[i]),end='')
print()
