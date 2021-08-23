"""
选择排序
    每次扫描一遍所有的数据，找到最小的值跟第一数字交换位置，
    然后从第二个开始再扫描一次，找到最小的值然后跟第二个数字交换位置，
    重复以上步骤
"""
class SelectedSorting():
    def __init__(self) -> None:
        self.unsorted_list = [1, 5, 8, 3, 9, 10, 30, 23, 7, 34]
    
    def selected_sorting(self):
        for i in range(len(self.unsorted_list)):
            min_idx = i
            for j in range(i+1, len(self.unsorted_list)):
                if self.unsorted_list[j] < self.unsorted_list[min_idx]:
                    min_idx = j
            tmp = self.unsorted_list[i]
            self.unsorted_list[i] = self.unsorted_list[min_idx]
            self.unsorted_list[min_idx] = tmp
            print("循环的次数：%s, 当前数组的值：%s" % (i, self.unsorted_list))


sorting = SelectedSorting()
sorting.selected_sorting()