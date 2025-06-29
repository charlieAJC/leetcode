from bisect import bisect_left, insort
from collections import defaultdict


class NumberContainers(object):

    def __init__(self):
        # 記錄索引對應的數字
        self.index_to_number = {}
        # 記錄數字對應的有序索引清單
        self.number_to_indices = defaultdict(list)

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        # version 1 (部分邏輯來自 ChatGPT)
        # # 若索引已存在，需從原數字的索引清單中移除
        # if index in self.index_to_number:
        #     original_number = self.index_to_number[index]
        #     # 僅在數字變更時執行刪除
        #     if original_number != number:
        #         indices = self.number_to_indices[original_number]
        #         pos = bisect_left(indices, index)
        #         if pos < len(indices) and indices[pos] == index:
        #             indices.pop(pos)
        #         # 將索引插入對應數字的有序索引清單
        #         insort(self.number_to_indices[number], index)
        # else:
        #     # 將索引插入對應數字的有序索引清單
        #     insort(self.number_to_indices[number], index)
        # # 更新索引對應的數字
        # self.index_to_number[index] = number
        # =================================================================
        # version 2 (省略 version 1 中無用的邏輯)
        if index in self.index_to_number:
            original_number = self.index_to_number[index]
            if original_number != number:
                indices = self.number_to_indices[original_number]
                pos = bisect_left(indices, index)
                indices.pop(pos)
                insort(self.number_to_indices[number], index)
        else:
            insort(self.number_to_indices[number], index)
        self.index_to_number[index] = number

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        # version 1 (部分邏輯來自 ChatGPT)
        # # 查詢數字對應的最小索引
        # if number in self.number_to_indices:
        #     indices = self.number_to_indices[number]
        #     # 跳過已刪除的索引
        #     while indices and indices[0] not in self.index_to_number:
        #         indices.pop(0)
        #     # 若清單不為空，返回最小索引
        #     if indices:
        #         return indices[0]
        # return -1
        # =================================================================
        # version 2 (省略 version 1 中無用的邏輯)
        if number in self.number_to_indices:
            if len(self.number_to_indices[number]) > 0:
                return self.number_to_indices[number][0]
            else:
                return -1
        return -1

    def debug(self):
        print("self.index_to_number")
        print(self.index_to_number)
        print("self.number_to_indices")
        print(self.number_to_indices)


nc = NumberContainers()
# # There is no index that is filled with number 10. Therefore, we return -1.
# print(nc.find(10))
# # Your container at index 2 will be filled with number 10.
# print(nc.change(2, 10))
# # Your container at index 1 will be filled with number 10.
# print(nc.change(1, 10))
# # Your container at index 3 will be filled with number 10.
# print(nc.change(3, 10))
# # Your container at index 5 will be filled with number 10.
# print(nc.change(5, 10))
# # Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
# print(nc.find(10))
# # Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20.
# print(nc.change(1, 20))
# # Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.
# print(nc.find(10))

print(nc.change(1, 10))
# nc.debug()
print(nc.change(1, 10))
# nc.debug()
print(nc.find(10))
# nc.debug()
print(nc.change(1, 20))
# nc.debug()
print(nc.find(10))
