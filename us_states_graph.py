import networkx as nx
from math import radians, sin, cos, sqrt, atan2


def create_graph() -> nx.Graph:
    # State abbreviations and their coordinates
    state_coordinates = {
        "WA": (47.6062, -122.3321),  # Washington
        "MT": (46.8797, -110.3626),  # Montana
        "MN": (46.7296, -94.6859),  # Minnesota
        "NY": (40.7128, -74.0060),  # New York
        "NV": (36.1699, -115.1398),  # Nevada
        "CA": (36.7783, -119.4179),  # California
        "AZ": (34.0489, -111.0937),  # Arizona
        "TX": (31.9686, -99.9018),  # Texas
        "FL": (27.9944, -81.7603),  # Florida
        "GA": (32.1656, -82.9001),  # Georgia
        "NC": (35.7596, -79.0193),  # North Carolina
        "MO": (38.5739, -92.6032),  # Missouri
        "KS": (39.0119, -98.4842),  # Kansas
        "CO": (39.5501, -105.7821),  # Colorado
        "IA": (41.8780, -93.0977),  # Iowa
        "TN": (35.5175, -86.5804),  # Tennessee
        "MI": (44.3148, -85.6024),  # Michigan
        "OH": (40.4173, -82.9071),  # Ohio4
        "ID": (44.0682, -114.7420),  # Idaho
    }

    highway_graph = nx.Graph()

    for state, coordinates in state_coordinates.items():
        highway_graph.add_node(state, pos=(coordinates[1], coordinates[0]))

    edges = [
        ("WA", "MT"),
        ("MT", "NV"),
        ("MT", "MN"),
        ("TN", "NC"),
        ("NY", "NC"),
        ("CA", "AZ"),
        ("CA", "NV"),
        ("MT", "IA"),
        ("MT", "CO"),
        ("CO", "KS"),
        ("CO", "IA"),
        ("IA", "MO"),
        ("KS", "MO"),
        ("KS", "IA"),
        ("IA", "MN"),
        ("MO", "NC"),
        ("NC", "GA"),
        ("GA", "FL"),
        ("AZ", "TX"),
        ("TX", "CO"),
        ("TX", "KS"),
        ("TX", "MO"),
        ("TX", "GA"),
        ("WA", "CA"),
        ("NV", "CO"),
        ("AZ", "CO"),
        ("IA", "OH"),
        ("OH", "MI"),
        ("OH", "NY"),
        ("MO", "OH"),
        ("OH", "NC"),
        ("WA", "ID"),
        ("ID", "MT"),
        ("ID", "NV"),
        ("TX", "TN"),
        ("TN", "GA"),
    ]

    weighted_edges = [
        (
            e[0],
            e[1],
            {
                "weight": round(
                    haversine_distance(state_coordinates[e[0]], state_coordinates[e[1]])
                )
            },
        )
        for e in edges
    ]

    highway_graph.add_edges_from(weighted_edges)
    return highway_graph


def haversine_distance(coord1, coord2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Extract latitude and longitude from the coordinates
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    # Calculate the differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance
    distance = R * c

    return distance
