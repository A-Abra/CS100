'''
Anosh Abraham
CS 100 2019 Section 025a
HW 12
11/30/19
'''

#1
def safeOpen(filename):
    try:
        inF = open(filename, 'r')
        return inF
    except FileNotFoundError:
        return None

#2
def safeFloat(x):
    try:
        return float(x)
    except ValueError:
        return 0.0


def averageSpeed():
    fileN = input('enter file name: ')
    file = safeOpen(fileN)
    if file == None:
        print('File not found. Try again.')
        fileN = input('enter file name: ')
        file = safeOpen(fileN)
        if file == None:
            print('File not found. Another error. Goodbye.')
            exit()

    total = 0
    count = 0
    for line in file:
        for num in line.split():
            val = safeFloat(num)
            if val > 2.0:
                total += val
                count +=1

    avg = total/count
    print('Avg speed is '+avg+' mph.')
                
