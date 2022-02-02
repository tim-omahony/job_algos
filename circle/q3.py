# You are given an array of strings 'arr'. Your task is to construct a string from the words in 'arr', starting with the 0th character from each word (in the order they appear in 'arr'), followed by the 1st character, then the 2nd character, etc. If one of the words doesn't have an ith character, skip that word. 
# For arr = ["Daisy", "Rose", "Hyacinth", "Poppy"], the output should be 
# solution(arr) = "DRHPaoyoisapsecpyiynth"


def solution(a):
  final_string = ""
  for word in a:
    char_array = [char for char in word]
    print(char_array)
    for i in range(len(char_array)):
      for j in range(len(char_array[0])):
        final_string += char_array[j]
  return final_string

print(solution(["Daisy", "Rose", "Hyacinth", "Poppy"]))