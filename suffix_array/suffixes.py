from suffix_array import suffix_array

s = input()
s += '$'
p, c = suffix_array(s)

for x in p:
    print(s[x:])
