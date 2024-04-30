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
    return (vektor[0]**2 + vektor[1]**2)**0.5

def uzaklik_hesapla(nokta1, nokta2):
    return vektor_uzunluk(vektor_hesapla(nokta1, nokta2))

def kullanıcıdan_noktalar_al():
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
        uzunluk = vektor_uzunluk(vektor)
        ax.arrow(nokta1[0], nokta1[1], vektor[0], vektor[1], head_width=0.2, head_length=0.2, fc='red', ec='red')
        ax.text(nokta1[0] + vektor[0]/2, nokta1[1] + vektor[1]/2, f'{uzunluk:.2f}', color='black', fontsize=8)

    # Çapı ve uzaklığı hesapla ve yaz
    cap = max(vektor_uzunluk(vektor_hesapla(nokta1, nokta2)) for nokta1, nokta2 in combinations(nokta_kumesi, 2))
    
    # Dört nokta arasındaki uzaklığı hesapla
    uzaklik = uzaklik_hesapla(nokta_kumesi[0], nokta_kumesi[2])

    ax.text(0.5, 0.5, f'Çap: {cap:.2f}\nUzaklık: {uzaklik:.2f}', color='green', fontsize=12, transform=ax.transAxes)

    plt.xlabel('X Ekseni')
    plt.ylabel('Y Ekseni')
    plt.title('Üç Nokta ve Vektörler')
    plt.grid(True)
    plt.show()

# Kullanıcıdan nokta girişi al
kullanicidan_alinan_noktalar = kullanıcıdan_noktalar_al()

# Fonksiyonu kullanarak grafiği çiz
ciz_nokta_vektorleri_ve_uzakliklar(kullanicidan_alinan_noktalar)
