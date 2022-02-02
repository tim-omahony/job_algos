# You are given an array of integers 'a' and two integers l and r. Your task is to calculate a boolean array 'b', where b[i] = true if there exists an integer 'x', such that a[i] = (i + 1) * x and l <= x <= r. Otherwise, b[i] should be set to false. 
# For a = [8, 5, 6, 16, 5], l = 1, and r = 3, 
# the output should be solution(a, l , r) = [false, false, true, false, true]

def solution(a, l, r):
  boolean_arr = [False] * len(a)
  for i in range(len(a)):
    for x in range(r):
      if l <= x and x <= r: 
        if a[i] == (i + 1) * x: 
          boolean_arr[i] = True 
          
  return boolean_arr

print(solution([8, 5, 6, 16, 5], 1, 3))