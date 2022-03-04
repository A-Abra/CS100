'''
Anosh Abraham
CS 100 2019 Section 025
HW 09
10/31/19
'''

def file_copy(in_file, out_file):
    inF = open(in_file,'r')
    outF = open(out_file,'w')
    for line in inF:
        outF.write(line)
    inF.close()
    outF.close()


def file_stats(in_file):
    lineNum, wordNum, charNum = 0
    inF = open(in_file,'r')
    for line in inF:
        lineNum +=1
        wordList = line.split()
        wordNum += len(wordList)
        for word in wordList:
            charNum += len(word)
    inF.close()


def repeat_words(in_file, out_file):
    inF = open(in_file,'r')
    outF = open(out_file,'w')
    repWords = []
    for line in inF:
        words = line.strip().split()
        for word in words:
            word = word.strip().lower()
            if word not in repWords:
                repWords.append(word)
            else:
                outF.write(word + '')
        if len(repWords) > 0:
            outF.write('\n')
