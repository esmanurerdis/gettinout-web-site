import matplotlib.pyplot as plt
import math

def taxicab_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def taxicab_diameter(x_coords, y_coords):
    n = len(x_coords)
    max_distance = 0
    max_i, max_j = 0, 0
    for i in range(n):
        for j in range(i+1, n):
            distance = taxicab_distance(x_coords[i], y_coords[i], x_coords[j], y_coords[j])
            if distance > max_distance:
                max_distance = distance
                max_i, max_j = i, j
    return max_distance, max_i, max_j

def draw_triangle(ax, x_coords, y_coords, label):
    ax.plot(x_coords + [x_coords[0]], y_coords + [y_coords[0]], 'bo-')  # Draw the triangle
    ax.text((x_coords[0] + x_coords[1]) / 2, y_coords[0], label, color='blue', fontsize=10, ha='center')  # Label it

def plot_taxicab_diameter(ax, x_coords, y_coords, angle, diameter):
    ax.plot([x_coords[0], x_coords[1]], [y_coords[0], y_coords[1]], 'k--', alpha=0.5)  # Plot the line for angle
    ax.text(x_coords[1], y_coords[1], f"Açı: {angle}°", color='black', fontsize=10, ha='center', va='bottom', alpha=0.5)  # Label the angle
    ax.plot([x_coords[2], (x_coords[1] + x_coords[2]) / 2], [y_coords[2], (y_coords[1] + y_coords[2]) / 2], 'k--', alpha=0.5)  # Plot the line for diameter
    ax.text((x_coords[1] + x_coords[2]) / 2, (y_coords[1] + y_coords[2]) / 2, f"Taxicab Çapı: {diameter:.2f}", color='black', fontsize=10, ha='center', va='top', alpha=0.5)  # Label the diameter

def main():
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.set_xlabel('X Koordinatı')
    ax.set_ylabel('Y Koordinatı')
    ax.set_title("Eşkenar Üçgen ve Taxicab Çapı")

    # Eşkenar üçgenin taban uzunluğu ve yüksekliği
    base_length = 2  # Eşkenar üçgenin taban uzunluğu

    # Başlangıçta eşkenar üçgenin yüksekliği
    height = math.sqrt(3) / 2 * base_length  # Eşkenar üçgenin yüksekliği (tabanın uzunluğunun yarısı * √3/2)

    # Eşkenar üçgenin köşe noktaları
    x_coords = [0, base_length / 2, base_length]
    y_coords = [0, height, 0]

    # Eşkenar üçgeni çiz
    draw_triangle(ax, x_coords, y_coords, "Eşkenar Üçgen")

    # Başlangıçta taxicab çapını hesapla ve çiz
    diameter, _, _ = taxicab_diameter(x_coords, y_coords)
    plot_taxicab_diameter(ax, x_coords, y_coords, "Eşkenar", diameter)

    plt.grid(True)
    plt.axis('equal')
    plt.show()

    while True:
        # Kullanıcıdan açı değeri alınır
        angle = float(input("Açı değerini girin (0 ile 180 arasında, 0 ve 180 olmayacak): "))
        if 0 < angle < 180:
            # Yüksekliğin sabit olduğu bir durumda, açıya göre yükseklik hesaplanır
            height = math.tan(math.radians(angle)) * (base_length / 2)

            # Eşkenar üçgenin diğer iki köşesi hesaplanır
            x2 = base_length / 2
            y2 = height
            x3 = base_length
            y3 = 0

            # Eşkenar üçgenin koordinatları listelenir
            x_coords = [0, x2, x3]
            y_coords = [0, y2, 0]

            # Üçgen çizdirilir ve taxicab çapı çizilir
            draw_triangle(ax, x_coords, y_coords, f"Açı: {angle}°")
            diameter, _, _ = taxicab_diameter(x_coords, y_coords)
            plot_taxicab_diameter(ax, x_coords, y_coords, angle, diameter)

            plt.grid(True)
            plt.axis('equal')
            plt.show()

            devam = input("Devam etmek istiyor musunuz? (E/H): ")
            if devam.upper() != 'E':
                break
        else:
            print("Geçerli bir açı değeri girin.")

if __name__ == "__main__":
    main()
