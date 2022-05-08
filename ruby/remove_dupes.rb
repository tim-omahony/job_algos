def remove_dupes(string)
  count_hash = Hash.new
  new_string = ""
  string.each_char do |ch|
    if count_hash.key?(ch)
      count_hash[ch] += 1
    else
      count_hash[ch] = 1
    end
    if count_hash[ch] == 1
      new_string += ch
    end
  end
  new_string
end

puts remove_dupes("AABACC")