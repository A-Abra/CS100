'''
Anosh Abraham
CS 100 2019 Section 004
HW 05, October 7, 2019
'''

#1
months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
for i in range(len(months)):
    if months[i][0] == 'J':
        print(months[i])

#2
for i in range(100):
    if i%2==0 and i%5==0:
        print(i)

#3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for i in range(len(horton)):
    if horton[i] in vowels:
        print(horton[i], end=" ")
