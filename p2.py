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
    start_state = tuple(
        range(problem.n)
    )  # Initial state (all queens in different rows)
    open_set = [(problem.heuristic(start_state), start_state)]  # Priority queue
    closed_set = set()

    while open_set:
        _, current_state = open_set.pop(0)  # Get state with lowest f(n) value
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


# Example usage
if __name__ == "__main__":
    n = int(input("Enter the N Value : "))  # Change this to the desired board size
    n_queens_problem = NQueensProblem(n)
    solution = a_star_search(n_queens_problem)
    print("Solution:", solution)
