import matplotlib.pyplot as plt

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
    for i in range(4):
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
    for i in range(3):
        nokta1 = nokta_kumesi[i]
        nokta2 = nokta_kumesi[i + 1]
        vektor = vektor_hesapla(nokta1, nokta2)
        uzunluk = vektor_uzunluk(vektor)
        ax.quiver(nokta1[0], nokta1[1], vektor[0], vektor[1], angles='xy', scale_units='xy', scale=1, color='red', label=f'Uzunluk: {uzunluk:.2f}')

    # Çap ve uzaklıkları hesapla ve yaz
    cap = max(vektor_uzunluk(vektor_hesapla(nokta_kumesi[0], nokta_kumesi[1])),
              vektor_uzunluk(vektor_hesapla(nokta_kumesi[1], nokta_kumesi[2])),
              vektor_uzunluk(vektor_hesapla(nokta_kumesi[2], nokta_kumesi[3])))
    
    uzaklik1 = uzaklik_hesapla(nokta_kumesi[0], nokta_kumesi[2])
    uzaklik2 = uzaklik_hesapla(nokta_kumesi[1], nokta_kumesi[3])

    ax.text(0.5, 0.95, f'Çap: {cap:.2f}\nUzaklık1: {uzaklik1:.2f}\nUzaklık2: {uzaklik2:.2f}', color='green', fontsize=12, transform=ax.transAxes)

    ax.set_xlabel('X Ekseni')
    ax.set_ylabel('Y Ekseni')
    ax.set_title('Dört Nokta ve Vektörler')
    ax.legend()
    plt.grid(True)
    plt.show()

# Kullanıcıdan nokta girişi al
kullanicidan_alinan_noktalar = kullanıcıdan_noktalar_al()

# Fonksiyonu kullanarak grafiği çiz
ciz_nokta_vektorleri_ve_uzakliklar(kullanicidan_alinan_noktalar)
