def max_occurence(string)
  count_hash = Hash.new
  string.each_char do |ch|
    if count_hash.key?(ch)
      count_hash[ch] += 1
    else
      count_hash[ch] = 1
    end
  end
  count_hash.max_by { |key, value| value } # returns max element by key stored in the hash
end

puts max_occurence("AAB")
