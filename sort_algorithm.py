def bubble_sort(array_to_sort):
    length = len(array_to_sort)
    for i in range(length):
        for j in range(length - i - 1):
            if array_to_sort[j] > array_to_sort[j + 1]:
                array_to_sort[j], array_to_sort[j + 1] = array_to_sort[j + 1], array_to_sort[j]
    return array_to_sort


def select_sort(array_to_sort):
    length = len(array_to_sort)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if array_to_sort[min_index] > array_to_sort[j]:
                min_index = j
        array_to_sort[i], array_to_sort[min_index] = array_to_sort[min_index], array_to_sort[i]
    return array_to_sort


def insert_sort(array_to_sort):
    length = len(array_to_sort)
    for i in range(length):
        for j in range(i):
            if array_to_sort[i - j] < array_to_sort[i - j - 1]:
                array_to_sort[i - j], array_to_sort[i - j - 1] = array_to_sort[i - j - 1], array_to_sort[i - j]
            else:
                break
    return array_to_sort


def quick_sort(array_to_sort, start, end):
    # 判断low是否小于high,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = array_to_sort[i]
        while i < j:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (array_to_sort[j] >= base):
                j = j - 1
            # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            array_to_sort[i] = array_to_sort[j]
            # 同样的方式比较前半区
            while (i < j) and (array_to_sort[i] <= base):
                i = i + 1
            array_to_sort[j] = array_to_sort[i]
            # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
            array_to_sort[i] = base
        # 递归前后半区
        quick_sort(array_to_sort, start, i - 1)
        quick_sort(array_to_sort, j + 1, end)
    return array_to_sort


def shell_sort(array_to_sort):
    n = len(array_to_sort)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and array_to_sort[j - gap] > array_to_sort[j]:
                array_to_sort[j - gap], array_to_sort[j] = array_to_sort[j], array_to_sort[j - gap]
                j -= gap
        gap = gap // 2
    return array_to_sort


def merge_sort(array_to_sort):
    if len(array_to_sort) <= 1:
        return array_to_sort
    mid = len(array_to_sort) // 2
    left = merge_sort(array_to_sort[:mid])
    right = merge_sort(array_to_sort[mid:])
    return merge(left, right)


def merge(a_list, b_list):
    i = j = 0
    c_list = []
    while a_list and b_list:
        if a_list[0] < b_list[0]:
            c_list.append(a_list.pop(0))
        else:
            c_list.append(b_list.pop(0))
    c_list = c_list + a_list + b_list
    return c_list


if __name__ == '__main__':
    array = [2354, 4325435, 3462, 35, 123, 24, 3, 4, 5, 6]
    # print(bubble_sort(array))
    # print(select_sort(array))
    # print(insert_sort(array))
    # print(quick_sort(array, 0, len(array) - 1))
    # print(shell_sort(array))
    print(merge_sort(array))
