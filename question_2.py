# Given a list of words, group words that are anagrams of one another
# ['cat', 'pat', 'won', 'god', 'now', 'apt', 'dog'] --> ['cat', 'pat', 'apt', 'won', 'now', 'god', 'dog']
from itertools import chain
def group_anagrams(words):
  data = {}
  for k in words:
    print(k)
    key = ''.join(sorted(k))
    if key in data:
      data[key].append(k)
    else: 
      data[key] = [k]

  print(flat_list(data))

def flat_list(dictionary):
  new_list = []
  for word_bucket in dictionary.values():
    for word in word_bucket:
      new_list.append(word)
  return new_list


def flatten_dict_values(dictionary):
    return list(chain(*dictionary.values()))

group_anagrams(['cat', 'pat', 'won', 'god', 'now', 'apt', 'dog'])
