from collections import deque

def bipartition(graph):
    """Return (left_set, right_set) if bipartite; else None.

    Use BFS coloring over all components.
    """

    color = {}  # node -> 0 or 1

    for start in graph:

        # If not colored, start BFS from it
        if start not in color:
            color[start] = 0
            queue = deque([start])

            while queue:
                u = queue.popleft()

                for v in graph[u]:
                    # If uncolored, give opposite color
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)

                    # If same color neighbor → not bipartite
                    elif color[v] == color[u]:
                        return None

    # Build sets
    left = {node for node in color if color[node] == 0}
    right = {node for node in color if color[node] == 1}

    return (left, right)
