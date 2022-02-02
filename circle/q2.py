# Given an array of integers 'a', your task is to calculate the digits that occur the most number of times in the array. Return the array of these didgets in ascending order. 
# For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2,3,5]

def solution(a):
  count_dict = {}
  output_array = []
  for number in a:
    strings = str(number)
    split_arr = split(strings)
    for element in split_arr:
      if element in count_dict:
        count_dict[element] += 1
      else:
        count_dict[element] = 1
    for key in count_dict:
      if count_dict[key] > 1 and key not in output_array:
        output_array.append(key)
  output_array.sort()
  print(output_array)


def split(string):
  return [char for char in string]


solution([25, 2, 3, 57, 38, 41])