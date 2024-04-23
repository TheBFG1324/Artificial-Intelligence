import heapq

def getGrid():
    return [[0,0,0,0,0,0,0,0],
            [0,0,-1,-1,-1,-1,0,0],
            [0,0,0,0,0,-1,0,0],
            [0,0,0,0,0,-1,0,0]]

def getBigGrid():
    grid = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if i < 50:    # rear of bugtrap
                d = abs(i - 51) + abs(j - 50)
                if d == 50:
                    grid[i][j] = -1  # Set -1 for obstacles
            else:        # front of bugtrap
                if j > 50:  # upper lobe
                    d = abs(i - 50) + abs(j - 75)
                    if d == 24:
                        grid[i][j] = -1  # Set -1 for obstacles
                elif j < 50:  # lower lobe
                    d = abs(i - 50) + abs(j - 25)
                    if d == 24:
                        grid[i][j] = -1  # Set -1 for obstacles
    return grid

def valid_move(grid, cord, M, N):
    if cord[0] < 0 or cord[0] >= M:
        return False
    if cord[1] < 0 or cord[1] >= N:
        return False
    if grid[cord[0]][cord[1]] < 0:
        return False
    return True

def getMovesBFS(grid, cord, M, N):
    up = (cord[0]-1, cord[1])
    right = (cord[0], cord[1] + 1)
    down = (cord[0] + 1, cord[1])
    left = (cord[0], cord[1] - 1)
    moves = [left, up, right, down]
    ans = []
    for move in moves:
        if valid_move(grid, move, M, N):
            ans.append(move)
    return ans

def reconstruct_path(cord, init, visited):
    path = []
    cur = cord
    while cur != init:
        path.append(cur)
        cur = visited[cur]
    path.append(init)
    return path[::-1]

def bfs(grid, init, goal, M, N):
    queue = [init]
    visited = {init: None}
    closed = set()
    fringe = set([init])

    while queue:
        cord = queue.pop(0)
        closed.add(cord)
        fringe.remove(cord)

        if cord == goal:
            path = reconstruct_path(cord, init, visited)
            return len(closed), len(fringe), len(path)

        new_moves = getMovesBFS(grid, cord, M, N)
        for x in new_moves:
            if x not in visited:
                visited[x] = cord
                queue.append(x)
                fringe.add(x)

    return len(closed), len(fringe), -1

def man_distance(cord, goal):
    return abs(cord[0] - goal[0]) + abs(cord[1] - goal[1])

def gbfs(grid, init, goal, M, N):
    queue = [(man_distance(init, goal), init)]
    visited = {init: None}
    closed = set()
    fringe = set([init])

    while queue:
        _, current = heapq.heappop(queue)
        closed.add(current)
        fringe.remove(current)

        if current == goal:
            path = reconstruct_path(current, init, visited)
            return len(closed), len(fringe), len(path)

        moves = getMovesBFS(grid, current, M, N)
        for move in moves:
            if move not in visited:
                visited[move] = current
                heapq.heappush(queue, (man_distance(move, goal), move))
                fringe.add(move)

    return len(closed), len(fringe), -1

def aStar(grid, init, goal, M, N):
    queue = [(man_distance(init, goal), 0, init)]
    visited = {init: None}
    closed = set()
    fringe = set([init])
    cost_so_far = {init: 0}

    while queue:
        _, cost, current = heapq.heappop(queue)
        closed.add(current)
        fringe.remove(current)

        if current == goal:
            path = reconstruct_path(current, init, visited)
            return len(closed), len(fringe), len(path)
        
        for move in getMovesBFS(grid, current, M, N):
            new_cost = cost + 1
            if move not in cost_so_far or new_cost < cost_so_far[move]:
                cost_so_far[move] = new_cost
                priority = new_cost + man_distance(move, goal)
                heapq.heappush(queue, (priority, new_cost, move))
                visited[move] = current
                fringe.add(move)

    return len(closed), len(fringe), -1

# Test on small grid
g = getGrid()
M = len(g)
N = len(g[0])
init_pos = (3,2)
goal_pos = (3,6)

# Test on big grid
big_grid = getBigGrid()
big_M = len(big_grid)
big_N = len(big_grid[0])
big_init_pos = (50, 55)
big_goal_pos = (75, 70)

#Run BFS on test grid
closed, fringe, path_length = bfs(g, goal_pos, init_pos, M, N)
print(f"BFS test: Closed={closed}, Fringe={fringe}, Path Length={path_length}")
#Run GBFS on test grid
closed, fringe, path_length = gbfs(g, goal_pos, init_pos, M, N)
print(f"GBFS test: Closed={closed}, Fringe={fringe}, Path Length={path_length}")
#Run A* on test grid
closed, fringe, path_length = aStar(g, goal_pos, init_pos, M, N)
print(f"A* test: Closed={closed}, Fringe={fringe}, Path Length={path_length}")
# Run BFS on big grid
closed, fringe, path_length = bfs(big_grid, big_goal_pos, big_init_pos, big_M, big_N)
print(f"BFS Big grid: Closed={closed}, Fringe={fringe}, Path Length={path_length}")

# Run GBFS on big grid
closed, fringe, path_length = gbfs(big_grid, big_goal_pos, big_init_pos, big_M, big_N)
print(f"GBFS Big grid: Closed={closed}, Fringe={fringe}, Path Length={path_length}")

# Run A* on big grid
closed, fringe, path_length = aStar(big_grid, big_goal_pos, big_init_pos, big_M, big_N)
print(f"A* Big grid: Closed={closed}, Fringe={fringe}, Path Length={path_length}")

