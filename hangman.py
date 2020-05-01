from string import ascii_lowercase
from wordfreq import zipf_frequency, word_frequency
import sys

dec_mode = False

if len(sys.argv) == 2:
	if sys.argv[1] == '-d':
		dec_mode = True

with open('words.txt', 'r') as f:
	words = f.read().split()

gameover = False
guessed = []
guessed_wrong = []
current_word = ''

while True:
	old_word = current_word

	current_word = input('Please enter your word (underscores for blank spaces): ')
	current_word_length = len(current_word)

	if current_word == old_word:
		guessed_wrong.append(most_likely_letter)

	if current_word.count('_') == 0:
		gameover = True
		break

	words_alt = []

	for word in words:
		if len(word) == current_word_length:
			for x in range(current_word_length):
				if (current_word[x] == word[x] or current_word[x] == '_') and current_word[x] not in guessed_wrong:
					possible = True
				else:
					possible = False
					break
			if possible:
				words_alt.append(word)

	if len(words_alt) == 1:
		print('I guess: ' + words_alt[0])
		gameover = True
		break

	option_dicts = []

	for option in words_alt:
		if dec_mode:
			freq = round(word_frequency(option, 'en', wordlist='best', minimum=0.0) + 0.0000001, 7)
		else:
			freq = zipf_frequency(option, 'en', wordlist='best', minimum=0.0) + 1	
		option_dict = dict(word=option, freq=freq)
		option_dicts.append(option_dict)

	letter_dicts = []

	for letter in ascii_lowercase:
		letter_dict = dict(letter=letter, score=0)
		letter_dicts.append(letter_dict)

	for option_dict in option_dicts:
		for letter in option_dict["word"]:
			next(item for item in letter_dicts if item["letter"] == letter)["score"] += option_dict["freq"]

	option_dicts = sorted(option_dicts, key=lambda o: o['freq'], reverse=True)
	letter_dicts = sorted(letter_dicts, key=lambda l: l['score'], reverse=True)

	most_likely_letter = ''

	for letter in letter_dicts:
		if letter["letter"] not in guessed:
			most_likely_letter = letter["letter"]
			break

	print('I guess: ' + most_likely_letter)
	guessed.append(most_likely_letter)

	words = words_alt

print('Game over.')
print('Wrong guesses: ' + str(len(guessed_wrong)))