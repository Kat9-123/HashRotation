from hashlib import sha256
from binascii import b2a_base64




# Geneate chararcterset
characterSet = "abcdefghijklmnopqrstuvwxyz"
characterSet += characterSet.upper()
characterSet += "0123456789"
characterSet += ". "
characterSet *= 2

type = False # ENCRYPT
#type = True  # DECRYPT

key = input("Key: ")

print("[E] Encrypt or [D] Decrypt")
ch = input(">").upper()
if ch == "D":
	type = True

print("Enter", "ciphertext" if type else "plaintext")
inputText = input("")

out = ""

keyAddition = ""
loops = -(-len(inputText) // 16) # CEIL
for z in range(loops):
	indexArray = []

	# Generate hash
	hash = sha256((keyAddition + key).encode()).hexdigest()

	# Generate offset based on hash
	for i in range(len(hash)//4):
		indexArray.append(-1)
		for x in range(4):
			indexArray[i] += int(hash[i*4+x], 16) + 1

	# If block mod 16 isnt 0 this part helps
	characters = 16
	if z == loops - 1:
		characters = len(inputText) % 16

	# Rotate
	for i in range(characters):
		#print(i)
		if type:
			indexArray[i] = -indexArray[i]

		out += characterSet[characterSet.find(inputText[i+z*16])+indexArray[i]]
	
	keyAddition = hash	

print("Plaintext:" if type else "Ciphertext:",  out)
input()
