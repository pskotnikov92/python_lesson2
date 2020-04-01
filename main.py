#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
'''
number_line = 0
for i in range(1,6):
    number_line=0+i
    print("0 " + "(Line number " + str(number_line) + ")")
'''
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

'''
var = 0
x = 0
for i in range(10):
    var = var + 1
    print("Введите число № " + str(var))
    input()
    if input == 5:
        x = x + 1
print(x)
'''

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

'''
sum = 0
for i in range(1,101):
    sum+=i
print(sum)
'''

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

'''
pro = 1
for i in range(1,11):
    pro*=i
print(pro)
'''

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

'''
integer_number = 2129

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10
'''

'''
Задача 6
Найти сумму цифр числа.
'''

'''
integer_number = 852137
sumx = 0

while integer_number>0:
    if integer_number != 0:
        sumx = sumx + integer_number%10
        integer_number = integer_number//10

print(sumx)
'''

'''
Задача 7
Найти произведение цифр числа.
'''

'''
integer_number = 8529
prox = 1

while integer_number>0:
    if integer_number != 0:
        prox = prox * (integer_number%10)
        integer_number = integer_number//10

print(prox)
'''

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

'''
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
'''

'''
Задача 9
Найти максимальную цифру в числе
'''

'''
number = 1254685
max = number%10
number = number//10
while number > 0:
    if number%10 > max:
        max = number%10
    number = number//10
print(max)
'''

'''
Задача 10
Найти количество цифр 5 в числе
'''

'''
integer_number = 56758556789769
v = 0
while integer_number>0:
    if integer_number%10 == 5:
        v = v + 1
    integer_number = integer_number//10
print(v)
'''