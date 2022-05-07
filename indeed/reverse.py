def reverse(string):
    return string[::-1]


print(reverse("Hello World!"))


def reverse_while(string):
    start = string[0]
    end = string[-1]
    print(start, end)


print(reverse_while("Hello World!"))
