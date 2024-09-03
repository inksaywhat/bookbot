def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"Word count: {word_count}")

    # Count characters and print the result
    character_counts = count_characters(text)
    print(character_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()  # Convert all characters to lowercase
    char_count = {}

    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


main()
