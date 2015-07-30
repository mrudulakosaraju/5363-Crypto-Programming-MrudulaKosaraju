import argparse
import sys
import randomized_vigenere as rv




symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""

#adding parser arguments
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
parser.add_argument("-s", "--seed", dest="seed",help="Integer seed")

args = parser.parse_args()

#generating a keyword
seed = args.seed
f = open(args.inputFile,'r')
message = f.read()

#encrypting the plaintext
if(args.mode == 'encrypt'):
	data = rv.encryption(message,int(seed),symbols)
	#decrypting the encoded message
else:
	data = rv.decryption(message,int(seed),symbols)

o = open(args.outputFile,'w')
o.write(str(data))
o.close()






