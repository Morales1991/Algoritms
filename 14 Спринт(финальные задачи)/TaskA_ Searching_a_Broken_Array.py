#Алла ошиблась при копировании из одной структуры данных в другую.
# Она хранила массив чисел в кольцевом буфере.
# Массив был отсортирован по возрастанию, и в нём можно было найти элемент за логарифмическое время.
# Алла скопировала данные из кольцевого буфера в обычный массив, но сдвинула данные исходной отсортированной последовательности.
# Теперь массив не является отсортированным. Тем не менее, нужно обеспечить возможность находить в нем элемент за nLog(n)
#Можно предполагать, что в массиве только уникальные элементы.

#Формат ввода
#В первой строке записано число n –— длина массива.
#Во второй строке записано положительное число k –— искомый элемент. 
#n и k не превосходят 10 000.
#Далее в строку через пробел записано n натуральных чисел, каждое из которых не превосходит 10 000.

#Формат вывода
#Выведите индекс искомого элемента в массиве, если он найден (нумерация с нуля). Иначе выведите -1.

def search_in_broken_array(array, item):
    left = 0
    right = len(array) - 1
    while left <= right:
        if array[left] <= item <= array[right]:
            return binary_search(array, left, right, item)
        mid = (left + right) // 2
        if array[mid] < item < array[left]:
            return binary_search(array, mid + 1, right, item)
        if array[left] <= item <= array[mid]:
            return binary_search(array, left, mid, item)
        if item <= array[mid] < array[left]:
            right = mid
        else:
            left = mid + 1
    return -1

def binary_search(array, left, right, item):
    while left <= right:
        if array[left] == item:
            return left
        if array[right] == item:
            return right
        mid = (left + right) // 2
        if array[mid] == item:
            return mid
        if item < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    input()
    item = int(input())
    array = list(map(int, input().split()))
    print(search_in_broken_array(array, item))
