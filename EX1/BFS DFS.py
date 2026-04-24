import heapq
from collections import deque
from newc import Graph
from pri import PriorityQueue
def uniform_cost_search(self, start, goal_node=None):
    if start not in self.graph:
        print(f"Start node '{start}' not reached in the graph.")
        return "failure"

    node = {"state": start, "path_cost": 0, "parent": None}
    frontier = PriorityQueue()
    frontier.insert(node, node["path_cost"])
    explored, explored_list, s_no = set(), [], 0

    print("\nUniform Cost Search (UCS) Traversal:")
    self._print_table_header("Fringe (Priority Queue)")

    fringe_for_print = [(n["path_cost"], n["state"]) for _, _, n in frontier.elements]
    self._print_table_row(s_no, fringe_for_print, explored_list)from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
            print("Node added")
        else:
            print("Node already exists")

    def add_edge(self, u, v, cost=0):
        if u in self.graph and v in self.graph:
            if (v, cost) in self.graph[u]:
                print("Edge already exists")
            else:
                self.graph[u].append((v, cost))
                self.graph[v].append((u, cost))
                print("Edge added")
        else:
            print("Add nodes first")

    def delete_node(self, node):
        if node in self.graph:
            self.graph.pop(node)
            for n in self.graph:
                self.graph[n] = [(x, c) for x, c in self.graph[n] if x != node]
            print("Node deleted")
        else:
            print("Node not found")

    def delete_edge(self, u, v):
        if u in self.graph:
            initial_count = len(self.graph[u])
            self.graph[u] = [(x, c) for x, c in self.graph[u] if x != v]
            self.graph[v] = [(x, c) for x, c in self.graph[v] if x != u]
            if len(self.graph[u]) < initial_count:
                print("Edge deleted")
            else:
                print("Edge not found")
        else:
            print("Edge not found")

    def display(self):
        print("\nGraph:")
        for node in self.graph:
            print(node, "-", self.graph[node])

    def display_adj_list(self, node):
        if node in self.graph:
            print(node, "-", self.graph[node])
        else:
            print("Node not found")

    # Define some default minimum widths for better alignment
    S_NO_WIDTH = 5
    FRINGE_MIN_WIDTH = 50
    EXPLORED_MIN_WIDTH = 50

    def _print_table_header(self, fringe_label="Fringe"):
        # The header will use the minimum widths
        header_str = (f"{'S.No':<{self.S_NO_WIDTH}} | "
                      f"{fringe_label:<{self.FRINGE_MIN_WIDTH}} | "
                      f"{'Explored Set':<{self.EXPLORED_MIN_WIDTH}}")
        print(header_str)
        # Print a separator line that's sufficiently long
        print("-" * (self.S_NO_WIDTH + self.FRINGE_MIN_WIDTH + self.EXPLORED_MIN_WIDTH + 6)) # 6 for separators


    def _print_table_row(self, s_no, fringe, explored_list):
        s_no_str = f"{s_no:<{self.S_NO_WIDTH}}"

        # Convert fringe to string
        fringe_content = str(list(fringe))

        # Convert explored_list to string
        explored_content = str(explored_list)

        # Determine actual width needed for fringe and explored, taking minimums into account
        fringe_width = max(len(fringe_content), self.FRINGE_MIN_WIDTH)
        explored_width = max(len(explored_content), self.EXPLORED_MIN_WIDTH)

        # Print the row with dynamic padding based on actual content length
        print(f"{s_no_str} | {fringe_content:<{fringe_width}} | {explored_content:<{explored_width}}")


    def bfs_lr(self, start, goal_node=None):
        if start not in self.graph:
            print(f"Start node '{start}' not found in the graph.")
            return

        fringe = deque([start])
        visited = {start}
        explored_list = []

        s_no = 0
        path_found = False

        print("\nBFS (L-R) Traversal:")
        self._print_table_header("Fringe (Queue)")
        self._print_table_row(s_no, fringe, explored_list) # Initial state

        while fringe:
            s_no += 1
            current_node = fringe.popleft()

            explored_list.append(current_node)

            if current_node == goal_node:
                path_found = True
                self._print_table_row(s_no, fringe, explored_list)
                break

            for neighbor, _ in self.graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    fringe.append(neighbor)
            self._print_table_row(s_no, fringe, explored_list)

        print("-" * (self.S_NO_WIDTH + self.FRINGE_MIN_WIDTH + self.EXPLORED_MIN_WIDTH + 6)) # Consistent separator
        if path_found:
            print(f"\nTraversal finished. Goal node '{goal_node}' reached!")
        elif goal_node:
            print(f"\nTraversal finished. Goal node '{goal_node}' not found in the graph.")
        else:
            print("\nTraversal finished.")


    def bfs_rl(self, start, goal_node=None):
        if start not in self.graph:
            print(f"Start node '{start}' not found in the graph.")
            return

        fringe = deque([start])
        visited = {start}
        explored_list = []

        s_no = 0
        path_found = False

        print("\nBFS (R-L) Traversal:")
        self._print_table_header("Fringe (Queue)")
        self._print_table_row(s_no, fringe, explored_list) # Initial state

        while fringe:
            s_no += 1
            current_node = fringe.popleft()

            explored_list.append(current_node)

            if current_node == goal_node:
                path_found = True
                self._print_table_row(s_no, fringe, explored_list)
                break

            for neighbor, _ in reversed(self.graph[current_node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    fringe.append(neighbor)
            self._print_table_row(s_no, fringe, explored_list)

        print("-" * (self.S_NO_WIDTH + self.FRINGE_MIN_WIDTH + self.EXPLORED_MIN_WIDTH + 6))
        if path_found:
            print(f"\nTraversal finished. Goal node '{goal_node}' reached!")
        elif goal_node:
            print(f"\nTraversal finished. Goal node '{goal_node}' not found in the graph.")
        else:
            print("\nTraversal finished.")

    def dfs_lr(self, start, goal_node=None):
        if start not in self.graph:
            print(f"Start node '{start}' not found in the graph.")
            return

        fringe = [start]  # Stack for DFS
        visited = {start}
        explored_list = []

        s_no = 0
        path_found = False

        print("\nDFS (L-R) Traversal:")
        self._print_table_header("Fringe (Stack)")
        self._print_table_row(s_no, fringe, explored_list) # Initial state

        while fringe:
            s_no += 1
            current_node_state = fringe.pop()

            explored_list.append(current_node_state)

            if current_node_state == goal_node:
                path_found = True
                self._print_table_row(s_no, fringe, explored_list)
                break

            for neighbor_state, _ in reversed(self.graph[current_node_state]):
                if neighbor_state not in visited:
                    visited.add(neighbor_state)
                    fringe.append(neighbor_state)
            self._print_table_row(s_no, fringe, explored_list)

        print("-" * (self.S_NO_WIDTH + self.FRINGE_MIN_WIDTH + self.EXPLORED_MIN_WIDTH + 6))
        if path_found:
            print(f"\nTraversal finished. Goal node '{goal_node}' reached!")
        elif goal_node:
            print(f"\nTraversal finished. Goal node '{goal_node}' not found in the graph.")
        else:
            print("\nTraversal finished.")

    def dfs_rl(self, start, goal_node=None):
        if start not in self.graph:
            print(f"Start node '{start}' not found in the graph.")
            return

        fringe = [start]  # Stack for DFS
        visited = {start}
        explored_list = []

        s_no = 0
        path_found = False

        print("\nDFS (R-L) Traversal:")
        self._print_table_header("Fringe (Stack)")
        self._print_table_row(s_no, fringe, explored_list) # Initial state

        while fringe:
            s_no += 1
            current_node_state = fringe.pop()

            explored_list.append(current_node_state)

            if current_node_state == goal_node:
                path_found = True
                self._print_table_row(s_no, fringe, explored_list)
                break

            for neighbor_state, _ in self.graph[current_node_state]:
                if neighbor_state not in visited:
                    visited.add(neighbor_state)
                    fringe.append(neighbor_state)
            self._print_table_row(s_no, fringe, explored_list)

        print("-" * (self.S_NO_WIDTH + self.FRINGE_MIN_WIDTH + self.EXPLORED_MIN_WIDTH + 6))
        if path_found:
            print(f"\nTraversal finished. Goal node '{goal_node}' reached!")
        elif goal_node:
            print(f"\nTraversal finished. Goal node '{goal_node}' not found in the graph.")
        else:
            print("\nTraversal finished.")

# Existing menu and main loop remain the same
g = Graph()
while True:
    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 11.")
        continue # Skip the rest of the loop and re-display menu
    if ch == 1:
        g.add_node(input("Node: "))
    elif ch == 2:
        u = input("From: ")
        v = input("To: ")
       # cost = int(input("Cost (0 if none): "))
        g.add_edge(u, v, cost=0)
    elif ch == 3:
        node_to_delete = input("Node: ")
        g.delete_node(node_to_delete)
    elif ch == 4:
        u = input("From: ")
        v = input("To: ")
        g.delete_edge(u, v)
    elif ch == 5:
        g.display()
    elif ch == 6:
        g.display_adj_list(input("Node: "))
    elif ch == 7:
        start_node = input("Start node: ")
        goal_input = input("Enter goal node : ")
        goal_node = goal_input if goal_input else None
        g.bfs_lr(start_node, goal_node)
    elif ch == 8:
        start_node = input("Start node: ")
        goal_input = input("Enter goal node : ")
        goal_node = goal_input if goal_input else None
        g.bfs_rl(start_node, goal_node)
    elif ch == 9:
        start_node = input("Start node: ")
        goal_input = input("Enter goal node : ")
        goal_node = goal_input if goal_input else None
        g.dfs_lr(start_node, goal_node)
    elif ch == 10:
        start_node = input("Start node: ")
        goal_input = input("Enter goal node  ")
        goal_node = goal_input if goal_input else None
        g.dfs_rl(start_node, goal_node)
    elif ch == 11:
        print("Program terminated")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 11.")
