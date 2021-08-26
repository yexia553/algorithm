"""
插入排序
"""
import random


class SelectedSorting():
    def __init__(self):
        pass
    
    def generate_list(self):
        """
        生成一个随机的列表
        """
        l = list()
        for _ in range(50):
            l.append(random.randint(1, 10000))
        
        return l

    def sorting(self):
        """
        插入排序
        与冒泡排序非常像，
        """
        unsorted_list = self.generate_list()
        for i in range(1, len(unsorted_list)-1):
            for j in range(i, 0, -1):
                if unsorted_list[j] < unsorted_list[j-1]:
                    tmp = unsorted_list[j]
                    unsorted_list[j] = unsorted_list[j-1]
                    unsorted_list[j-1] = tmp
                else:
                    break
        print(unsorted_list)

    def validation(self):
        """
        验证算法
        """
        for _ in range(50):
            self.sorting()


sorting = SelectedSorting()
sorting.validation()