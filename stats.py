def get_num_words(text):
        words = text.split()
        number = len(words)
        return number
def char_number(text):
	let_num = {}
	for letter in text:
		if letter.lower() not in let_num:
			let_num[letter.lower()] = 1
		else:
			 let_num[letter.lower()] += 1
	return let_num
def sort_on(items):
	return items["num"]
def actually_sorts(char_count_dict):
	result_list = []
	for character, count in char_count_dict.items():
		new_dict = {"char": character, "num": count}
		result_list.append(new_dict)
		result_list.sort(reverse=True, key=sort_on)
	return result_list



