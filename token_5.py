characters = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

words =input("Enter a word: ")

value = []
tmps = []
tmp = ""

for i in words:
    if i in characters:
        if tmp:
            value.append(tmp.strip())
            tmps.append(tmp.strip() + i)
            tmp = ""
        else:
            if tmps:
                tmps[-1] += i
    else:
        tmp += i
if tmp:
    value.append(tmp.strip())
    tmps.append(tmp.strip())

print(tmps)
print(value)