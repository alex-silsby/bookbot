
def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    
    letter_counts = count_letter_occurrences(file_contents)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"Number of words: {count_words(file_contents)}")
    print()
    for letter, count in letter_counts.items():
        print(f"The '{letter}' character occurs {count} times")
    print(f"--- End report of {path_to_file} ---")

def count_words(text_string):
    words = text_string.split()
    return len(words)

def count_letter_occurrences(text_string):
    letter_counts = {}
    for letter in text_string:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    sorted_letter_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_letter_counts

main()