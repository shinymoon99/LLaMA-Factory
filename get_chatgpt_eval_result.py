def count_words_starting_with_n(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word.startswith("n") or word.startswith("N"):
                    count += 1
    return count

# Example usage:
# Suppose you have a file named 'words.txt' containing words separated by lines.
# You can use the function like this:
filename = './output\gpt_judge/result1.txt'
num_words_starting_with_n = count_words_starting_with_n(filename)
print("Number of words starting with 'n':", num_words_starting_with_n)
