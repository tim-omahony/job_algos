# A String is said to be a rotation of another String, 
# if it has the same length, contains the same characters, 
# and they were rotated around one of the characters. 
# For example, String"bcda" is a rotation of "abcd" but "bdca" is not a rotation of String "abcd".
require 'set'

def string_rotation(str1, str2)
  temp = ""
  if str1.length == str2.length
    temp = str1 + str1 # concatting str1 gives a string with the rotation in it => store in temp
    # binding.irb
    if temp.include?(str2) # check temp for string 2  (rotated str1) :)
      true
    end
  else
    false
  end
end

puts string_rotation("abcd","bcda")
