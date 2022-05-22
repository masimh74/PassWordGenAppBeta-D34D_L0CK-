#Password Generator and Passphrase Module.
"""
    includes Exception classes and Contains the following methods:
    def Generate(len)
    def split()
    def GetPhrase()
"""
# import math ### ?
import random
import string


"""Error handling classes to raise value and length errors for Passwords"""
class PassWLengthError(Exception):
    pass
class PassWLengthValueError(PassWLengthError):
    pass

def Generate(leng,specialpool = '!@#$%^&*()_-+?/";:.~`[]{}|'):
    """
        Password Generating method which takes integer value for length of password,
        uses ascii letter pools and special symbols to randomly stitch characters into a string
        returns the random password (string)
    """
    if leng > 20:leng = 20
    letterpool = string.ascii_uppercase+string.ascii_lowercase
    numpool = string.digits
    passw = ""
    random.seed()
    for i in range(0, leng):
        rval = random.randint(0,2)
        if rval == 0:
            char = random.choice(letterpool)
        elif rval == 1 and specialpool:
            char = random.choice(specialpool)
        else:
            char = random.choice(numpool)
        passw+=char
    return passw

def split(words):
    return [char for char in words]

def GetPhrase(pw):
    """
        function to get passphrase for password given password parameter (string)
        creates passphrase string based on letters found in password using dictionary of words
        returns  passphrase (string)
    """

    Wordpool = {'A': 'APPLE', 'B': 'BANANA', 'C': 'COKE',
                'D': 'DON', 'E': 'EAGLE', 'F': 'FREE',
                'G': 'GOAT', 'H': 'HOME', 'I': 'ITALY',
                'J': 'JUMP', 'K': 'KIWI', 'L': 'LAKE',
                'M': 'MAGE', 'N': 'NUKE', 'O': 'OAK',
                'P': 'PARIS', 'Q': 'QUIZ', 'R': 'ROPE',
                'S': 'SHEESH', 'T': 'TURKEY', 'U': 'UGLY',
                'V': 'VISA', 'W': 'WORK', 'X': 'XYLOPHONE',
                'Y': 'YEET', 'Z': 'ZOOM',

                'a': 'anime', 'b': 'book', 'c': 'cool',
                'd': 'deep', 'e': 'east', 'f': 'fork',
                'g': 'game', 'h': 'heart', 'i': 'irish',
                'j': 'jam', 'k': 'kite', 'l': 'lame', 'm': 'magic'
        , 'n': 'nerd', 'o': 'oil', 'p': 'puff', 'q': 'quail'
        , 'r': 'rain', 's': 'soup', 't': 'trash', 'u': 'umbrella'
        , 'v': 'vamp', 'w': 'weirdo', 'x': 'xeno', 'y': 'yeehaw'
        , 'z': 'zoinks'}
    list = split(pw)
    listphrase = []
    fphrase = ""
    for k in list:
        if k in Wordpool.keys():
            listphrase.append(Wordpool.get(k))
        elif k not in Wordpool.keys():
            listphrase.append(k)
    for i in listphrase:
        fphrase += i
        fphrase += ' '
    return fphrase


"""
    How to Utilize Module (import PassGenMod):
    p = PassGenMod.Generate(10) (generates password with given length)
    phrase = PassGenMod.GetPhrase(p) (generates phrase)
    print(p)
    print("passphrase is: ", phrase)
"""


def main():
    print(Generate(12))                         #checked
    print(GetPhrase("password"))

if __name__ == "__main__":
    main()
#End of module
