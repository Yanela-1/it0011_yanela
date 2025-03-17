def sort_key(word):
  return (word[0].isupper(), word.lower())

user_input = input("Enter a string statement: ")
input_list = user_input.split()
print(input_list)
nonowords = ["and", "but", "or", "of", "nor", "for", "so", "yet", "a", "an", "the"]
word_dict = {}

for word in input_list:
  if word.lower() in nonowords:
    continue
  elif word in word_dict:
    word_dict[word] += 1
  else:
    word_dict[word] = 1

for word in sorted(word_dict.keys(), key=sort_key):
  print(f"{word} - {word_dict[word]}")

total_count = sum(word_dict.values())
print(f"Total words filtered: {total_count}")