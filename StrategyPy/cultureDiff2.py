import networkx as nx
import matplotlib.pyplot as plt

# 空の無向グラフを作成
G = nx.Graph()

# 文化圏ごとにノードを追加
cultures = {
    "English": ["United States", "United Kingdom",  "Canada", "Australia", "New Zealand"],
    "EU": ["France", "Germany", "Italy", "Spain", "Netherlands", "Sweden", "Poland", "Belgium"],
    "Chinese": ["China", "Hong Kong", "Macau", "Taiwan"],
    "Spanish": ["Mexico", "Argentina"],
    "Portugal": ["Brazil"],
    "Arabic": ["Saudi Arabia", "United Arab Emirates", "North Africa"],
    "ASEAN": ["Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand", "Brunei", "Vietnam", "Laos", "Myanmar", "Cambodia"],
    "India":["India"],
    "Africa":["South Africa"],
    "Russia":["Russia", "Belarus", "Central Asia"],
    "Japan":["Japan"],
    "South Korea":["South Korea"],
    "Third party":["North Korea", "Pakistan"]
}


# 文化圏のノードを追加
for culture, countries in cultures.items():
    G.add_node(culture)
    for country in countries:
        G.add_edge(culture, country)

# グラフを描画
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=8)
plt.title("World Cultural Regions")
plt.show()