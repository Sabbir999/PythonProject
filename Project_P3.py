import re

def getWordList(filename):
    wordList = []
    with open(filename) as file:
        for line in file.readlines():
            words = re.findall(r'\w+', line)
            wordList.extend(words)
    return wordList

def writeFile(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
        
def getUniqueWords(filename):
    wordList = []
    with open(filename) as file:
        for line in file.readlines():
            line = line.split()
            for word in line:
                if word not in wordList:
                    wordList.append(word)
    return wordList

def getUnionWords(filename1, filename2):
    w1 = getUniqueWords(filename1)
    w2 = getUniqueWords(filename2)
    return list(set(w1 + w2))  # Use set to remove duplicates

def getCommonWords(filename1, filename2):
    commonWords = []
    w1 = getUniqueWords(filename1)
    w2 = getUniqueWords(filename2)
    for word in w1:
        if word in w2:
            commonWords.append(word)
    return commonWords

def notInanotherWord(filename1, filename2):
    wordList = []
    w1 = getWordList(filename1)
    w2 = getWordList(filename2)
    for word1 in w1:
        if word1 not in w2:
            wordList.append(word1)
    return wordList

def displayFile(filename):
    tabString = ''
    words = getWordList(filename)
    wordCounts = {}
    for word in words:
        wordCounts[word] = wordCounts.get(word, 0) + 1

    tabString += f"{'Word':<20}{'Count':<5}\n"
    for word, count in wordCounts.items():
        tabString += f"{word:<20}{count:<5}\n"
    return tabString
        
def main():
    file1 = input("Enter the name of the first input file: ")
    file2 = input("Enter the name of the second input file: ")
    writeString = ''
    unique1 = getUniqueWords(file1)
    unique2 = getUniqueWords(file2)  
    writeString += "Unique words in file 1: " + ' '.join(unique1) + '\n'
    writeString += "Unique words in file 2: " + ' '.join(unique2) + '\n'
    unionList = getUnionWords(file1, file2)
    writeString += "Union of the words in files 1 and 2: " + ' '.join(unionList) + '\n'
    common_words = getCommonWords(file1, file2)
    writeString += "Intersection of the words in files 1 and 2: " + ' '.join(common_words) + '\n'
    inFile1 = notInanotherWord(file1, file2)
    inFile2 = notInanotherWord(file2, file1)
    writeString += "Words in file 1 but not in file 2: " + ' '.join(inFile1) + '\n'
    writeString += "Words in file 2 but not in file 1: " + ' '.join(inFile2) + '\n'
    writeString += "Words in file 1 but not in file 2 and words in file 2 but not in file 1: " + ' '.join(inFile1 + inFile2) + '\n'
    writeString += "Frequency table for file 1:\n" + displayFile(file1) + '\n'
    writeString += "Frequency table for file 2:\n" + displayFile(file2) + '\n'
    outputFile = 'fileAnalysis.txt'
    writeFile(outputFile, writeString)
    print(f"data saved in {outputFile}")

main()
