import networkx as nx
import matplotlib.pyplot as plt

import us_states_graph


def main():
    highway_graph = us_states_graph.create_graph()

    for start in highway_graph.nodes():
        results = dijkstra(highway_graph, start)
        for end, (distance, path) in results.items():
            print(f"{start} -> {end}: {path} ({distance})")

    show_graph(highway_graph)


def dijkstra(graph: nx.Graph, start):
    distances = {node: float("infinity") for node in graph.nodes()}
    distances[start] = 0
    predecessors = {node: None for node in graph.nodes()}
    unvisited = list(graph.nodes())

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])

        if distances[current_node] == float("infinity"):
            break

        neighbors = graph.neighbors(current_node)
        for neighbor in neighbors:
            weight = graph[current_node][neighbor]["weight"]
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node

        unvisited.remove(current_node)

    result = {
        node: (distances[node], get_shortest_path(predecessors, node))
        for node in graph.nodes()
    }
    return result


def get_shortest_path(predecessors, end):
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    return path


def show_graph(graph):
    pos = nx.get_node_attributes(graph, "pos")
    edge_labels = nx.get_edge_attributes(graph, "weight")

    nx.draw(
        graph,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=700,
        node_color="skyblue",
        font_size=8,
        edge_color="gray",
    )

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.show()


if __name__ == "__main__":
    main()
