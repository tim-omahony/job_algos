def remove_char(string, char)
  removed_string = ""
  string.each_char do |ch|
    # binding.irb
    if ch != char
      removed_string += ch
    end
  end
  removed_string
end

puts remove_char("AABACAACA", "A")
