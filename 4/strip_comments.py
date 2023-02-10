"""
Complete the solution so that it strips all text 
that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out.
Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
"""
def strip_comments(strng, markers):
    words = strng.split("\n")
    result = []
    for word in words:
        if not word.isalpha():
            for i in range(len(word)):
                if word[i] in markers:
                    if len(word[:i]) > 1:
                        result.append(word[:i].rstrip())
                    else:
                        pass
        else:
            result.append(word)
        
    
    return "\n".join(result)
                
#'a\nc\nd' 
print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))

