from HeapSort import heap_sort
from GenerateData import generate_new_data
import time

# Функция для получения среднего времени сортировки последовательности чисел, чтобы получить более усредненное время,
# можно передать в функцию второй необязательный параметр count_to_get_average_time, который увелчит количество
# итераций цикла
def get_average_time_of_sort(sequence, count_to_get_average_time=10):
    average = 0
    for i in range(count_to_get_average_time):
        sequence_to_sort = sequence
        start_time = time.time()
        heap_sort(sequence_to_sort)
        average += time.time() - start_time
    print(average / count_to_get_average_time)


generate_new_data()  # Создаем новый набор данных, для повторного создания раскомменитровать

with open('500 numbers.txt') as inf:
    sequence_of_500 = [int(line) for line in inf]
print('Average time of sort of 500 numbers is:')
get_average_time_of_sort(sequence_of_500)

with open('1000 numbers.txt') as inf:
    sequence_of_1000 = [int(line) for line in inf]
print('Average time of sort of 1000 numbers is:')
get_average_time_of_sort(sequence_of_1000)

with open('2000 numbers.txt') as inf:
    sequence_of_2000 = [int(line) for line in inf]
print('Average time of sort of 2000 numbers is:')
get_average_time_of_sort(sequence_of_2000)

with open('4000 numbers.txt') as inf:
    sequence_of_4000 = [int(line) for line in inf]
print('Average time of sort of 4000 numbers is:')
get_average_time_of_sort(sequence_of_4000)

with open('8000 numbers.txt') as inf:
    sequence_of_8000 = [int(line) for line in inf]
print('Average time of sort of 8000 numbers is:')
get_average_time_of_sort(sequence_of_8000)

with open('16000 numbers.txt') as inf:
    sequence_of_16000 = [int(line) for line in inf]
print('Average time of sort of 16000 numbers is:')
get_average_time_of_sort(sequence_of_16000)

with open('32000 numbers.txt') as inf:
    sequence_of_32000 = [int(line) for line in inf]
print('Average time of sort of 32000 numbers is:')
get_average_time_of_sort(sequence_of_32000)

with open('64000 numbers.txt') as inf:
    sequence_of_64000 = [int(line) for line in inf]
print('Average time of sort of 64000 numbers is:')
get_average_time_of_sort(sequence_of_64000)

with open('128000 numbers.txt') as inf:
    sequence_of_128000 = [int(line) for line in inf]
print('Average time of sort of 128000 numbers is:')
get_average_time_of_sort(sequence_of_128000)
