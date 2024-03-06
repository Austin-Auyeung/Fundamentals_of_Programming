import statistics
def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        # find the median
        median_value = statistics.median([list1[0], list1[len(list1)//2], list1[-1]])
        left_list = []
        middle_list = []
        right_list = []

        for i in list1:
            if i < median_value:
                left_list.append(i)
            elif i > median_value:
                right_list.append(i)
            else:
                middle_list.append(i)
        return quick_sort(left_list) + middle_list + quick_sort(right_list)


list1 = [31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28]
print(quick_sort(list1))