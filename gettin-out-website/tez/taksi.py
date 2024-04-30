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
    return max(abs(vektor[0]), abs(vektor[1]))

def uzaklik_hesapla(nokta1, nokta2, uzaklik_turu):
    if uzaklik_turu == "öklidyen":
        # Öklidyen uzaklık
        return ((nokta2[0] - nokta1[0])**2 + (nokta2[1] - nokta1[1])**2)**0.5
    elif uzaklik_turu == "taksimetrik":
        # Taksimetrik uzaklık
        return vektor_uzunluk(vektor_hesapla(nokta1, nokta2))
    else:
        print("Geçersiz uzaklık türü.")
        return None

def kullanıcıdan_noktalar_al():
    nokta_kumesi = []
    for i in range(3):
        nokta_str = input(f"Nokta {i+1} Koordinatlarını (x, y) şeklinde girin: ")
        nokta = parse_nokta(nokta_str)

        if nokta is not None:
            nokta_kumesi.append(nokta)

    return nokta_kumesi

def ciz_nokta_vektorleri_ve_uzakliklar(nokta_kumesi, uzaklik_turu):
    fig, ax = plt.subplots()

    # Noktaları çiz
    for nokta in nokta_kumesi:
        ax.plot(nokta[0], nokta[1], 'bo')  # Mavi renkte nokta

    # Vektörleri çiz ve uzunlukları yaz
    for nokta1, nokta2 in combinations(nokta_kumesi, 2):
        vektor = vektor_hesapla(nokta1, nokta2)
        uzunluk_euclidean = uzaklik_hesapla(nokta1, nokta2, "öklidyen")
        uzunluk_chebyshev = uzaklik_hesapla(nokta1, nokta2, "taksimetrik")
        
        # Öklidyen uzaklık için çizim
        ax.arrow(nokta1[0], nokta1[1], vektor[0], vektor[1], head_width=0.2, head_length=0.2, color='blue')
        ax.text(nokta1[0] + vektor[0]/2, nokta1[1] + vektor[1]/2, f'{uzunluk_euclidean:.2f}', color='black', fontsize=8)

        # Taksimetrik uzaklık için çizim
        ax.arrow(nokta1[0] + 0.2, nokta1[1], vektor[0], vektor[1], head_width=0.2, head_length=0.2, color='green')
        ax.text(nokta1[0] + vektor[0]/2 + 0.2, nokta1[1] + vektor[1]/2 - 0.5, f'{uzunluk_chebyshev:.2f}', color='black', fontsize=8)

    # Başlıkları ekle
    ax.text(0.5, 1.1, 'Öklidyen Uzaklık (Mavi)', color='blue', fontsize=12, transform=ax.transAxes, ha='center')
    ax.text(0.5, 1.05, 'Taksimetrik Uzaklık (Yeşil)', color='green', fontsize=12, transform=ax.transAxes, ha='center')

    plt.xlabel('X Ekseni')
    plt.ylabel('Y Ekseni')
    plt.title('Üç Nokta ve Vektörler')
    plt.grid(True)
    plt.show()

# Kullanıcıdan nokta girişi al
kullanicidan_alinan_noktalar = kullanıcıdan_noktalar_al()

# Çizimi yap
ciz_nokta_vektorleri_ve_uzakliklar(kullanicidan_alinan_noktalar, "öklidyen")





