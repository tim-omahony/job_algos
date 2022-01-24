# Given a string s and a positive integer n find the most common substring of length n within string s.
# e.g. given the string "hello hello hello bring bring testing" and the integer 4, the result would give "hell"

def most_common_substring(inp, n):
  dictionary = {}
  i = 0
  max_substring = ""
  max_amount = 0
  n = int(n)
  while i <= len(inp) - n - 1:
    for i in range (inp[i + n -1]):
      key = i
      dictionary[key] += 1
      if dictionary[key] > max_amount and max_substring != key:
        max_substring = key
        max_amount = dictionary[key]
      i += 1
  return max_substring

print(most_common_substring("hello hello hello bring bring testing", 4))