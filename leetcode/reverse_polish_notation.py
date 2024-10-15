class Solution:
    def evalRPN(self, tokens: list[str]):
        res_list = []
        for s in range(len(tokens)):
            char = tokens[s]

            if char == "+":
                result = res_list[-2] + res_list[-1]
                res_list.pop()
                res_list.pop()
            elif char == "-":
                result = res_list[-2] - res_list[-1]
                res_list.pop()
                res_list.pop()
            elif char == "*":
                result = res_list[-2] * res_list[-1]
                res_list.pop()
                res_list.pop()
            elif char == "/":
                result = int(float(res_list[-2]) / res_list[-1])
                res_list.pop()
                res_list.pop()
            else:
                result = int(char)

            res_list.append(result)
        return res_list[-1]


a = Solution()
print(a.evalRPN(tokens=["4","13","5","/","+"]
                ))
