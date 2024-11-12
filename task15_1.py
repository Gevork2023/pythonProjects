num = int(input("Введите число: "))
num_list_1 = []
for digit in range(1, num + 1, 2):
     num_list_1.append(digit)
print(f"Список из нечётных чисел от одного до N: {num_list_1}")