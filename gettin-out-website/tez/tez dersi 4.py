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

# Kümenin noktaları
points = [(0.2, 0.3), (0.4, 0.5), (0.6, 0.7), (0.8, 0.9)]

# Çemberi çizme
draw_points(points)

center, radius = compute_circle(points)
draw_circle(center, radius)

plt.show()
