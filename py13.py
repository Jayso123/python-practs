def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)

filename = "python.txt"
word_count = count_words_in_file(filename)
print(f"Word count: {word_count}")
