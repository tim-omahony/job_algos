
# You have an empty sequence, and you will be given queries. Each query is one of these three types:
# 1 X     Push the element X into the list.
# 2        Delete the element present at the top of the list.
# 3        Print the maximum element in the list.

# Input Format

# The first line of input contains an integer. The next lines each contain an above mentioned query. (It is guaranteed that each query is valid.)

# Output Format

# When matching query type 3, Print the maximum element in the list on a new line.

# Sample Input

# 10
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 2
# 3
# 1 91
# 3
# Sample Output

# 26
# 91

# queries = int(input())  # sets the number of queries


# class Stack:
#     def __init__(self):
#         # initialises the stack using None to indicate no value and -float('inf') so that the first element which is added is the max
#         self.stack = [(float('inf'), -float('inf'))]

#     def push(self, x):
#         return self.stack.append(x)

#     def pop(self):
#         # removes the top element
#         self.stack.pop()
#         return

#     def max(self):
#         # returns the max element in the stack
#         return self.stack[-1][1]


# new_stack = Stack()

# for i in range(queries):
#     # creates a new list 'array'. map casts each input to an int within the list and splits them on spaces so that each element can be extracted individually.
#     array = list(map(int, input().split()))
#     # if the 0th element (the query) is 1, the 1st element (the number) is pushed into the stack
#     if array[0] == 1:
#         new_stack.push(array[1])
#     elif array[0] == 2:  # if the 0th element is 2, the stack is popped, removing the top element
#         new_stack.pop()
#     else:  # otherwise, the max element is printed
#         print(new_stack.max())


# ^ see above for my terrible overcomplication of this solution (it also didn't work)

num_queries = int(input())

stack = []  # initialise an empty list

for i in range(num_queries):
    # takes the inputs, splits them on spaces and casts them to ints in a list
    commands = list(map(int, input().split()))

    if commands[0] == 1:  # if the first element is 1, the second element is pushed into the stack
        stack.append(commands[1])
    elif commands[0] == 2:  # if the first element is 2, the top element is popped
        stack.pop()
    else:  # otherwise the max element is printed
        print(max(stack))
