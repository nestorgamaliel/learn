def _suma(*valo):
	print(f'{valo=}')
	result = 0
	for v in valo:
		result += v
	return result


print(_suma(4,3,2,1))
