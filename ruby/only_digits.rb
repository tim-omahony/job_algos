def only_digits(string)
  string.scan(/\D/).empty? # returns true if the string only contains digits / is empty
end

puts only_digits("12345678")
puts only_digits("-123")
puts only_digits("A")