# def binary_search(nums, target)
#   low = 0
#   high = nums.length - 1

#   while low <= high
#     mid = low + ((high - low) / 2).floor

#     if nums[mid] == target
#       mid
#     elsif target < nums[mid]
#       high = mid - 1
#     elsif target > nums[mid]
#       low = mid + 1
#     end
#   end
#   return -1
# end

def binary_search_rec(nums, target, low, high)
  return -1 if low > high

  # Finding the mid
  mid = low + ((high - low) / 2).floor
  
  #Target value is present at the middle of the array
  if nums[mid] == target
    return mid
  
  #Target value is present in the left subarray
  elsif target < nums[mid]
    return binary_search_rec(nums, target, low, mid - 1)
  
  #Target value is present in the right subarray
  else                                   
    return binary_search_rec(nums, target, mid + 1, high)
  end
end

def binary_search(nums, target)
  return binary_search_rec(nums, target, 0, nums.length() - 1)
end

nums_lists = [[], [0,1], [1,2,3], [-1,0,3,5,9,12], [-1,0,3,5,9,12]]
target_list = [12, 1, 3, 9, 2]
nums_lists.length.times do |i|
	nums = nums_lists[i]
	target = target_list[i]
	index = binary_search(nums, target)
	if index != -1
		print target.to_s + " exists in the array and its index is ", index.to_s
	else
		print target.to_s, " does not exist in the array so the return value is ", index.to_s
	end
	print "\n----------------------------------------------------------------------------------------------------\n"
end
