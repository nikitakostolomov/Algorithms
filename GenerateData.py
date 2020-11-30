import random


def generate_new_data():  # Функция для создания нового набора данных, которые будут записаны в файлы
    count = 500  # Стартовое количество значений в последовательности
    while count <= 128000:  # Идем до 128000 значений в массиве данных
        sequence = [random.randint(0, 100000) for i in range(count)]  # В последовательность будут записаны случайные числа от 0 до 99999
        if count == 500:
            f = open('500 numbers.txt', 'w')
            for number in sequence:
                f.write(str(number) + '\n')
            f.close()
        if count == 1000:
            f = open('1000 numbers.txt', 'w')
            for number in sequence:
                f.write(str(number) + '\n')
            f.close()
        if count == 2000:
            f = open('2000 numbers.txt', 'w')
            for number in sequence:
                f.write(str(number) + '\n')
            f.close()
        if count == 4000:
            f = open('4000 numbers.txt', 'w')
            for number in sequence:
                f.write(str(number) + '\n')
            f.close()
        if count == 8000:
            f = open('8000 numbers.txt', 'w')
            for number in sequence:
                f.write(str(number) + '\n')
            f.close()
        if count == 16000:
            f = open('16000 numbers.txt', 'w')
            for number in sequence:
                f.write(str(number) + '\n')
            f.close()
        if count == 32000:
            f = open('32000 numbers.txt', 'w')
            for number in sequence:
                f.write(str(number) + '\n')
            f.close()
        if count == 64000:
            f = open('64000 numbers.txt', 'w')
            for number in sequence:
                f.write(str(number) + '\n')
            f.close()
        if count == 128000:
            f = open('128000 numbers.txt', 'w')
            for number in sequence:
                f.write(str(number) + '\n')
            f.close()
        count *= 2
