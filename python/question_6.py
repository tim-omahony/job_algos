# Given an input "stream" e.g. ['{', '[', '(', ')', ']', '}']
# Check that the brackets are matched.
# I.e. if '{' is provided, ensure a '}' exists in the correct position.
# Matched: ['{', '[', '(', ')', ']', '}']
# Invalid: ['{', '[', '}', ']']

def matched_brackets(bracket_array):
  seen_elements = []
  for element in bracket_array:    
    if element == '{' or element ==  '[' or element== '(':
      seen_elements.append(element)
    elif element == '}' or element ==  ']' or element== ')':
      last_seen_element = seen_elements[-1]
      if last_seen_element == '{' and element == '}':
        seen_elements.pop()
      elif last_seen_element == '[' and element == ']':
        seen_elements.pop()
      elif last_seen_element == '(' and element == ')':
        seen_elements.pop()
  return len(seen_elements) == 0

print(matched_brackets(['{', '[', '(', ')', ']', '}']))