import matplotlib.pyplot as plt

def oklid_uzaklik(nokta1, nokta2):
    return ((nokta2[0] - nokta1[0])**2 + (nokta2[1] - nokta1[1])**2)**0.5

def taksimetrik_uzaklik(nokta1, nokta2):
    return abs(nokta2[0] - nokta1[0]) + abs(nokta2[1] - nokta1[1])

def nokta_girisi_al():
    try:
        x = float(input("X koordinatını girin: "))
        y = float(input("Y koordinatını girin: "))
        return x, y
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal değerler girin.")
        return None

# İlk noktayı al
nokta_a = nokta_girisi_al()
if nokta_a is not None:
    # İkinci noktayı al
    nokta_b = nokta_girisi_al()
    if nokta_b is not None:
        # Noktaları çiz
        plt.plot([nokta_a[0], nokta_b[0]], [nokta_a[1], nokta_b[1]], 'ro-')

        # Öklidyen uzaklığı hesapla
        oklid_mesafe = oklid_uzaklik(nokta_a, nokta_b)
        print(f"Öklidyen Uzaklık: {oklid_mesafe:.2f}")

        # Taksimetrik uzaklığı hesapla
        taksimetrik_mesafe = taksimetrik_uzaklik(nokta_a, nokta_b)
        print(f"Taksimetrik Uzaklık: {taksimetrik_mesafe:.2f}")

        # Grafiği göster
        plt.xlabel('X Ekseni')
        plt.ylabel('Y Ekseni')
        plt.title('Noktalar ve Uzaklıklar')
        plt.grid(True)
        plt.show()
