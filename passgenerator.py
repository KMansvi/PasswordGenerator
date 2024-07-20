import string
import random

#input the desired length of the password
length=int(input("Enter the length of the password you want to create: "))

#characters that can be used in the password
chars = string.ascii_letters + string.digits + string.punctuation

#generating the password
password = ''.join(random.choice(chars) for i in range(length))

#displaying the generating password
print("Generated password of mentioned length: ",password)