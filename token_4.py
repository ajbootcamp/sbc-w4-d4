user = input("Enter word: ")

pref = ["un", "re", "im", "pre", "dis", "mis"]
suf = ["ful", "less", "ness", "ly", "er"]

subwords = []

for i in user.split():
    for j in pref:
        if i.startswith(j):
            suffix = i[len(j):]
            subwords.append(j)
            subwords.append(f"{len(j)* "#"}{suffix}")
            break
    else:
        for k in suf:
            if i.endswith(k):
                prefix = i[:-len(k)]
                subwords.append(f"{prefix}{len(k) * "#"}")
                subwords.append(k)
                break
        else:
            subwords.append(i)        

print(subwords)