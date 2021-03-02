# Made by: Kat9_123
# This is a simple encryption algorithm that is based on the caesar cipher
# it has some randomly generated "salt" at the beginning of the message
# to try to circumvent a KPA
from hashlib import sha256
from binascii import b2a_base64
from os import urandom
import base64



# Geneate chararcterset
characterSet = "abcdefghijklmnopqrstuvwxyz"
characterSet += characterSet.upper()
characterSet += "0123456789"
characterSet += "/+"
characterSet *= 8

type = False # ENCRYPT
#type = True  # DECRYPT





# Get user input
key = input("Key: ")

print("Enter text")
inputText = input("").replace(".", "/").replace(" ", "+")


print("[E]ncrypt or [D]ecrypt")
ch = input(">").upper()

out = ""

# Handle decryption AND "salt" to try to circumvent a KPA
if ch == "D":
	type = True
	salt = inputText.split("=")[0] + "="
	inputText = inputText.split("=")[1]
else:
	salt = base64.b64encode(urandom(32)).decode()
	out = extra

key = salt + key





keyAddition = ""
loops = -(-len(inputText) // 32) # CEIL

# Loop through 32 character blocks
for z in range(loops):
	indexArray = []

	# Generate hash
	hash = sha256((keyAddition + key).encode()).hexdigest()

	# Generate 32 offsets based on hash
	for i in range(len(hash)//2):
		indexArray.append(int(hash[(i*2):(i*2+2)], 16))

	# Last block
	characters = 32
	if z == loops - 1:
		characters = len(inputText) % 32

	# Rotate
	for i in range(characters):
		if type:
			indexArray[i] = -indexArray[i]

		char = inputText[i+z*32]
		index = characterSet.find(char)
		out += characterSet[index+indexArray[i]]
	
	keyAddition = hash	

print(("Plaintext: " + out.replace("+"," ").replace("/",".")) if type else ("Ciphertext: " + out))
input()
