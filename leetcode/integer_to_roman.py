class Solution(object):
    def int_to_roman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        store_int_roman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"],
                         [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]

        for i in range(len(store_int_roman)):
            while num >= store_int_roman[i][0]:
                roman += store_int_roman[i][1]
                num -= store_int_roman[i][0]
        return roman
