# Given a list of words, group words that are anagrams of one another
# ['cat', 'pat', 'won', 'god', 'now', 'apt', 'dog'] --> ['cat', 'pat', 'apt', 'won', 'now', 'god', 'dog']

require 'pry'
def group_anagrams(array)
  hash = Hash.new { |hash, k| hash[k] = [] } # create an empty hash of arrays
  array.each do |word|
    binding.pry
    key = word.chars.sort.join 
    hash[key].push(word)
  end
  hash.values.flatten
end

puts group_anagrams(['cat', 'pat', 'won', 'god', 'now', 'apt', 'dog'])


# ↓ jon explanation 
# so
# cat, act, tab, bat

# cat becomes act
# {act => [cat]}
# act becomes act
# {act => [cat, act]}
# tab becomes abt
# {act => [cat, act], abt => [tab]}
# bat becomes abt
# {act => [cat, act], abt => [tab, bat]}
