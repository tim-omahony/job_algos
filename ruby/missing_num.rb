require 'set'

def missing_num(array)
  set = array.to_set
  return nil if set.empty?
  (1...100000).each { |i| return i unless !set.include?(i) }
end

array = (1...1000000).to_a.sort{ rand() - 0.5 }[1...100000] 

puts missing_num(array)

