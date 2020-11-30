def heap_sort(sequence):

    def sift_down(parent, limit):
        item = sequence[parent]
        while True:
            child = (parent * 2) + 1
            if child >= limit:
                break
            if child + 1 < limit and sequence[child] < sequence[child + 1]:
                child += 1
            if item < sequence[child]:
                sequence[parent] = sequence[child]
                parent = child
            else:
                break
        sequence[parent] = item
    # Тело функции heap_sort
    length = len(sequence)
    # Формирование первичной пирамиды
    for index in range((length // 2) - 1, -1, -1):
        sift_down(index, length)
    # Окончательное упорядочение
    for index in range(length - 1, 0, -1):
        sequence[0], sequence[index] = sequence[index], sequence[0]
        sift_down(0, index)