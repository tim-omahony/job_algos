# def reversed(string)
#   reversed_string = ""
#   for i in 1..string.length
#     reversed_string += string[string.length - i] 
#   end
#   puts reversed_string
# end

# puts reversed("Hello World!")

def reversed_while(string)
  last = string.length - 1
  start = 0
  while start <= last
    temp = string[start]
    string[start] = string[last]
    string[last] = temp
    start += 1
    last -= 1
  end
  string
end

puts reversed_while("Hello World!")