import networkx as nx

# 空の無向グラフを作成
G = nx.Graph()

# ノードを追加
G.add_node(1)
G.add_nodes_from([2, 3])

# エッジを追加
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 3)])

# ノードとエッジの数を取得
print("ノード数:", G.number_of_nodes())
print("エッジ数:", G.number_of_edges())

# ノードやエッジの情報を取得
print("ノード一覧:", G.nodes())
print("エッジ一覧:", G.edges())

# グラフを描画
import matplotlib.pyplot as plt
nx.draw(G, with_labels=True)
plt.show()