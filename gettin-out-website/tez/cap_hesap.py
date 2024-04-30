import itertools
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cap_hesapla(kume):
    # Graf oluştur
    G = nx.Graph()

    # Küme elemanlarını graf düğümleri olarak ekle
    for eleman in kume:
        G.add_node(eleman, weight=0)  # Her düğüme 'weight' özniteliği ekleniyor

    # Her bir düğüm çifti arasına mesafeleri ekleyerek grafı oluştur
    for a, b in itertools.combinations(kume, 2):
        mesafe = abs(a - b)
        G.add_edge(a, b, weight=mesafe)

    try:
        # Grafın çapını hesapla
        cap = nx.diameter(G, weight='weight')

        # Çap uzunluklarını belirli bir ölçeğe göre ayarla
        scale_factor = 10.0  # Ayarlamak için kullanılacak ölçek faktörü
        edge_lengths = [G[a][b]['weight'] * scale_factor for a, b in G.edges()]

        # 3D grafik oluştur
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Düğümleri 3D'de yerleştirme
        pos = nx.spring_layout(G, dim=3)

        # Çap uzunluklarını çizgilerle birleştirme ve üzerlerine yazdırma
        for (a, b), length in zip(G.edges(), edge_lengths):
            x_values = [pos[a][0], pos[b][0]]
            y_values = [pos[a][1], pos[b][1]]
            z_values = [pos[a][2], pos[b][2]]
            ax.plot(x_values, y_values, z_values, linewidth=2, label=f"{length:.2f}")
            mid_x = (pos[a][0] + pos[b][0]) / 2
            mid_y = (pos[a][1] + pos[b][1]) / 2
            mid_z = (pos[a][2] + pos[b][2]) / 2
            ax.text(mid_x, mid_y, mid_z, f"{length:.2f}", color='red', fontsize=8, ha='right')

        # Düğümleri 3D'de çiz ve üzerlerine değerlerini yaz
        for node, (x, y, z) in pos.items():
            ax.scatter(x, y, z, label=str(node), color='skyblue', s=700)
            ax.text(x, y, z, f"{node}({G.nodes[node]['weight']:.2f})", color='black', fontsize=8, ha='right')

        # Çapı ve küme elemanlarını ekrana yazdır
        plt.title(f"Kümenin Çapı: {cap}\nElemanlar: {kume}")
        plt.legend()
        plt.show()
    except nx.NetworkXError:
        print("Çap hesaplanamadı.")

# Kullanıcıdan küme elemanlarını al
kume_elemanlari = input("Virgülle ayrılmış küme elemanlarını girin: ")

# Girilen elemanları virgülle ayırarak bir küme oluştur
kume = set(map(int, kume_elemanlari.split(',')))

# Çapı hesapla ve 3D grafı çizdir
cap_hesapla(kume)


















