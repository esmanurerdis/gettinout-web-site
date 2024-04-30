import networkx as nx
import matplotlib.pyplot as plt

# Örnek bir graf oluşturalım
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (3, 5)])

# Grafiği çizdirelim
pos = nx.spring_layout(G)  # Grafı düzgün bir şekilde yerleştirmek için pozisyonları hesaplayalım
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold', width=2, edge_color='gray')
plt.title("Örnek Graf")
plt.show()
