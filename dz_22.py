#Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

def function (x, y):
    for i in range(x):
        c = int(input("число для массива "))
        y.append(c)
    return y

a1 = int(input("Введите длину массива "))   
a2 = int(input("Введите длину массива "))       
z1 = []
z2 = []
function(a1, z1)
function(a2, z2)

for i in range(len(z2)):
    z1.append(z2[i])
print(sorted(z1))