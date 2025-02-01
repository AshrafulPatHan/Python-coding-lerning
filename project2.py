import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ফুলের আকৃতি সংজ্ঞায়িত করা
t = np.linspace(0, 2 * np.pi, 100)
x = np.sin(t) * np.cos(4 * t)
y = np.sin(t) * np.sin(4 * t)

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

petals, = ax.plot([], [], 'r', lw=2)
particles, = ax.plot([], [], 'yo', markersize=5)

# কণা সংরক্ষণ
num_particles = 20
px = np.random.uniform(-0.1, 0.1, num_particles)
py = np.random.uniform(-0.1, 0.1, num_particles)
pvx = np.random.uniform(-0.02, 0.02, num_particles)
pvy = np.random.uniform(-0.02, 0.02, num_particles)

def init():
    petals.set_data([], [])
    particles.set_data([], [])
    return petals, particles

def update(frame):
    petals.set_data(x, y)
    
    global px, py
    px += pvx
    py += pvy
    particles.set_data(px, py)
    
    return petals, particles

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, interval=50, blit=True)
plt.show()
