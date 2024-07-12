 # type: ignore
sentence = input("Enter a String: ")
value = []
tmp = ""

# for i in sentence:
#     if i == " ":
#         value.append(tmp)
#         tmp = ""
#     else:
#         tmp += i
# if tmp:
#     value.append(tmp)

# print(value)

# print(list(sentence))

for i in sentence:
    if i == " , . ? ! /":
        value.append(tmp)
        tmp = ""
    else:
        tmp += i
if tmp:
    value.append(tmp)

print(value)
print(list(sentence))

paragraph = input("Enter a paragraph: ")

punctuation_marks = ['.', '!', '?', ',']


def tokenize_sentences(paragraph):
    sentences = []  
    sentence = "" 
    
    for char in paragraph:  
        sentence += char 
        if char in punctuation_marks:  
            sentences.append(sentence)  
            sentence = ""  
    
    return sentences 

tokenized_sentences = tokenize_sentences(paragraph)

for sentence in tokenized_sentences:
    print(sentence)