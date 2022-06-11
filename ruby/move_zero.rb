# We’re given an integer array, nums. 
# Move all zeroes if any to the left while maintaining the order of other elements in the array.
# Sample input
# [1, 10, 20, 0, 59, 63, 0, 88, 0]
# Expected output
# [0, 0, 0, 1, 10, 20, 59, 63, 88]

def move_zeroes(nums)
  # Write your code here.
  i = 0
  j = 0
  while i < nums.length
    if nums[i] != 0
      nums[j] = nums[i]
      j += 1
    end
    i += 1
  end
  while j < nums.length
    nums[j] = 0
    j += 1
  end
  nums.to_a
end

puts move_zeroes([1, 10, 20, 0, 59, 63, 0, 88, 0])