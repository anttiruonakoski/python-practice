first_word = input('Anna eka sana ')
second_word = input('Anna toka sana ')

if sorted(list(first_word)) == sorted(list(second_word)):
	print('ovat anagrammeja')
else:
	print('eivät ole anagrammeja')
