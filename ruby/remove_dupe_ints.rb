require 'set'

def remove_dupes_set(array)
  set = Set.new
  array.each {|num| set << num}
  set.sort.to_a.join
end

puts remove_dupes_set([1,1,2,3,5,6,3,4,2])

def remove_no_lib(array)
  removed_arr = []
  count_hash = Hash.new
  array.each do |num|
    if count_hash.key?(num)
      count_hash[num] += 1
    else
      count_hash[num] = 1
    end
    if count_hash[num] == 1
      removed_arr << num
    end
  end
  removed_arr.join
end

puts remove_no_lib([1,1,2,3,5,6,3,4,2])