import networkx as nx
import matplotlib.pyplot as plt

import us_states_graph


def show_graph(graph):
    pos = nx.get_node_attributes(graph, "pos")
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

    plt.show()


def show_main_characteristics(graph):
    print("Number of nodes:", graph.number_of_nodes())
    print("Number of edges:", graph.number_of_edges())
    print("Density:", nx.density(graph))
    print("Center:", nx.center(graph))
    print("Periphery:", nx.periphery(graph))


def main():
    # Create the graph
    highway_graph = us_states_graph.create_graph()

    # Show the main characteristics of the graph
    show_main_characteristics(highway_graph)

    # Display the graph
    show_graph(highway_graph)


if __name__ == "__main__":
    main()
