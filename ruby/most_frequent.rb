def most_frequent(array)
  array.max_by { |i| array.count(i) }
end

puts most_frequent(["dog", "dog","dog","dog","cat", "cat", "cat", "cat"])