import matplotlib.pyplot as plt
import numpy as np

def draw_circle(center, radius):
    circle = plt.Circle(center, radius, fill=False, color='r')
    plt.gca().add_patch(circle)

def draw_points(points):
    plt.scatter(*zip(*points), marker='o')
    plt.xlim(0, 1)
    plt.ylim(0, 1)

def compute_circle(points):
    # Kümenin ağırlık merkezi
    center = np.mean(points, axis=0)

    # En uzak noktanın çapı (yarıçap)
    radius = max(np.linalg.norm(np.array(center) - np.array(point)) for point in points)

    return center, radius

# Kullanıcıdan nokta sayısını al
num_points = int(input("Kaç nokta gireceksiniz? "))

# Kullanıcıdan noktaları al
points = []
for i in range(num_points):
    x = float(input(f"Nokta {i + 1} x koordinatını girin: "))
    y = float(input(f"Nokta {i + 1} y koordinatını girin: "))
    points.append((x, y))

# Çemberi çizme
draw_points(points)

# Çemberi hesapla ve çiz
center, radius = compute_circle(points)
draw_circle(center, radius)

# Düzgün bir çizim sağlamak için:
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
