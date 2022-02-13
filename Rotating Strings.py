import string

good = "nopqrstuvwxyzABCDEFGHIJKLM9012345678"
text = "abcdefghijklmNOPQRSTUVWXYZ0123456789"
rotationFactor = 39

rslt = ""

alphaLowercaseIndex = list(string.ascii_lowercase)
alphaUppercaseIndex = list(string.ascii_uppercase)

for char in text:
	if char.isalpha():
		if char.isupper():
			orgIndex = alphaUppercaseIndex.index(char)
			rotatedIndex = (orgIndex + rotationFactor) % len(alphaUppercaseIndex)
			rotatedChar = alphaUppercaseIndex[rotatedIndex]
		elif char.islower():
			orgIndex = alphaLowercaseIndex.index(char)
			rotatedIndex = (orgIndex + rotationFactor) % len(alphaUppercaseIndex)
			rotatedChar = alphaLowercaseIndex[rotatedIndex]
		rotatedIndex = orgIndex + rotationFactor
	elif char.isnumeric():
		rotatedChar = (int(char) + rotationFactor) % 10
	else:
		rotatedChar = char
	rslt += str(rotatedChar)

print("Rotated text: ", rslt)
print("***Good text: ", good)
print(good == rslt)