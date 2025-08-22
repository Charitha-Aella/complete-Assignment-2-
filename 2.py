import math

class PathFinder:
    def _init_(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.start = (0, 0)
        self.goal = (self.n - 1, self.n - 1)
        self.dirs = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1),           (0, 1),
                     (1, -1),  (1, 0),  (1, 1)]

    def h(self, node):
        (x1, y1), (x2, y2) = node, self.goal
        return math.sqrt((x1 - x2) * 2 + (y1 - y2) * 2)

    def goal_test(self, node):
        return node == self.goal

    def move_gen(self, node, closed):
        x, y = node
        moves = []
        for dx, dy in self.dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                if self.grid[nx][ny] == 0 and (nx, ny) not in closed:
                    moves.append((nx, ny))
        return moves

    def _reconstruct(self, parents, end):
        path = [end]
        while path[-1] in parents:
            path.append(parents[path[-1]])
        path.reverse()
        return path

    def a_star_search(self):
        if self.grid[0][0] != 0 or self.grid[self.n - 1][self.n - 1] != 0:
            return -1, []
        open_list = [self.start]
        closed = set()
        parents = {}
        g = {self.start: 0}
        while open_list:
            current = min(open_list, key=lambda n: g.get(n, float('inf')) + self.h(n))
            open_list.remove(current)
            if self.goal_test(current):
                path = self._reconstruct(parents, current)
                return len(path), path
            closed.add(current)
            for nb in self.move_gen(current, closed):
                tentative_g = g[current] + 1
                if tentative_g < g.get(nb, float('inf')):
                    parents[nb] = current
                    g[nb] = tentative_g
                    if nb not in open_list and nb not in closed:
                        open_list.append(nb)
        return -1, []


grid1 = [[0, 1], [1, 0]]
grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
grid3 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]

pf1 = PathFinder(grid1)
print(pf1.a_star_search())

pf2 = PathFinder(grid2)
print(pf2.a_star_search())

pf3 = PathFinder(grid3)
print(pf3.a_star_search())
