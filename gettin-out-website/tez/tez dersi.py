import networkx as nx

# Örnek bir graf oluşturalım
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Tüm düğümleri içeren en kısa döngüyü bulmak için nx.cycle_basis() fonksiyonunu kullanabiliriz
cycles = nx.cycle_basis(G)

# En kısa döngünün uzunluğunu bulalım
min_cycle_length = min([len(cycle) for cycle in cycles])

print("Tüm düğümleri içeren en kısa döngü uzunluğu:", min_cycle_length)

