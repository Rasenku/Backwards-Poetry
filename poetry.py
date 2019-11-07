import random

def reverse(s):
    s.reverse()
    index = len(s)
    for line in s:
        print(f"{index} {line}")
        index -= 1

s = '''A winter blanket
Covers the Earth in respose
but only a dream''' .split("\n")
reverse(s)

def lines_printed_random(s):

    lines = []

    for i in range(0, len(s)):
        index = random.randint(0, len(s) - 1)
        lines.append(s[index])

    print("\n".join(lines))
