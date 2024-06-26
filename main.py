
def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	words = file_contents.split()
	counter = 0
	for x in words:
		counter += 1
	print(f"There are a total of {counter} words in this document")

main()

def sort_on(dict_item):
    return dict_item["num"]

# Function to count characters
def character_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    lower_case = file_contents.lower()
    character_dict = {}
    for x in lower_case:
        if x in character_dict:
            character_dict[x] += 1
        else:
            character_dict[x] = 1
    return character_dict

# Get the character counts
character_counts = character_count()

# Convert dictionary to list of dictionaries
character_list = [{'character': char, 'num': count} for char, count in character_counts.items()]

# Sort the list
character_list.sort(reverse=True, key=sort_on)

for char_dict in character_list:
    if char_dict['character'].isalpha():  # Check if it's an alphabetic character
        print(f"The '{char_dict['character']}' character was found {char_dict['num']} times")
