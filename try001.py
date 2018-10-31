s = input(" Введите целое число:")
try:
	i = int(s)
	print("Правильно, вы вели целое число:", s)
except ValueError as oshibka:
	print("Ошибочка:", oshibka)
	
	
