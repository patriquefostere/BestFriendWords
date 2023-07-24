from english_words import get_english_words_set
import string
import json

allWords = get_english_words_set(['web2'], lower = True, alpha = True)
alphabet = list(string.ascii_lowercase)

paths = {}
bfWords = []

def GetTwoLetterWords():
    result = ["da", "la", "on", "am", "hi", "if", "lo", "ai", "ta",  
"re", "ex", "ey", "er", "ok", "my", "oh", "ho", "in", "so",  
"an", "he", "by", "um", "ox", "ra", "do", "us", "gi", "fa", "ay",
 "el", "pi", "jo", "ya", "po", "ne", "mu", "si", "za", "aw", "we", 
 "go", "it", "to", "ah", "en", "fi", "is", "un", "yo", "ax", "mi", "or", 
 "mo", "em", "pa", "ad", "ma", "up", "ha", "ow", "od", "na", "zo", "om", "os", 
 "ye", "sh", "id", "me", "of", "eh", "ut", "at", "as", "ab", "mr", "be", "no", "bo", "aa"]

    # for x in allWords:
    #     if(len(x) == 2):
    #         result.append(x)

    return result

def Main():
    # populate bfWords with two letter words, just to start with 
    twoLetterWords = GetTwoLetterWords()
    # print(twoLetterWords)
    # twoLetterWords = ["lo"]
    InitialPopulate(twoLetterWords) # populate using two letter words to get the three letter best friend words

    next = Iterate(paths)[0]
    next = Iterate(next)[0]
    next = Iterate(next)[0]
    next = Iterate(next)[0]
    next = Iterate(next)[0]
    next = Iterate(next)[0]

    next = Iterate(next)[0]

    next = Iterate(next)[0]
    next = Iterate(next)[0]

    next = Iterate(next)[0]

    next = Iterate(next)[0]

    IterateTimes()

    PrintPaths(next)

def IterateTimes():#todo
    next = Iterate(paths)
    while True:
        anotherNext = Iterate(next[0])
        if not anotherNext[1]: 
            break
        
        next = anotherNext
        print(next)
    
    return next
        
def Iterate(tempPaths):
    
    newTempPaths = GetNextRoundOfWords(tempPaths)
    
    finalPaths = merge_two_dicts(paths, newTempPaths)

    newPathsExist = True
    if(len(tempPaths) != len(finalPaths)):
        print("\r\ntempPaths: ", len(tempPaths))
        print("\r\nfinalPaths: ", len(finalPaths))
    else: 
        print("\r\nno new paths")
        newPathsExist = False

    return finalPaths, newPathsExist

def InitialPopulate(twoLetterWords):
    for twoLetterWord in twoLetterWords:
        
        for letter in alphabet:
            path1 = [twoLetterWord]
            path2 = [twoLetterWord]
            newWord1 = twoLetterWord + letter
            newWord2 = letter + twoLetterWord

            HandleNewWord(newWord1, path1)
            HandleNewWord(newWord2, path2)

def PrintPaths(pathsToPrint):
    for key in pathsToPrint.keys():
        if(len(key) > 6):
            print("key: ", key)
            print("path: ", pathsToPrint[key]) 

def GetNextRoundOfWords(currentPaths):
    tempPaths = {}
    for key in currentPaths.keys():
        for letter in alphabet:
            newWord1 = key + letter
            newWord2 = letter + key

            if(IsWord(newWord1)):
                newPath = currentPaths[key].copy()
                newPath.append(newWord1)
                tempPaths[newWord1] = newPath

            if(IsWord(newWord2)):
                newPath = currentPaths[key].copy()
                newPath.append(newWord2)
                tempPaths[newWord2] = newPath

    return tempPaths

def HandleNewWord(newWord, path):
    if(IsWord(newWord)):
        path.append(newWord)
        paths[path[len(path) - 1]] = path

def IsWord(word):
    if word in allWords:
        # print(word + " is a word")
        return True

    return False

def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

Main()
