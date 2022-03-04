'''
Anosh Abraham
CS 100 2019 Section 025
HW 10
11/4/19
'''

#1
def initialLetterCount(wordList):
    d = {}
    for word in wordList:
        if word[0] not in d:
            d[word[0]]=1
        else:
            d[word[0]]+=1
    return d

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))

#2
def initialLetters(wordList):
    d = {}
    for word in wordList:
        if word[0] not in d:
            d[word[0]]=[word]
    return d

print(initialLetters(horton))

#3
def shareALetter(wordList):
    d = {}
    for word in wordList:
        if word not in d:
            l = []
            for char in word:
                for other in wordList:
                    if char in other:
                        if other not in l:
                            l.append(other)
            d[word] = l
    return d

print(shareALetter(horton))
