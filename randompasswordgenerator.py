import random
import string
pass_len=int(input("enter your choice for size of password"))
charvalues = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(charvalues)for i in range(pass_len))
print("your random password is: ",password)