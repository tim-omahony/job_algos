def anagrams(str1, str2)
  string1_sorted = str1.chars.sort
  string2_sorted = str2.chars.sort
  # _str1 = str1.chars.sort
  # _str2 = str2.chars.sort

  areAnagrams = string1_sorted == string2_sorted

  # areAnagrams = _str1 == _str2
  
  areAnagrams
end

puts anagrams("the", "it")
puts anagrams("angel", "glean")