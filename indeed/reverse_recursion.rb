def reverse(string)
  return string if string.length <= 1

  reversed_str = reverse(string[1..-1])
  reversed_str += string[0]
  reversed_str
end

puts reverse("Hello World!")

# reverse(“water”)
# (reverse(“ater”)) + “w”
# ((reverse(“ter”)) + “a”) + “w”
# (((reverse(“er”)) + “t”) + “a”) + “w”
# ((((reverse(“r”)) + “e”) + “t”) + “a”) + “w”
# ((((“r”) + “e”) + “t”) + “a”) + “w”
# “retaw”