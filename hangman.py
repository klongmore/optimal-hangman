from string import ascii_lowercase
from wordfreq import word_frequency

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
		guessed_wrong.append(most_occurring_letter)

	if current_word.count('_') == 0:
		gameover = True
		break

	words_alt = []
	master_string = ''

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
				master_string += word

	if len(words_alt) == 1:
		print('I guess: ' + words_alt[0])
		gameover = True
		break

	catch_lowercase = []
	most_frequent_word = ''
	most_frequent_word_freq = 0.0

	if current_word.count('_') == 1:
		for option in words_alt:
			freq = word_frequency(option, 'en', wordlist='best', minimum=0.0)
			if freq > most_frequent_word_freq:
				most_frequent_word_freq = freq
				most_frequent_word = option
		for letter in most_frequent_word:
			if letter not in guessed:
				most_occurring_letter = letter

	most_occurring_letter_count = 0
	most_occurring_letter = ''

	for letter in ascii_lowercase:
		if letter not in current_word and letter not in guessed:
			count = 0
			for character in master_string:
				if letter == character:
					count += 1
			if count > most_occurring_letter_count:
				most_occurring_letter_count = count
				most_occurring_letter = letter
			elif count == most_occurring_letter_count:
				for option in words_alt:
					freq = word_frequency(option, 'en', wordlist='best', minimum=0.0)
					if freq > most_frequent_word_freq:
						most_frequent_word_freq = freq
						most_frequent_word = option
				for letter in most_frequent_word:
					if letter not in guessed:
						most_occurring_letter = letter

	print('I guess: ' + most_occurring_letter)
	guessed.append(most_occurring_letter)

	words = words_alt

print('Game over.')
print('Wrong guesses: ' + str(len(guessed_wrong)))