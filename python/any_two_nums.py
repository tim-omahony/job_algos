#Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not. Consider this array and the target sums:
# [5, 7, 1, 2, 8, 4, 3]
# Target Sum: 10
# 7+3=10, 2+8=10
# Target Sum: 19
# No 2 values sum up to 19

def find_sum_of_two(A, val):
  found_vals = set()
  for number in A:
      if val - number in found_vals:
          return True
      else: 
        found_vals.add(number)
  return False

print(find_sum_of_two([5, 7, 1, 2, 8, 4, 3], 19))