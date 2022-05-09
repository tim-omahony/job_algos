# "Hey there hi hi hello"
# "hi"

# "abba"
# "bba"
# "ba"
# "a"
# abbba
# bbb
# def most_common_sub_string_of_length(string, n)
#   count_hash = Hash.new(0)
#   string.each_char.with_index do |ch, index|
#     key = ""
#     (index..index + (n - 1)).each { |i| 
#       puts i
#       key << string[i] unless i >= string.length }
#     count_hash[key] += 1 unless key.length < n
#     puts count_hash
#   end
#   puts count_hash.max_by{|key, value| value}
# end

# def most_common_sub_string_of_length(string, n)
#   count_hash = Hash.new(0) 
#   index = 0
#   while index <= string.length - n - 1
#     slice = string[index..index + n - 1]
#     count_hash[slice] += 1 
#     index += 1
#     puts count_hash
#   end
#   puts count_hash.max_by{|key, value| value}
# end

def most_common_sub_string_of_length(string, n)
  count_hash = Hash.new(0) 
  index = 0
  max = ""
  max_count = 0
  while index <= string.length - n - 1
    slice = string[index..index + n - 1]
    count_hash[slice] += 1 
    if max_count < count_hash[slice] 
      max = slice
      max_count = count_hash[slice]
    end
    index += 1
  end
  puts max
end


# string = "test hello"
# slice = string[0..2]


# ab = 1
# bb = 1
# ba = 2
most_common_sub_string_of_length("hey there hi hello", 2)