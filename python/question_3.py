# Given a string s and a positive integer n find the most common substring of length n within string s.
# e.g. given the string "hello hello hello bring bring testing" and the integer 4, the result would give "hell"
# from collections import defaultdict
def most_common_substring(inp, n):
  dictionary = {}
  # dictionary = defaultdict(lambda:0,dictionary)
  i = 0
  max_substring = ""
  max_amount = 0
  n = int(n)
  while i <= len(inp) - n - 1:
    key = inp[i: i + (n)]
    if key in dictionary:
      dictionary[key] += 1
    else:
      dictionary[key] = 1
    if dictionary[key] > max_amount and max_substring != key:
      max_substring = key
      max_amount = dictionary[key]
    i += 1
  return max_substring

print(most_common_substring("hello hello hello testing", 5))