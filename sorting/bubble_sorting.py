"""
冒泡排序

TODO:
    把时间复杂度优化成O(n)
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
        冒泡排序：
        从第一个数开始，跟后面所有的值比较，如果比后面的大，就把这个数的位置往后挪一个，直到比较到最后一个位置，
        
        两个循环中的边界值要多思考
        """
        unsorted_list = self.generate_list()
        # 时间复杂度 O(n^2)
        for i in range(len(unsorted_list)):
            for j in range(len(unsorted_list)-(i+1)):
                if unsorted_list[j] > unsorted_list[j+1]:
                    # 空间复杂度是O(1)
                    tmp = unsorted_list[j]
                    unsorted_list[j] = unsorted_list[j+1]
                    unsorted_list[j+1] = tmp
        print(unsorted_list)

    def validation(self):
        """
        验证算法
        """
        for _ in range(50):
            self.sorting()


sorting = SelectedSorting()
sorting.validation()