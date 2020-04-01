
var = 0
x = 0
for i in range(10):
    var = var + 1
    print("Введите число № " + str(var))
    z = input()
    if z == 5:
        x+=1
print(x)




print('Goal 2')
sum = 0
for i in range(10):
    answer = int(input('Напишите любую цифру: '))
    if answer == 5:
        sum += 1

print('Количество пятёрок равно', sum)
print('')