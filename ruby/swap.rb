def swap(num1, num2)
  num1 = num1 + num2
  num2 = num1 - num2
  num1 = num1 - num2
  puts num1, num2
end

swap(1,2) 