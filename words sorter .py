

string1 = input("Enter the words : ")

words = string1
words = string1.split(" ")
for i in range(len(words)):
    words[i] = words[i].lower()
string1 = sorted(words)
print(' '.join(string1))
