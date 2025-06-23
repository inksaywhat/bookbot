from stats import count_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_counts = count_characters(text)

    # Print the report
    print_report(book_path, word_count, character_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char.isalpha():  # Only consider alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


def print_report(path, word_count, character_counts):
    # Print the header of the report
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    # Convert the character counts dictionary to a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in character_counts.items()]

    # Define the sort function
    def sort_on(dict):
        return dict["num"]

    # Sort the list by the number of occurrences (most frequent first)
    char_list.sort(reverse=True, key=sort_on)

    # Print each character and its count
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    # Print the footer of the report
    print(f"--- End report ---")


if __name__ == "__main__":
    main()
