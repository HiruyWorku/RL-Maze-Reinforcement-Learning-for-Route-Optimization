import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    heap = [(0 + heuristic(start, goal), 0, start, [start])]
    visited = set()
    while heap:
        est, cost, current, path = heapq.heappop(heap)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        r, c = current
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                next_pos = (nr, nc)
                heapq.heappush(heap, (cost+1+heuristic(next_pos, goal), cost+1, next_pos, path+[next_pos]))
    return []

if __name__ == "__main__":
    maze = [[0,0,0,0,0],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [0,0,0,0,0]]
    start = (0, 0)
    goal = (4, 4)
    print("A* Path:", astar(maze, start, goal))