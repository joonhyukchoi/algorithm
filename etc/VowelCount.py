def get_count(sentence):
    count = 0
    for word in sentence:
        if word in "aeiou":
            count += 1
    return count
sentence = "aeiou"
print(get_count(sentence))

for el in sentence:
    print(el)
    if el in "aeiou":
        print('tt')