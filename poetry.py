poem = '''A winter blanket
Covers the Earth in respose
but only a dream'''


#TODO: get a list of strings that contains lines of poem

#Use lines = poem.split("\n")
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


#Testingcode
#lines_printed_backwards(lines)
