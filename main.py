import sys
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents
if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
def main():
	return get_book_text(sys.argv[1])
from stats import get_num_words
book_content = main()
word_count = get_num_words(book_content)
from stats import char_number
character_count = char_number(book_content)
from stats import actually_sorts
sorted_list = actually_sorts(character_count)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for item in sorted_list:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")
print("============= END ===============")

