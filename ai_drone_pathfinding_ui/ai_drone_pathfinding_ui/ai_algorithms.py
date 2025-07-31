from queue import PriorityQueue

def get_neighbors(pos, grid):
    neighbors = []
    x, y = pos
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 'X':
            neighbors.append((nx, ny))
    return neighbors

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def search_path(grid, start, goal, algorithm='bfs'):
    if algorithm == 'dfs':
        return dfs(grid, start, goal)
    elif algorithm == 'bfs':
        return bfs(grid, start, goal)
    elif algorithm == 'ucs':
        return ucs(grid, start, goal)
    elif algorithm == 'astar':
        return astar(grid, start, goal)
    elif algorithm == 'greedy':
        return greedy(grid, start, goal)
    else:
        return []

def dfs(grid, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (node, path) = stack.pop()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return []

def bfs(grid, start, goal):
    from collections import deque
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (node, path) = queue.popleft()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return []

def ucs(grid, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    visited = set()
    while not pq.empty():
        cost, node, path = pq.get()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                pq.put((cost + 1, neighbor, path + [neighbor]))
    return []

def astar(grid, start, goal):
    pq = PriorityQueue()
    pq.put((0 + heuristic(start, goal), 0, start, [start]))
    visited = set()
    while not pq.empty():
        est, cost, node, path = pq.get()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                new_cost = cost + 1
                priority = new_cost + heuristic(neighbor, goal)
                pq.put((priority, new_cost, neighbor, path + [neighbor]))
    return []

def greedy(grid, start, goal):
    pq = PriorityQueue()
    pq.put((heuristic(start, goal), start, [start]))
    visited = set()
    while not pq.empty():
        h, node, path = pq.get()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                pq.put((heuristic(neighbor, goal), neighbor, path + [neighbor]))
    return []
