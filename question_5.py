# Given an array of integers e.g. [1, 3, 4, 4, 5, 5]
# Return the most common integer

def most_common_int(arr):
  count_dict = {}
  for element in arr:
    if element in count_dict:
      count_dict[element] += 1
    else:
      count_dict[element] = 1
  # print(count_dict)
  return biggest_int(count_dict)

def biggest_int(dictionary):
  max_num = 0
  key_max = 0
  for key in dictionary: 
    if dictionary[key] > max_num:
      max_num = dictionary[key]
      key_max = key
  return key_max
      
print(most_common_int([1, 3, 4, 4, 4, 5, 5, 5, 5]))