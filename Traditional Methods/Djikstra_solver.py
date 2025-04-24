import heapq

def dijkstra(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    heap = [(0, start, [start])]
    while heap:
        cost, current, path = heapq.heappop(heap)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        r, c = current
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                heapq.heappush(heap, (cost+1, (nr,nc), path+[(nr,nc)]))
    return []

if __name__ == "__main__":
    maze = [[0,0,0,0,0],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [0,0,0,0,0]]
    start = (0, 0)
    goal = (4, 4)
    print("Dijkstra Path:", dijkstra(maze, start, goal))