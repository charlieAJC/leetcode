class ProductOfNumbers(object):

    def __init__(self):
        self.prefix_product = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prefix_product = [1]
        else:
            self.prefix_product.append(self.prefix_product[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.prefix_product):
            return 0
        else:
            return self.prefix_product[-1] // self.prefix_product[-k - 1]


productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)
# [3]
productOfNumbers.add(0)
# [3,0]
productOfNumbers.add(2)
# [3,0,2]
productOfNumbers.add(5)
# [3,0,2,5]
productOfNumbers.add(4)
# [3,0,2,5,4]
print(productOfNumbers.getProduct(2))
# return 20. The product of the last 2 numbers is 5 * 4 = 20
print(productOfNumbers.getProduct(3))
# return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
print(productOfNumbers.getProduct(4))
# return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8)
# [3,0,2,5,4,8]
print(productOfNumbers.getProduct(2))
# return 32. The product of the last 2 numbers is 4 * 8 = 32


# nums = [3, 4, 5, 2]
# prefix_product = [1, 3, 12, 60, 120]
# 假設 k = 3，答案是 40
# 40 = 120 / 3 = prefix_product[-1] // prefix_product[-4]
# prefix_product[-4] = prefix_product[2] = nums 前 1 個數的乘積
