def duplicates(string)
  count_hash = Hash.new
  dup_string = ""
  string.each_char do |ch| 
    if !count_hash.key?(ch)
      count_hash[ch] = 1
    else
      count_hash[ch] += 1
    end
    # binding.irb
    if count_hash[ch] > 1
      dup_string += ch unless dup_string.include?(ch)
    end
  end
  dup_string
end

puts duplicates("this is a test")
