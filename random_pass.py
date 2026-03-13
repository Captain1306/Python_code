import random
import string
rng=string.ascii_letters + string.punctuation + string.digits
pass_len=12
passcode=""
for i in range(pass_len):
    case=random.choice(rng)
    passcode+=case
print("Your Genrated password is : ",passcode)

