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
    self._print_table_row(s_no, fringe_for_print, explored_list)
    while True:
        if frontier.is_empty():
            print("-" * (self.S_NO_WIDTH + self.FRINGE_MIN_WIDTH + self.EXPLORED_MIN_WIDTH + 6))
            print(f"\nTraversal finished. Goal node '{goal_node}' not found.")
            return "failure"
        s_no += 1
        node = frontier.pop()
        if node["state"] not in explored: explored_list.append(node["state"])
        if node["state"] == goal_node:
            fringe_for_print = [(n["path_cost"], n["state"]) for _, _, n in frontier.elements]
            self._print_table_row(s_no, fringe_for_print, explored_list)
            print("-" * (self.S_NO_WIDTH + self.FRINGE_MIN_WIDTH + self.EXPLORED_MIN_WIDTH + 6))
            print(f"\nGoal reached! Path: {self._solution(node)} (Cost: {node['path_cost']})")
            return self._solution(node)
        explored.add(node["state"])
        for neighbor_state, action_cost in self.graph.get(node["state"], []):
            child = {"state": neighbor_state, "path_cost": node["path_cost"] + action_cost, "parent": node}
            if child["state"] not in explored and not frontier.contains_state(child["state"]):
                frontier.insert(child, child["path_cost"])
            elif frontier.contains_state(child["state"]):
                old_node = frontier.get_node(child["state"])
                if child["path_cost"] < old_node["path_cost"]:
                    frontier.replace(old_node, child)

        fringe_for_print = [(n["path_cost"], n["state"]) for _, _, n in frontier.elements]
        self._print_table_row(s_no, fringe_for_print, explored_list)

def _solution(self, node):
    path = []
    while node:
        path.append(node["state"])
        node = node["parent"]
    return '-'.join(reversed(path))
g = Graph()
while True:
    print("\nMENU")
    print("1 Add Node")
    print("2 Add Edge")
    print("3 Delete Node")
    print("4 Delete Edge")
    print("5 Display Graph")
    print("6 Display Adjacency List")
    print("7 Uniform Cost Search") # Only UCS option
    print("8 Exit") # Streamlined exit option

    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 8.")
        continue # Skip the rest of the loop and re-display menu

    if ch == 1:
        g.add_node(input("Node: "))
    elif ch == 2:
        u = input("From: ")
        v = input("To: ")
        cost_str = input("Cost (integer): ")
        try:
            cost = int(cost_str)
            g.add_edge(u, v, cost=cost)
        except ValueError:
            print("Invalid cost. Please enter an integer.")
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
    elif ch == 7: # UCS option
        start_node = input("Start node: ")
        goal_input = input("Enter goal node: ")
        goal_node = goal_input if goal_input else None
        g.uniform_cost_search(start_node, goal_node)
    elif ch == 8: # Exit option
        print("Program terminated")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")Enter choice: 1
