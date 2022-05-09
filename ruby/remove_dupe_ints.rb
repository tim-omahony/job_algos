require 'set'

def remove_dupes_set(array)
  set = Set.new
  array.each {|num| set << num}
  set.sort.to_a.join
end

puts remove_dupes_set([1,1,2,3,5,6,3,4,2])