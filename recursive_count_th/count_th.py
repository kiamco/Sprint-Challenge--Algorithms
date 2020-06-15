'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

occurance = 0
def count_th(word, occurance = 0):
    # create 2 pointers
    pointer1 = len(word) - 1
    pointer2 = pointer1 - 1
    
    # check word length
    if len(word) <= 1:
        return occurance
    
    # check match
    if word[pointer1] == 'h' and word[pointer2] == 't':
        return count_th(word[:len(word) - 1], occurance + 1)
    else:
        # move pointers
        pointer2 -= 1
        pointer1 -= 1
        return count_th(word[:len(word) -1], occurance)
            
    
    
    
