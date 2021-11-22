# 1
s = input()
print(len(s))
# 2
t = ""
if len(s) < 2:
    print()
else:
    for i in range(0, 2):
        t += s[i]
    for i in range(len(s)-2, len(s)):
        t += s[i]
    print(t)
# 3
t = s[1:]
ch = s[0]
print(t.find(ch))
while t.find(ch) > -1:
    t = t.replace(ch, "$")
print(ch+t)
# 4

if len(s) % 4 == 0:
    t = ""
    for i in range(len(s)-1, -1, -1):
        t += s[i]
    print(t)
else:
    print("length is not a multiple of 4")
# 5
s = input("Input sequence of words using ', ': ")
words_set = s.split(", ")
words_set = set(words_set)
words_set = list(words_set)
words_set.sort()
print(words_set)
