"""
Anosh Abraham
CS 100 2019 Section 025
HW 06, October 8, 2019
"""

#1a,b
def hasFinalLetter(strList, letters):
    newList = []

    for string in strList:
        if string[-1] in letters:
            newList.append(string)
    return newList


strList = ["Hello worlD", "hotline", "Hoody"]
letters = "yD"
print(hasFinalLetter(strList, letters))

strList = ["Hello", "compscionehundred", "how"]
letters = "yD"
print(hasFinalLetter(strList, letters))

strList = ["artificial", "libra", "BaYe"]
letters = "aY"
print(hasFinalLetter(strList, letters))


#2a,b
def isDivisible(maxInt, twoInts):
    divList = []
    for i in range(0,maxInt):
        if i%twoInts[0]==0 and i%twoInts[1]==0:
            divList.append(i)
    return divList


twoNums = (10,7)
maxNum = 0
print(isDivisible(maxNum,twoNums))

twoNums = (2,1)
maxNum = 32
print(isDivisible(maxNum,twoNums))

twoNums = (-10,-2)
maxNum = 20
print(isDivisible(maxNum,twoNums))
