# def explore(start, target, grid):
#     m, n = len(grid), len(grid[0])
#     marked = [[0 for _ in range(n)] for _ in range(m)]
#     marked[start[0]][start[1]] = 1
#     queue = [start]
#
#     def neighbors(point):
#         x, y = point
#         possible_neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
#         return [(nx, ny) for nx, ny in possible_neighbors if 0 <= nx < m and 0 <= ny < n]
#
#     while queue:
#         current = queue.pop()
#         for neighbor in neighbors(current):
#             nx, ny = neighbor
#             if not marked[nx][ny] and grid[nx][ny] == 0:  # Assuming 0 represents an open cell
#                 marked[nx][ny] = 1
#                 queue.insert(0, (nx, ny))
#
#     return marked[target[0]][target[1]]
#
# # Example usage:
# grid = [
#     [0, 0, 0, 0],
#     [0, 1, 1, 0],
#     [0, 0, 0, 0],
#     [0, 1, 0, 0]
# ]
#
# start_point = (0, 0)
# target_point = (3, 3)
#
# result = explore(start_point, target_point, grid)
# print(result)


# x = float('inf')
# if x > 500000000000000000000000000000000000000000:
#     print(int(x))

def mystery(l):
  list1 = l[0:5]
  return list1


list1 = [44,71,12,8,23,17,16]
result = mystery(list1)
print(result)
print(list1)



