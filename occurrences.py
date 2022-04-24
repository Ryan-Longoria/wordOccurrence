file = open("file.txt", "r")
data = file.read()
occurrences = data.count("word")

print('Number of occurences: ', occurrences)