###Check strings if all characters have the same frequency, or if one character
###is removed, all the characters have the same frequency 


###Source of problem:  Hacker Rank

###O(n) Worst Case Time



###Kieran Thompson  23/04/18

def validString(text):

    charFrequencies = {}
    frequencyOfFrequencies = {}    

    ##loop through text by characters
    for char in text:

        ##count the frequencies of the characters,
        ##using the dictionary "charFrequencies"
        if char not in charFrequencies.keys():
            charFrequencies[char] = 1
        else:
            charFrequencies[char] = charFrequencies[char] + 1
    

            
    ##loop the frequecnies of each character and store the different
    ##numbers 
    for char in charFrequencies:
        value = charFrequencies[char]
        if charFrequencies[char] not in frequencyOfFrequencies.keys():
            frequencyOfFrequencies[value] = 1
        else:
            frequencyOfFrequencies[value] = frequencyOfFrequencies[value] + 1
    

    ##if there is only one frequency, its valid
    ##Or if there is one other frequency, that is 1 and it happens one time
    ##Or its invalid
    if len(frequencyOfFrequencies) == 1:
        return True
    elif len(frequencyOfFrequencies) == 2 and 1 in frequencyOfFrequencies.keys():
        if frequencyOfFrequencies[1] == 1:
            return True
        else:
            return False
    else:
        return False



## Run Code

print(validString("aabbcd"))  ### False
print(validString("aaccaa"))  ### False
print(validString("aaba"))    ### True
print(validString("aaa"))     ### True

