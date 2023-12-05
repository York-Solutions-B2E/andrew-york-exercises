import string 
stopWords = ["as", "the", "is", "at", "which", "a", "of", "to"]

def text_analyzer(str):
    wordList = str.split()
    # Remove stopWords
    filteredWordList = []
    for word in wordList:
        if word not in stopWords:
            filteredWordList.append(word)
    # Count number of words
    wordCount = len(filteredWordList)
    # Identify longest word
    longest = filteredWordList[0]
    for x in filteredWordList:
        if len(x) > len(longest):
            longest = x
    # Standardize words: all lowercase, remove punctuation
    def remove_punctuation(inputString):
        toRemove = str.maketrans("", "", string.punctuation)
        newString = inputString.translate(toRemove)
        return newString
    standardWordList = []
    for x in filteredWordList:
        word = remove_punctuation(x.lower())
        standardWordList.append(word)
    # Count occurrences of each unique word
    wordSet = dict()
    for word in standardWordList:
        if word in wordSet:
            wordSet[word] += 1
        else:
            wordSet[word] = 1

    return wordCount, longest, wordSet, standardWordList, wordList

string1 = "Many are the strange chances of the world, and help oft shall come from the hands of the weak when the Wise falter."

output = text_analyzer(string1)
wordCount = output[0]
longest = output[1]
wordSet = output[2]

# print(output[4])
# print(output[3])

print("Word count: ", wordCount)
print("Longest word: ", longest)
print("Unique word occurrence: ", wordSet)

# Note on punctuation removal:
    # using a string method called maketrans which lets you replace characters according to your own specification
    # arg 1: characters you want to replace
    # arg 2: characters you want to replace them with
    # arg 3: characters you want to remove