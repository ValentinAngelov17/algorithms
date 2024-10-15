class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cash = []
        is_okay = True
        for bill in bills:
            cash.append(bill)

            if bill == 10:
                if 5 in cash:
                    cash.remove(5)
                else:
                    is_okay = False
                    break

            elif bill == 20:
                if 5 in cash and 10 in cash:
                    cash.remove(5)
                    cash.remove(10)
                elif cash.count(5) >= 3:
                    for _ in range(3):
                        cash.remove(5)
                else:
                    is_okay = False
                    break
        if is_okay:
            return True
        else:
            return False


a = Solution()
print(a.lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]))
