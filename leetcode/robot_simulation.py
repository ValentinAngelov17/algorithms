class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x, y = 0, 0
        furthest_point = 0
        possible_directions = {"up": ("left", "right"),
                               "right": ("up", "down"),
                               "down": ("right", "left"),
                               "left": ("down", "up")}

        current_direction = "up"
        for command in commands:
            if command == -2:
                current_direction = possible_directions[current_direction][0]
                continue
            elif command == -1:
                current_direction = possible_directions[current_direction][1]
                continue
            else:
                if current_direction == "up":
                    y += command
                elif current_direction == "down":
                    y -= command
                elif current_direction == "right":
                    x += command
                else:
                    x -= command

            current_point = x ** 2 + y ** 2
            if current_point >= furthest_point:
                furthest_point = current_point

        return furthest_point


a = Solution()
print(a.robotSim(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]))
