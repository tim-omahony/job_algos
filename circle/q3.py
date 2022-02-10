# You are given an array of strings 'arr'. Your task is to construct a string from the words in 'arr', starting with the 0th character from each word (in the order they appear in 'arr'), followed by the 1st character, then the 2nd character, etc. If one of the words doesn't have an ith character, skip that word. 
# For arr = ["Daisy", "Rose", "Hyacinth", "Poppy"], the output should be 
# solution(arr) = "DRHPaoyoisapsecpyiynth"

# def solution(a)
#   0.upto(a.max_by(&:size).size).flat_map {|i| a.map {|elem| elem[i] } }.join
# end

# puts solution(["Daisy", "Rose", "Hyacinth", "Poppy"])

def solution(a):
  final_string = ""
  longest_str = max(a, key=len)
  for word in a:
    char_array = [char for char in word]
    print(char_array)
    for i in range(len(longest_str)):
      
      for i in range(len(char_array)):
        for j in range(len(char_array[0])):
          final_string += char_array[j]
          print(final_string)
  return final_string

def jonny_solution(a):
  words = []
  longest_str = max(a, key=len)
  for i in range(len(longest_str)):
    for word in a:
      print(word[i])
      if i < len(word):
        words.append(word[i])
  return ''.join(words)

print(jonny_solution(["Daisy", "Rose", "Hyacinth", "Poppy"]))