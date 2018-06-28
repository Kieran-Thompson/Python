###Flatten any level of nested list 


###Kieran Thompson  23/3/18


def flattenList(s):
    if len(s) == 0:
        return []   ##base case is the lsit is empty 
    if type(s[0]) == list:          
        element = flattenList(s[0])  ### if the fist item is a list, flatten that list
    else:
        element = [s[0]]            ### or the item is not a list 
    return element + flattenList(s[1:])     ###add the first element to the rest of the list
                                            ###which has to be flattened





## Run Code
s = [1,2,3,4,[5,6]]

print(flattenList(s))  ###result is [1,2,3,4,5,6]

