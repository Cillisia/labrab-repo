numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
l = len(numbers)
summ = 0
for i in range(l):
    if numbers[i] is None:
        position = i

summ = sum(numbers[:position])+ sum(numbers[position+1:])
average = summ/l
numbers[position]=average
print("Измененный список:", numbers)
