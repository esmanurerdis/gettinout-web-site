import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def en_kucuk_taksimetrik_cember(noktalar):
    # Noktaların konveks kabuğunu al
    konveks_kabuk = ConvexHull(noktalar)

    # Konveks kabuğun merkezi
    merkez = np.mean(noktalar[konveks_kabuk.vertices], axis=0)

    # En uzak noktanın merkeze olan taksimetrik uzaklığı, taksimetrik çemberin yarıçapıdır
    yaricap = np.max(np.sum(np.abs(noktalar[konveks_kabuk.vertices] - merkez), axis=1))

    return merkez, yaricap

def plot_cember_ve_noktalar(noktalar, merkez, yaricap):
    fig, ax = plt.subplots()

    # Noktaları çiz
    ax.plot(noktalar[:, 0], noktalar[:, 1], 'o', label='Noktalar')

    # En küçük taksimetrik çemberi çiz
    circle = plt.Circle(merkez, yaricap, edgecolor='r', facecolor='none', label='Taksimetrik Çember')
    ax.add_patch(circle)

    # Merkezi işaretle
    ax.plot(merkez[0], merkez[1], 'rx', label='Merkez')

    # Merkez ve yarıçap bilgilerini göster
    ax.annotate(f'Merkez: {merkez}\nYarıçap: {yaricap:.4f}', xy=(0.05, 0.85), xycoords='axes fraction',
                bbox=dict(boxstyle="round,pad=0.3", edgecolor="w", facecolor="w"))

    plt.axis('equal')
    plt.legend()
    plt.show()

# Kullanıcıdan nokta sayısını al
nokta_sayisi = int(input("Nokta sayısını girin: "))

# Kullanıcıdan nokta koordinatlarını al
noktalar = []
for i in range(nokta_sayisi):
    x = float(input(f"Nokta {i+1} x koordinatını girin: "))
    y = float(input(f"Nokta {i+1} y koordinatını girin: "))
    noktalar.append([x, y])

noktalar = np.array(noktalar)

# En küçük taksimetrik çemberi bul
merkez, yaricap = en_kucuk_taksimetrik_cember(noktalar)

print("Merkez:", merkez)
print("Yarıçap:", yaricap)

# Çembreyi ve noktaları çiz
plot_cember_ve_noktalar(noktalar, merkez, yaricap)

