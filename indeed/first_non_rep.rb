def first_non_rep(string)
  low_string = string.downcase
  low_string.chars.find { |character| low_string.count(character) == 1 }
end

puts first_non_rep("AABaBCCDDxG")