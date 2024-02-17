def power(x, y):
	k = 1
	num = x
	while k < y:
		num *= x
		k +=1
	return num

def min_max(s):
	return (min(s), max(s))

def leap_year(year):
	if year % 4 == 0:
		if year % 100 == 0 and year % 400 == 0:
			return True
		elif year % 100 != 0 and year % 400 != 0:
			return True
	return False

def bmi(w, h):
	return w/(h**2)

def rotate(num):
	n = num % 10
	copy = num//10
	k = 0
	while copy > 0:
		copy//=10
		k += 1
	return n*pow(10, k) + (num//10)

def for_min(s):
	min = s[0]
	for k in s:
		if k < min:
			min = k
	return min

def while_min(s):
	k = 0
	min = s[k]
	while k < len(s):
		if s[k] < min:
			min = s[k]
		k += 1
	return min

def for_max(s):
	max = s[0]
	for k in s:
		if k > max:
			max = k
	return max

def while_max(s):
	k = 0
	max = s[k]
	while k < len(s):
		if s[k] > max:
			max = s[k]
		k += 1
	return max

def vowel_count(str):
	string_length, count, k = len(str), 0, 0
	while k < string_length:
		if str[k] == 'a' or str[k] == 'e' or  str[k] == 'i' or  str[k] == 'o' or str[k] == 'u' or str[k] == 'A' or str[k] == 'E' or str[k] == 'I' or str[k] == 'O' or str[k] == 'U':
			count += 1
		k += 1
	return count

def digital_root(num):
	root = 0
	while num > 0:
		root, num = root + num % 10, num//10
	return root
