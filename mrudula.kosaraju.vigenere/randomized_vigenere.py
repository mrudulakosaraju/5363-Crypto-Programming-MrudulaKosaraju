
import random
symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
encryptedData = []
decryptedData = []
matrixcheck = []
n = len(symbols)
i=0
# key word generation
def keywordFromSeed(seed):
    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 1000) % 95 + 32))
        seed = seed // 1000
    return ''.join(Letters)
 

# bulding 95X95 matrix with symbols 
def buildVigenere(symbols,seed):
    random.seed(seed)
    n = len(symbols)
    vigenere = [[0 for i in range(n)] for i in range(n)]
    symbols = list(symbols)
    random.shuffle(symbols)
    symbols = ''.join(symbols)
    for sym in symbols:
        random.seed(seed)
        myList = []
    
        for i in range(n):
            r = random.randrange(n)
            
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(n)
                myList.append(r)
                               
            while(vigenere[i][r] != 0):
                r = (r + 1) % n
            
            vigenere[i][r] = sym
            
    return vigenere
    
def matrixletter(vigenerematrix,n):
    matr1 = [vigenerematrix[i][0] for i in range(n)] 
    return matr1

 # this function is to encrypt the plain text
def encryption(message,key,symbols):
    i=0
    matrixcheck=[]
    realkey = keywordFromSeed(key)
    vigenerematrix = buildVigenere(symbols,key)
    matrixcheck = matrixletter(vigenerematrix,n)# checking column wise [vigenerematrix[i][0] for i in range(n)] 
    while i < len(message):
        encryptedData.append(vigenerematrix[matrixcheck.index(realkey[i%len(realkey)])][vigenerematrix[0].index(message[i])])
        i = i + 1
    return ''.join(encryptedData)
    print(encryptedData)

# this function to decrypt the cipher text
def decryption(message,key,symbols):
    i=0
    matrixcheck=[]
    realkey = keywordFromSeed(key)
    vigenerematrix = buildVigenere(symbols,key)
    matrixcheck = matrixletter(vigenerematrix,n)
    while i < len(message):
        decryptedData.append(vigenerematrix[0][vigenerematrix[matrixcheck.index(realkey[i%len(realkey)])].index(message[i])])
        i = i + 1
    return ''.join(decryptedData)
    Print(decryptedData)


if __name__=='__main__':
    pass