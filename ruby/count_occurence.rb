def count_occurence(string, char)
  count_hash = Hash.new
  string.each_char do |ch|
    if count_hash.key?(ch)
      count_hash[ch] += 1
    else
      count_hash[ch] = 1
    end
  end
  count_hash[char]
end

puts count_occurence("ABCDEFGA", "A")