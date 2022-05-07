# Given a string - "Hello world", reverse the string. "dlrow olleH"

def reverse(string):
  str2 = ""
  for i in range(len(string)):
    end = string[len(string) - i -1]
    str2 += end
  return str2

print(reverse('Hello world'))