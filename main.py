from stats import get_num_words, get_num_letters, raport_stats
import sys

def get_book_text(path):
    with open(path) as file:
        return file.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #get_num_words(get_book_text("books/frankenstein.txt"))
    #get_num_letters(get_book_text("books/frankenstein.txt"))
    raport_stats(get_book_text(sys.argv[1]))
main()