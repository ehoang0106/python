def reverser_string(str):
	new_str = ""
	index = len(str)
	while index > 0:
		new_str += str[index -1]
		index -= 1
	return new_str
#-----------------

def master_yoda(text):
    return ' '.join(text.split()[::-1])

print(master_yoda("aihhi do cho"))