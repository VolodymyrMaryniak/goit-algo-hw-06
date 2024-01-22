import networkx as nx
from collections import deque
import typing

import us_states_graph


def dfs_recursive(
    graph: nx.Graph,
    vertex: str,
    visit_callback: typing.Callable[[str], None] = None,
    visited: set = None,
):
    if visited is None:
        visited = set()

    visited.add(vertex)

    # Visit the vertex
    if visit_callback is not None:
        visit_callback(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visit_callback, visited)


def bfs_recursive(
    graph: nx.Graph,
    queue: typing.Deque,
    visit_callback: typing.Callable[[str], None] = None,
    visited: set = None,
):
    if visited is None:
        visited = set()

    if not queue:
        return

    vertex = queue.popleft()
    if vertex not in visited:
        # Visit the vertex
        if visit_callback is not None:
            visit_callback(vertex)

        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)

    bfs_recursive(graph, queue, visit_callback, visited)


def main():
    highway_graph = us_states_graph.create_graph()
    print("DFS:")
    dfs_recursive(
        highway_graph, "FL", visit_callback=lambda vertex: print(vertex, end=" ")
    )

    print("\nBFS:")
    bfs_recursive(
        highway_graph,
        deque(["FL"]),
        visit_callback=lambda vertex: print(vertex, end=" "),
    )


if __name__ == "__main__":
    main()
