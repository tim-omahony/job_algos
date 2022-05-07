def vowels_cons(string)
  vowel_count = 0
  cons_count = 0
  string.downcase.each_char do |ch|
    if ch == "a" || ch == "e" || ch == "i" || ch == "o" || ch == "u"
      vowel_count += 1
    else
      cons_count += 1
    end
  end
  puts vowel_count, cons_count
end

puts vowels_cons("AbCD")