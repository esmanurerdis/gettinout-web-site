import matplotlib.pyplot as plt
from itertools import combinations

def parse_nokta(nokta_str):
    try:
        x, y = map(float, nokta_str.split(','))
        return x, y
    except ValueError:
        print("Geçersiz giriş. Lütfen noktayı doğru bir şekilde girin.")
        return None

def vektor_hesapla(nokta1, nokta2):
    return (nokta2[0] - nokta1[0], nokta2[1] - nokta1[1])

def vektor_uzunluk(vektor):
    return ((vektor[0])**2 + (vektor[1])**2)**0.5

def taksimetrik_uzaklik(nokta1, nokta2):
    return max(abs(nokta2[0] - nokta1[0]), abs(nokta2[1] - nokta1[1]))

def cap_ve_uzakliklari_hesapla(nokta_kumesi):
    max_euclidean_uzaklik = 0
    max_taksimetrik_uzaklik = 0

    for nokta1, nokta2 in combinations(nokta_kumesi, 2):
        vektor = vektor_hesapla(nokta1, nokta2)
        
        euclidean_uzaklik = vektor_uzunluk(vektor)
        taksimetrik_uzaklik_degeri = taksimetrik_uzaklik(nokta1, nokta2)

        if euclidean_uzaklik > max_euclidean_uzaklik:
            max_euclidean_uzaklik = euclidean_uzaklik

        if taksimetrik_uzaklik_degeri > max_taksimetrik_uzaklik:
            max_taksimetrik_uzaklik = taksimetrik_uzaklik_degeri

    return max_euclidean_uzaklik, max_taksimetrik_uzaklik

def kullanici_dan_noktalar_al():
    nokta_kumesi = []
    for i in range(3):
        nokta_str = input(f"Nokta {i+1} Koordinatlarını (x, y) şeklinde girin: ")
        nokta = parse_nokta(nokta_str)
        if nokta is not None:
            nokta_kumesi.append(nokta)
    return nokta_kumesi

def ciz_nokta_vektorleri_ve_uzakliklar(nokta_kumesi):
    fig, ax = plt.subplots()

    # Noktaları çiz
    for nokta in nokta_kumesi:
        ax.plot(nokta[0], nokta[1], 'bo')  # Mavi renkte nokta

    # Vektörleri çiz ve uzunlukları yaz
    for nokta1, nokta2 in combinations(nokta_kumesi, 2):
        vektor = vektor_hesapla(nokta1, nokta2)
        
        euclidean_uzaklik = vektor_uzunluk(vektor)
        taksimetrik_uzaklik_degeri = taksimetrik_uzaklik(nokta1, nokta2)

        # Öklidyen uzaklık için çizim
        ax.arrow(nokta1[0], nokta1[1], vektor[0], vektor[1], head_width=0.2, head_length=0.2, color='blue')
        ax.text(nokta1[0] + vektor[0]/2, nokta1[1] + vektor[1]/2, f'Euclidean: {euclidean_uzaklik:.2f}', color='black', fontsize=8)

        # Taksimetrik uzaklık için çizim
        ax.arrow(nokta1[0] + 0.2, nokta1[1], vektor[0], vektor[1], head_width=0.2, head_length=0.2, color='green')
        ax.text(nokta1[0] + vektor[0]/2 + 0.2, nokta1[1] + vektor[1]/2 - 0.5,
                f'Taksimetrik: {taksimetrik_uzaklik_degeri:.2f}', color='black', fontsize=8)

    # Çap ve uzaklıkları hesapla ve yaz
    max_euclidean_uzaklik, max_taksimetrik_uzaklik = cap_ve_uzakliklari_hesapla(nokta_kumesi)

    ax.text(0.5, 0.5, f'Max Euclidean: {max_euclidean_uzaklik:.2f}\nMax Taksimetrik: {max_taksimetrik_uzaklik:.2f}',
            color='black', fontsize=10, transform=ax.transAxes, ha='center', va='center')

    # Başlıkları ekle
    ax.text(0.5, 1.1, 'Uzaklıklar (Mavi: Euclidean, Yeşil: Taksimetrik)', color='black', fontsize=12, transform=ax.transAxes, ha='center')

    plt.xlabel('X Ekseni')
    plt.ylabel('Y Ekseni')
    plt.title('Üç Nokta ve Vektörler')
    plt.grid(True)
    plt.show()

# Kullanıcıdan nokta girişi al
kullanicidan_alinan_noktalar = kullanici_dan_noktalar_al()

# Çizimi yap
ciz_nokta_vektorleri_ve_uzakliklar(kullanicidan_alinan_noktalar)
