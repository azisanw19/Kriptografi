'''
    data: angkasa biru pagi yang indah

    f = ((sigma(data)%256)^len(data))%256

    blocksize: 16
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
     a, n, g, k, a, s, a,  , b, i, r, u,  , p, a, g
     f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f
     i,  , y, a, n, g,  , i, n, d, a, h
     f, f, f, f, f, f, f, f, f, f, f, f
    ------------------------------------------------- xor
    [104, 33, 120, 96, 111, 102, 33, 104, 111, 101, 96, 105, 96, 111, 102, 106]

    convert to ascii (alphabet + numeric)
    682178606f6621686f656069606f666a
'''

def myhash(data):
    hashsize = 16
    digest = [0]*hashsize
    data_index = 0
    end = False
    count = 0
    for char in data:
        count += ord(char)
    change =((count%256)**len(data))%256
    for i in range(hashsize):
        while data_index < len(data) and not end:
            for i in range(hashsize):
                if data_index == len(data):
                    data_index = 0
                    end = True
                digest[i] = (((digest[i])**change)%256)^ord(data[data_index])^change
                data_index += 1
        return digest
    
data = input("Data: ")
h = (myhash(data))

for i in range(len(h)):
    print('{:02x}'.format(h[i]),end='')
print()