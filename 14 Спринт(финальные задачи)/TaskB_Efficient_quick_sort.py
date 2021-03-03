#Тимофей решил организовать соревнование по спортивному программированию, чтобы найти талантливых стажёров.
#Задачи подобраны, участники зарегистрированы, тесты написаны. Осталось придумать, как в конце соревнования будет определяться победитель. 
#Каждый участник имеет уникальный логин. Когда соревнование закончится, к нему будут привязаны два показателя: количество решённых задач Pi и размер штрафа Fi. 
#Штраф начисляется за неудачные попытки и время, затраченное на задачу. 
#Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот, у которого решено больше задач. 
#При равенстве числа решённых задач первым идёт участник с меньшим штрафом. 
#Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.
#Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин. 
#В своё отсутствие он поручил вам реализовать алгоритм быстрой сортировки (англ. quick sort) для таблицы результатов. 
#Так как Тимофей любит спортивное программирование и не любит зря расходовать оперативную память, то ваша реализация сортировки не может потреблять O(n) дополнительной памяти для промежуточных данных.

#Формат ввода
#В первой строке задано число участников n, 1 ≤ n ≤ 100 000. 
#В каждой из следующих n строк задана информация про одного из участников.
#i-й участник описывается тремя параметрами:
    #уникальным логином (строкой из маленьких латинских букв длиной не более 20)
    #числом решённых задач Pi
    #штрафом Fi
    #Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.

#Формат вывода
#Для отсортированного списка участников выведите по порядку их логины по одному в строке.

from collections import namedtuple


def quick_sort(array, comparator):  
    def _partition(array, left, right):
        pivot = left
        for student in range(left + 1, right + 1):
            if  comparator(array[left], array[student]):
                pivot += 1
                array[student], array[pivot] = array[pivot], array[student]
        array[pivot], array[left] = array[left], array[pivot]
        return pivot
    
    def _quick_sort(array, low, high):
        if low < high:
            split_index = _partition(array, low, high)
            _quick_sort(array, low, split_index)
            _quick_sort(array, split_index + 1, high)
    _quick_sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    def comparator(member_first, member_second):
        if member_first.points < member_second.points:
            return True
        elif member_first.points > member_second.points:
            return False
        else:
            if member_first.penalties > member_second.penalties:
                return True
            elif member_first.penalties < member_second.penalties:
                return False
            else:
                if member_first.nickname > member_second.nickname:
                    return True
                else:
                    return False

    number_of_participants = int(input())
    students  =  [None] * number_of_participants
    Student = namedtuple('Student', 'nickname points penalties')
    for i in range(number_of_participants):
        try:
            nickname, points, penalties = input().split()
            students[i] = Student(nickname, int(points), int(penalties))
        except ValueError as error:
            raise ValueError(error)
    quick_sort(students, comparator)
    for student in students:
        print(student.nickname)
