def dfs(maze, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        current, path = stack.pop()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        r, c = current
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] == 0:
                stack.append(((nr, nc), path + [(nr, nc)]))
    return []

if __name__ == "__main__":
    maze = [[0,0,0,0,0],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [0,0,0,0,0]]
    start = (0, 0)
    goal = (4, 4)
    print("DFS Path:", dfs(maze, start, goal))