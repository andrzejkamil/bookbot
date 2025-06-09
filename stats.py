import sys
def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_letters(text):
    new_text = text.lower()
    new_dict = {}
    for c in new_text:
        if c.isalpha():
            if c in new_dict:
                new_dict[c] += 1
            else:
                new_dict[c] = 1
    return(new_dict)

def raport_stats(text):
    
    word_count = get_num_words(text)
    letters = get_num_letters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for letter, count in letters.items():
        print(f"{letter}: {count}")
    print("============= END ===============")