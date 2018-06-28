#### Are all the characters of a string unique

###Source of problem: Cracking the Coding Interview/Array Section 

###O(n) Worst Case Time

 

### Kieran Thompson  11/06/18

##A fuction to see if there is duplicate 
def IsUnique():
    inputString = input("Please enter some characters: ")

    ##seperate the characters, in the form of a list
    inputString = list(inputString)

    print(inputString)


    present = {}
    ##go through each character in the string adding it to a dictionary,
    ##if it is added twice, return False
    for character in inputString:
        if character in present.keys():
            return False
        else:
            present[character] = 0

    return True

## Run Code
print(IsUnique)

###Possible Alternatives:
###Could convert to ASCII/ Unicode, then sort it
###check to see if any two, consecutive characters are the same
###Time complexity would be the same as the sorting algorithm used 
