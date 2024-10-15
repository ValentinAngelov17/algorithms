from fractions import Fraction


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        numbers = []
        operations = []
        result = 0

        for index, value in enumerate(expression):
            if value == "/":
                number = float(expression[index - 1]) / float(expression[index + 1])
                if expression[0] == "-":
                    number = - float(expression[index - 1]) / float(expression[index + 1])
                numbers.append(number)
            elif value == "+":
                operations.append("+")
            elif value == "-":
                operations.append("-")
        for number in range(len(numbers) - 1):
            for operation in operations:
                if operation == "+":
                    result = numbers[number + 1] + numbers[number]
                else:
                    result = numbers[number] - numbers[number + 1]

        return result


a = Solution()
print(a.fractionAddition("1/3-1/2"))
