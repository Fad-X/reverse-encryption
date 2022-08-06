# THIS SCRIPT IS USED TO ENCODE AND DECODE USING THE REVERSE TECHNIQUE
#CODE WRITTEN BY FAD-X
#FEEL FREE TO COPY, MODIFY AND USE
message = input("Type / Paste the data to be ENCRYPTED or DECRYPTED \n")

translated = " "

i = len(message) -1

while i>= 0:
	translated = translated + message[i]
	i = i-1
translated = translated.upper()	
print("The resultimg Data is \n", translated)
