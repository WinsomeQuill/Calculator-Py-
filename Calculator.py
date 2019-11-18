"""
Простой калькулятор на Python3 от WinsomeQuill :)
Плюсы:
	- Защита от крашей
	- Русский язык
	- Язык Python3
	- Много функций (больше чем в С++ версии)
	- Есть меню помощи
	
Минусы:
	- Возможно есть баги
	- Плохой код и нет оптимизации

Итог: Если хотите получть 5 по информатики, то качайте, если хотите взять за основу, то бросайте эту затею.
"""

#------------------------[Подгрузка нужных библиотек]------------------------#
from math import sqrt
from math import sin
from math import cos
from math import tan
from math import isfinite
from math import radians
from math import degrees
import math


#------------------------[Переменные]------------------------#
en = 1 #Нужна для цикла
hen = 0

#------------------------[Очистка в отдельном коде]------------------------#
def clear():
	print("\n"*3) 	

#------------------------[Главный код]------------------------#
while en == 1: #Цикл
	print("calc - калькулятор")
	print("disc - дискриминант")
	print("clear - очистить консоль")
	print("help - помощь")
	line = input("")
	
#------------------------[Код калькулятора]------------------------#	
	if line == "calc":
		try:
			a = float(input("Введи а: "))
		except ValueError:
				print("<WARNING> Сработала защита от краша!")
				continue
		else:
			op = input("Введи оператор: ")
			if op == "k":
				print(sqrt(a))
				continue
			if op == "sin":
				print(sin(a))
				continue
			if op == "cos":
				print(cos(a))
				continue
			if op == "tg":
				print(tan(a))
				continue
			if op == "inrad":
				print(radians(a))
				continue 
			if op == "ingrad":
				print(degrees(a))
				continue
		if op == "k" or op == "+" or op == "-" or op == "*" or op == "/" or op == "^":
			try:
				b = float(input("Введи b: "))
			except ValueError:
				print("<WARNING> Сработала защита от краша!")
				continue
			if op == "+":
				print(int(a) + int(b))
				clear()
			if op == "-":
				print(int(a) - int(b))
				clear()
			if op == "*":
				print(int(a) * int(b))
				clear()
			if op == "^":
				print(int(a) ** int(b))
				clear()
			if op == "/":
				if int(b) == 0:
					print("Делить на ноль нельзя!")
				else:
					print(int(a) / int(b))
					clear()
		else:
			print("Такого оператора нету!")
			clear()
			
#------------------------[Код дискриминанта]------------------------#		
	if line == "disc":
				print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
				a = float(input("a = "))
				b = float(input("b = "))
				c = float(input("c = "))
				
				discr = b ** 2 - 4 * a * c
				print("Дискриминант (D) = %.2f" % discr)
				
				if discr > 0:
					x1 = (-b + math.sqrt(discr)) / (2 * a)
					x2 = (-b - math.sqrt(discr)) / (2 * a)
					print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
				elif discr == 0:
					x = -b / (2 * a)
					print("x = %.2f" % x)
				else:
					print("Корней нет")
					
#------------------------[Код меню помощи]------------------------#
	if line == "help":
		print("\n----Меню помощи----")
		print("Введи цифру чтобы открыть нужный раздел") ##########################
		print("1. Оператора калькулятора")
		print("2. На каком языке написано данный скрипт?")
		print("3. Связь с создателем")
		print("0. Выход")
		print("Версия скрипта 1.1 (18.11.2019)")
		print("---------------------------------\n")
		hen = 1
		
		while hen == 1:
			
			hline = input("Номер: ")
			if hline == "1":
			    	print("\nКалькулятор поддерживает следующие операторы:")
			    	print("\n\"+\" - сложение\n\"-\" - вычитание\n\"*\" - умножение\n\"/\" - деление\n\"k\" - корень\n\"sin\" - синус (в рад.)\n\"cos\" - косинус (в рад.)\n\"tg\" - тангенс\n\"inrad\" - перевести градусы в радианы\n\"ingrad\" - перевести из радиан в градусы\n")
			
			if hline == "2":
			    	print("\nДанный скрипт был написан на языке программирования Python3 \n")
			
			if hline == "3":
			    	print("\nПочта - Doshikplayer@gmail.com")
			    	print("ВК - vk.com/winsomequill")
			    	print("Форум - Forum.QuartzLand.Ru\n")
			
			if hline == "0":
			    	hen = 0
			    	print("\nУдачи ;)\n")
			    	
#------------------------[Код очистки консоли]------------------------#
	if line == "clear":
		print("\n"*100)
