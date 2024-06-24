import networkx as nx
import matplotlib.pyplot as plt

# Create an empty undirected graph
G = nx.Graph()

# Add nodes for each cultural region
cultures = {
    "English": ["United States", "United Kingdom", "Canada", "Australia", "New Zealand"],
    "EU": ["France", "Germany", "Italy", "Spain", "Netherlands", "Sweden", "Poland", "Belgium"],
    "Chinese": ["China", "Hong Kong", "Macau", "Taiwan"],
    "Spanish": ["Mexico", "Argentina"],
    "Portugal": ["Brazil"],
    "Arabic": ["Saudi Arabia", "United Arab Emirates"],
    "ASEAN": ["Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand", "Brunei", "Vietnam", "Laos", "Myanmar", "Cambodia"],
    "India":["India"],
    "Africa":["South Africa"],
    "Russia":["Russia", "Belarus"],
    "Japan":["Japan"],
    "South Korea":["South Korea"],
    "Third party":["North Korea", "Pakistan"]
}

# Add nodes and edges for cultural regions
for culture, countries in cultures.items():
    G.add_node(culture)
    for country in countries:
        G.add_edge(culture, country)

# Add edges between cultural groups
cultural_connections = [
    ("English", "EU"),
    ("Chinese", "ASEAN"),
    ("ASEAN", "India"),
    ("Spanish", "Portugal"),
    ("Arabic", "Africa")
]

for connection in cultural_connections:
    G.add_edge(*connection)

# Draw the graph
pos = nx.spring_layout(G, seed=42)  # This lays out the nodes using the Fruchterman-Reingold force-directed algorithm.
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=8)
plt.title("World Cultural Regions")
plt.show()
