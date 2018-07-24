
from random import shuffle

last_number = int(input('Anna suurin luku: '))
sort_order = int(input('Anna järjestys: \n1 nouseva \n2 laskeva \n3 satunnainen '))

number_list = list(range(1, last_number + 1))

if sort_order == 1:
	pass
elif sort_order == 2:
	number_list.reverse()
elif sort_order == 3:
	shuffle(number_list)

print(' + '.join(map(str, number_list)), '=', sum(number_list))
