cubes = [x**3 for x in range (100) if  x%2 != 0 ]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
sum_of_numbers = 0
sum_of_numbers_list=[]
for i in range(len(cubes)):
    numbers_str = str(cubes[i])
    numbers_list = list(numbers_str)
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])
    for i in range(len(numbers_list)):
        sum_of_numbers = sum_of_numbers + numbers_list[i]
    if sum_of_numbers % 7 == 0:
        print('Cумму чисел, делящихся на 7 : ',sum_of_numbers)
        sum_of_numbers_list.append(sum_of_numbers)
print('Список чисел, делящихся на 7 : ',sum_of_numbers_list)
cubes = [(x**3)+17 for x in range(100) if x%2 == 0]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
sum_of_numbers = 0
sum_of_numbers_list_even_numbers =[]
for i in range(len(cubes)):
    numbers_str = str(cubes[i])
    numbers_list = list(numbers_str)
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])
    for i in range(len(numbers_list)):
        sum_of_numbers = sum_of_numbers + numbers_list[i]
    if sum_of_numbers % 7 == 0:
        print('Cумму чисел, делящихся на 7 : ',sum_of_numbers)
        sum_of_numbers_list_even_numbers.append(sum_of_numbers)
print('Список чисел, делящихся на 7 : ',sum_of_numbers_list_even_numbers)

