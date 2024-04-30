import networkx as nx
import matplotlib.pyplot as plt

# Kullanıcıdan düğüm ve kenarları alalım
düğüm_sayısı = int(input("Graf için düğüm sayısını girin: "))
kenar_sayısı = int(input("Graf için kenar sayısını girin: "))

# Boş bir graf oluşturalım
G = nx.Graph()

# Kullanıcıdan kenarları alalım ve grafa ekleyelim
for _ in range(kenar_sayısı):
    düğümler = input("Kenarı girin (örn. '1 2' şeklinde): ").split()
    düğüm1, düğüm2 = int(düğümler[0]), int(düğümler[1])
    G.add_edge(düğüm1, düğüm2)

# Grafiği çizdirelim
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold', width=2, edge_color='gray')
plt.title("Kullanıcıdan Alınan Graf")
plt.show()

