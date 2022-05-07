# Given an array of integers (e.g. [1, 3, 5, 1, 2, 3]) return the first integer that does not occur in this array.
# i.e. in this example, the first integer is 4.

def first_non_occurring_int(arr):
  unique_arr = set(arr)
  for i in range(1, 1000000000000):
    if i not in unique_arr:
      return i


print(first_non_occurring_int([1, 3, 5, 1, 2, 3]))

  