en = 1
while en == 1:
 a = input("Введи а: ")
 op = input("Введи оператор: ")
 b = input("Введи b: ")

 if op == "+":
	 print(int(a) + int(b))
 if op == "-":
	 print(int(a) - int(b))
 if op == "*":
	 print(int(a) * int(b))
 if op == "/":
	 if int(b) == 0:
		 print("Делить на ноль нельзя!")
else:
		print(int(a) / int(b))
