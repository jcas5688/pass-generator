import random
from string import digits, punctuation, ascii_letters 

def passgen():
    lenght = 20
    symbols= ascii_letters + digits + punctuation
    secure= random.SystemRandom()
    passw= "".join(secure.choice(symbols)
                    for i in range(lenght))

    print (passw)


passgen()