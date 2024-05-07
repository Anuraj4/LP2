# BFS

n = int(input("Enter number of nodes: "))
p = input("Goal Node:")

graph = {}


print("Enter edges in the format 'node1 node2'.")
for i in range(n):
    node, *neighbors = input("Enter node and its roots separated by spaces: ").split()
    graph[node] = neighbors


visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        if m == p:
            print("\n" + p + " is the goal node and is found!")
            break

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("\nFollowing is the Breadth-First Search:")
bfs(visited, graph, "a")

# DFS

n = int(input("Enter number of nodes: "))
root = input("Enter the root node: ")
goal_node = input("Enter the goal node: ")

graph = {}

print("Enter edges in the format 'node root1 root2 ...'.")
for _ in range(n):
    node, *neighbors = input("Enter node and its roots separated by spaces: ").split()
    graph[node] = neighbors

visited = []


def dfs(visited, graph, node, goal_node):
    if node not in visited:
        print(node)
        visited.append(node)
        if node == goal_node:
            print(node, " is a goal node and is found")
            return True
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour, goal_node):
                return True
    return False


# Driver Code
print("Depth-First Search (DFS):")
dfs(visited, graph, root, goal_node)


# Define the N-Queens problem
class NQueensProblem:
    def __init__(self, n):
        self.n = n

    def transition(self, state):
        # Generate all valid successor states from the current state
        # (Move each queen to a different row in its column)
        successors = []
        for col in range(self.n):
            for row in range(self.n):
                if row != state[col]:
                    successor = state[:col] + (row,) + state[col + 1 :]
                    successors.append(successor)
        return successors

    def cost(self, state):
        # Calculate the number of attacked queens
        attacked_queens = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                    attacked_queens += 1
        return attacked_queens

    def heuristic(self, state):
        # Heuristic: Number of attacked queens
        return self.cost(state)


# A* search
def a_star_search(problem):
    start_state = tuple(range(problem.n))
    # Initial state (all queens in different rows)
    open_set = [(problem.heuristic(start_state), start_state)]
    # Priority queue
    closed_set = set()

    while open_set:
        _, current_state = open_set.pop(0)
        # Get state with lowest f(n) value
        if current_state not in closed_set:
            closed_set.add(current_state)
            if problem.cost(current_state) == 0:
                return current_state  # Found a solution
            successors = problem.transition(current_state)
            for successor in successors:
                f_value = problem.cost(successor) + problem.heuristic(successor)
                open_set.append((f_value, successor))
            open_set.sort()  # Sort by f(n) value

    return None  # No solution found


if __name__ == "__main__":
    n = int(input("Enter the N Value : "))
    n_queens_problem = NQueensProblem(n)
    solution = a_star_search(n_queens_problem)
    print("Solution :", solution)
