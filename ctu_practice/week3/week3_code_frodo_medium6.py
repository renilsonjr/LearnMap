# 6. Read words from the user one per line until they type `done` 
# (a sentinel"stop sign" value that should not be stored). Store the words in a list with `.append()`, 
# then print how many words were entered and print the words in reverse order using `reversed()`.

words = []

word1 = input()

while word1 != "done":
    words.append(word1)
    word1 = input()
print("the amount of words are {}".format(len(words)))
for word in reversed(words):
    print(word)