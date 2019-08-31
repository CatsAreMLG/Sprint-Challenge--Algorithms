'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
    # check if length is 0 if so return the count
    if len(word) == 0:
        return count
    else:
        # check if first two of index is th if so add to count
        if word[:2] == 'th':
            count += 1
        # return the count_th passing in the word minus the first letter and the count
        return count_th(word[1:], count)
