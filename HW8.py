'''
Anosh Abraham
CS 100 2019 Section 025
HW 08
10/25/19
'''

def twoWords(length, firstLet):
    twoList = []
    
    while True:
        wordOne = input('Enter a '+str(length)+'-letter word: ')
        if len(wordOne) == length:
            break
    while True:
        wordTwo = input('Enter a word beginning with '+firstLet+': ')
        if (wordTwo[0] == firstLet.upper()) or (wordTwo[0] == firstLet.lower()):
            break
    twoList.append(wordOne)
    twoList.append(wordTwo)
    return twoList

print(twoWords(4, 'B'))


def enterNewPassword():
    while True:
        
