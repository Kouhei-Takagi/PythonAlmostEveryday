import networkx as nx
import matplotlib.pyplot as plt

# Create an empty undirected graph
G = nx.Graph()

# Define nodes and edges for each cultural region
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
        G.add_edge(culture, country, color='blue')  # Default blue color for normal relationships

# Define friendly and hostile connections with color coding
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

# Graph layout settings
pos = nx.spring_layout(G, seed=42)  # For consistent layout
plt.figure(figsize=(14, 10))  # Increase the size of the figure to improve readability

# Draw nodes and labels
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=5000)
nx.draw_networkx_labels(G, pos, font_size=12)

# Draw edges with color coding
for edge in G.edges(data=True):
    nx.draw_networkx_edges(G, pos, edgelist=[(edge[0], edge[1])], edge_color=edge[2]['color'], width=2)

plt.title("World Cultural Regions with Relationships")
plt.axis('off')  # Turn off the axis
plt.show()