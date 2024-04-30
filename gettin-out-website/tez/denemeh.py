import matplotlib.pyplot as plt
from itertools import combinations

def vektor_hesapla(nokta1, nokta2):
    return (nokta2[0] - nokta1[0], nokta2[1] - nokta1[1])

def vektor_uzunluk(vektor):
    return (vektor[0]**2 + vektor[1]**2)**0.5

def ciz_nokta_vektorleri_ve_uzunluklar(nokta_kumesi):
    fig, ax = plt.subplots()

    # Noktaları çiz
    for nokta in nokta_kumesi:
        ax.plot(nokta[0], nokta[1], 'bo')  # Mavi renkte nokta

    # Vektörleri çiz ve uzunlukları yaz
    for nokta1, nokta2 in combinations(nokta_kumesi, 2):
        vektor = vektor_hesapla(nokta1, nokta2)
        uzunluk = vektor_uzunluk(vektor)
        ax.arrow(nokta1[0], nokta1[1], vektor[0], vektor[1], head_width=0.2, head_length=0.2, fc='red', ec='red')
        ax.text(nokta1[0] + vektor[0]/2, nokta1[1] + vektor[1]/2, f'{uzunluk:.2f}', color='black', fontsize=8)

    # Çapı hesapla ve yaz
    cap = max(vektor_uzunluk(vektor_hesapla(nokta1, nokta2)) for nokta1, nokta2 in combinations(nokta_kumesi, 2))
    ax.text(0.5, 0.5, f'Çap: {cap:.2f}', color='green', fontsize=12, transform=ax.transAxes)

    plt.xlabel('X Ekseni')
    plt.ylabel('Y Ekseni')
    plt.title('Üç Nokta ve Vektörler')
    plt.grid(True)
    plt.show()

# Örnek kullanım:
ornek_nokta_kumesi = [(0, 0), (1, 0), (2, 1),(0,2)]
ciz_nokta_vektorleri_ve_uzunluklar(ornek_nokta_kumesi)