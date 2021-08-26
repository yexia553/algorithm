"""
选择排序
    每次扫描一遍所有的数据，找到最小的值跟第一数字交换位置，
    然后从第二个开始再扫描一次，找到最小的值然后跟第二个数字交换位置，
    重复以上步骤

TODO:
优化思路：在每一次循环的时候同时找出最小值和最大值，这样可以减少一半的循环
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
        排序
        """
        unsorted_list = self.generate_list()
        for i in range(len(unsorted_list)):
            min_idx = i
            for j in range(i+1, len(unsorted_list)):
                # 执行次数：n*(n-1)/2,所以时间复杂度是：O(n^2)
                if unsorted_list[j] < unsorted_list[min_idx]:
                    min_idx = j
            # 以下三行中通过临时变量替换原列表中的值，
            # 没有新增任何列表，整个排序过程中只有最开始的那一个列表，
            # 所以空间复杂度是O(1)
            tmp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[min_idx]
            unsorted_list[min_idx] = tmp
            # print("循环的次数：%s, 当前数组的值：%s" % (i, unsorted_list))
        print(unsorted_list)

    def validation(self):
        """
        验证排序算法
        """
        for _ in range(50):
            self.sorting()


sorting = SelectedSorting()
sorting.validation()