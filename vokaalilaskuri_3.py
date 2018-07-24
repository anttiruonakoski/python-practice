vowels = 'aeiouyåäö'

word = list(filter(str.isalpha, str.lower(input('Anna sana '))))
vowel_count = sum(map(lambda k: k in vowels, word))

print ('Sanassa on {} vokaalia ja {} konsonanttia.'.format(vowel_count, len(word) - vowel_count))
