import networkx as nx
import matplotlib.pyplot as plt

def taksimetrik_graf_ciz(dugum_sayisi):
    # Taksimetrik graf oluştur (her düğüm birbirine bağlı)
    G = nx.complete_graph(dugum_sayisi)

    # Grafı çiz
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', edge_color='gray', alpha=0.7)

    # Çap uzunluklarını grafiğin üzerine yazdır
    for edge in G.edges():
        x, y = pos[edge[0]], pos[edge[1]]
        length = 1  # Çap uzunluğu her zaman 1'dir
        plt.text((x[0] + y[0]) / 2, (x[1] + y[1]) / 2, f"{length:.2f}", color='red', fontsize=8, ha='center')

    # Çapı ekrana yazdır (1 olacaktır)
    plt.title(f"Taksimetrik Grafin Çapı: {nx.diameter(G)}")
    plt.show()

# Kullanıcıdan grafın düğüm sayısını al
dugum_sayisi = int(input("Grafın düğüm sayısını girin: "))

# Taksimetrik grafi çiz
taksimetrik_graf_ciz(dugum_sayisi)
