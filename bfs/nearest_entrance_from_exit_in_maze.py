from queue import Queue

# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/?envType=study-plan-v2&envId=leetcode-75

# note: we need to track the depth in the queue (could be the third index or z coordinate)

def valid(maze: list[list[str]], location: list[int]) -> bool:
    # check if valid index
    max_row_index = len(maze) - 1
    max_column_index = len(maze[0]) - 1
    if location[0] > max_row_index or location[1] > max_column_index:
        return False
    # check if wall
    if maze[location[0]][location[1]] == "+":
        return False
    return True

def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    q = Queue()
    q.put(entrance)
    maze[entrance[0]][entrance[1]] = "+"
    count = 0
    while not q.empty():
        current = q.get()
        if current[0] == 0 or current[1] == 0:
            return count
    
        count = count + 1

        # up
        up = [current[0]-1,current[1]]
        if valid(maze, up):
            q.put(up)
        # down
        down = [current[0]+1,current[1]]
        if valid(maze, down):
            q.put(down)
        # left
        left = [current[0],current[1]]
        if valid(maze, down):
            q.put(down)
        # right

        count = count + 1
        print(q.qsize())
    # print(valid(maze, [1,5]))
    return -1


if __name__ == "__main__":
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    nearestExit(maze, entrance)
