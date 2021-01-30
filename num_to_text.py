names = ['', ' hundred ', ' thousand ', ' million ', ' billion ', ' trillion ', ' quadrillion ', ' quintillion ', ' sextillion ', ' septillion ',
		' octillion ', ' nonillion ', ' decillion ', ' undecillion ', ' duodecillion ', ' tredecillion ', ' quattuordecillion ', ' quindecillion ', ' sexdecillion ', ' septendecillion ',
		' octodecillion ', ' novemdecillion ', ' vigintillion ', ' centillion ']
one_to_ten = ['', ' one ', ' two ', ' three ', ' four ',
			 ' five ', ' six ', ' seven ', ' eight ', ' nine ', ' ten ']
multiples_of_ten = ['', ' ten ', ' twenty ', ' thirty ', ' fourty ',
			 ' fifty ', ' sixty ', ' seventy ', ' eighty ', ' ninety ']
xteens = [' ten ', ' eleven ', ' twelve', ' thirteen ', ' fourteen ',
			  ' fifteen', ' sixteen', ' seventeen ', ' eighteen ', ' nineteen ']


def stringify_subnum(num: int) -> str:
	'''
	Returns the readable representation of the given subnum.
	subnum - number with 3 digits (for example: 157,598 is made of two subnums - [157,598]).
	'''
	assert type(num) == int and (0 <= num <= 999), 'num must be an integer in range: 0 <= num <= 999'

	number_text = ''
	hundreds = int(num / 100)
	tens = int(num % 100 / 10)
	units = int(num % 10)
	
	if 0 < num <= 10:
		number_text += one_to_ten[num]
	elif 10 < num < 20:
		number_text += xteens[units]
	elif 20 <= num <= 99:
		number_text += multiples_of_ten[tens] + one_to_ten[units]
	elif hundreds < len(one_to_ten):
		number_text += one_to_ten[hundreds] + 'hundred'
		pair = tens * 10 + units
		
		if pair > 0:
			if 10 <= pair <= 19:
				number_text += ' and ' + xteens[pair - 10]
			elif pair < 10:
				number_text += ' and ' + one_to_ten[pair]
			elif pair >= 20:
				if units > 0:
					number_text += multiples_of_ten[tens] + one_to_ten[units]
				else:
					number_text += ' and ' + multiples_of_ten[tens]
	return number_text.strip()


def stringify_num(num) -> str:
	'''
	num - int or str, representing the number to stringify.
	Returns a readable representation of the given num.
	'''
	assert type(num) == str or type(num) == int, 'num must be int or str.'
	
	if type(num) == str:
		num = int(num.replace(',', ''))

	if num == 0:
		return 'zero'

	final_string = ''

	if num < 0:
		final_string = 'minus '
		num = -num

	num_str = format(num, ',d')
	subnums = [int(_) for _ in num_str.split(',')]

	for i in range(0, len(subnums)):
		curr_subnum = subnums[i]
		curr_pos = len(subnums) - i

		final_string += ' ' + stringify_subnum(curr_subnum)

		if curr_pos - 1 and subnums[i] != 0:
			final_string += names[curr_pos] + ','

	# remove excess spaces
	final_string = final_string.replace('  ', ' ')

	# remove spaces before commas
	final_string = final_string.replace(' , ', ', ')

	return final_string.strip(' ,')


def main():
	num = input('Enter number to stringify: ')
	num = num.replace(',', '')

	try:
		print(stringify_num(int(num)))
	except Exception as e:
		print('''Syntax Error.
				\rProper format: ^[\-]?[0-9]+$ (commas are ignored)
				\rFor Example: 1,234,567,890 or -1234567890''')


if __name__ == '__main__':
	main()
