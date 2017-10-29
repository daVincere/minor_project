import numpy


a = 17
b = 20

def encryptMessage(message):
	# cipher is a string
	cipher = ""

	for i in message:
		if (message[i]!=''):
			cipher = cipher + char ((((a * (msg[i]-'A') ) + b) % 26) + 'A')
		else:
			cipher += message[i]

	return cipher

def decryptMessage(cipher):
	message = ''
	# cipher is a string
	cipher = ""
	a_inv = 0
	flag = 0

	for i in range[:26]:
		flag = (a*i)%26
		if flag == 1:
			a_inv = i

	for i in len(cipher):
		if cipher[i]=='':
			 message = message + (char) (((a_inv * ((cipher[i]+'A' - b)) % 26)) + 'A')			
		else:
			message+=cipher[1]

	return message


def main():
	message = "Affine Cipher"

	cipherText = str(encryptMessage(message))

	print "Encrypted Message %s" %(cipherText)

	decrypt = decryptMessage(cipherText)
	print "Decrpted Message %s" %(decrypt)

	return 0

if __name__ == "__main__":
	main()

