'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

# we want to find the index of the first instance of "th"
  index = word.find('th')
# if we don't find "th", we want to stop running
  if index == -1:
    return 0
# otherwise, after we find the instance, we want to slice the string where the 'th' was found, and we add 2 so that it is removed from the string
  else:
    return 1 + count_th(word[index + 2:])