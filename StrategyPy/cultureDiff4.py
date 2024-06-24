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
        G.add_edge(culture, country, color='blue')  # Default color for normal relationships

# Add edges between cultural groups with specified colors for friendly or hostile
cultural_connections = [
    ("English", "EU", 'green'),        # Friendly
    ("EU", "Chinese", 'red'),          # Hostile
    ("Chinese", "ASEAN", 'green'),     # Friendly
    ("ASEAN", "India", 'green'),       # Friendly
    ("Spanish", "Portugal", 'green'),  # Friendly
    ("Arabic", "Africa", 'red')        # Hostile
]

for source, target, color in cultural_connections:
    G.add_edge(source, target, color=color)

# Draw the graph with colored edges
pos = nx.spring_layout(G, seed=42)
edges = G.edges(data=True)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1000)
nx.draw_networkx_labels(G, pos, font_size=8)
nx.draw_networkx_edges(G, pos, edgelist=[(u,v) for u,v,d in edges if d['color'] == 'green'], edge_color='green')
nx.draw_networkx_edges(G, pos, edgelist=[(u,v) for u,v,d in edges if d['color'] == 'red'], edge_color='red')
plt.title("World Cultural Regions")
plt.show()
