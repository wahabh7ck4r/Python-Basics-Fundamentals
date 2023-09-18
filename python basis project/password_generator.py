import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

passwd_len = int(input("Enter your password length:\n"))

s =[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

# random.shuffle(s)
# random.shuffle(s)
print("Your password is : ",end="")
# print("".join(s[0:plen]))
print("".join(random.sample(s, passwd_len)))

