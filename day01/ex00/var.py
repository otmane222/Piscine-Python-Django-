def my_var():
	lst = [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42,), set()]
	for elem in lst:
		print(f'{elem} has a type {type(elem)}')

if __name__ == '__main__':
	my_var()