# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
my_list = list(range(1, 10))
length_my_list = len(my_list)
print("Введите через Enter 9 чисел:")
for i in range(0, length_my_list):
    my_list[i] = int(input())

my_new_list = list(range(1, 6))
length_my_new_list = len(my_new_list)

for i in range(0, length_my_new_list):
    if i <= length_my_list - 1:
        my_new_list[i] = my_list[i] * my_list[length_my_list - 1]
        length_my_list -= 1
print(my_new_list)