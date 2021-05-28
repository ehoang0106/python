def rev_str(str):
	new_str = " "
	index = len(str)
	while index > 0:
		new_str = new_str + str[index -1]
		index = index -1
	return new_str
print(rev_str("hello"))