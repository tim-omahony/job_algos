def is_palindome(string)
  puts string.downcase == string.downcase.reverse
end


def loop_palindrome(string)
  reversed_string = ""
  for i in 1..string.length
    reversed_string += string.downcase[string.length - i]
  end
  if string.downcase == reversed_string
    true
  else
    false
  end
end

puts is_palindome("ABBA"), loop_palindrome("ABBA")
