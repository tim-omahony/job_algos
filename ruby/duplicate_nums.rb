def dupe_nums(array)
  count_hash = Hash.new
  dup_array = []
  array.each do |num|
    if count_hash[num]
      count_hash[num] += 1
    else
      count_hash[num] = 1
    end
    if count_hash[num] > 1
      dup_array << num unless dup_array.include?(num)
    end
  end
  dup_array
end

puts dupe_nums([1,1,2,3,5,6,3,4,2])