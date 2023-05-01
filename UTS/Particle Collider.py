'''
==================
UTS. Fisika Komputasi
[4] Sebelumnya sudah dibahas di dalam kelas mengenai
gerak partikel dengan kecepatan konstan sistem
bola billiard dengan syarat batas memantul sempurna.
Partikel yang dilibatkan sebelumnya hanya sebuah.

Pelajari mengenai gerak partikel 2D yang melibatkan
banyak partikel sehingga akan terjadi tumbukan antar
partikel. Massa setiap partikel didefinisikan tetapi
di set m = 1 untuk memudahkan. Tumbukan diset
elastik sempurna (e = 1.0) untuk memudahkan
==================
by. Julian Evan Chrisnanto
v.1 : Initial build - 17.4.2023
v.2 : Animation updated - 19.4.2023
==================
'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Membuat class bernama "Ball"
class Ball:
    def __init__(self, mass, x, y, v0, angle):
        # Membuat atribut pada "Ball"
        self.mass = mass # massa
        self.x = x # posisi x
        self.y = y # posisi y
        self.v0 = v0 # kecepatan awal
        self.angle = angle # sudut awal
        self.vx = v0*np.cos(angle) # kecepatan awal sb. x
        self.vy = v0*np.sin(angle) # kecepatan awal sb. y

    def collide(self, other, k):
        # Membuat fungsi untuk tumbukan dengan partikel lain "other"
        # bentukan sudut
        angle = np.arctan2(self.y-other.y, self.x-other.x)

        # momentum awal
        self_momentum = self.mass + np.sqrt(self.vx**2+self.vy**2)
        other_momentum = other.mass + np.sqrt(other.vx**2+other.vy**2)

        # kecepatan awal
        self_vx_init = self_momentum * np.cos(self.angle-angle)/self.mass
        self_vy_init = self_momentum * np.sin(self.angle-angle)/self.mass
        other_vx_init = other_momentum * np.cos(other.angle-angle)/other.mass
        other_vy_init = other_momentum * np.sin(other.angle-angle)/other.mass

        # kecepatan akhir
        self_vx_final = (self.mass - k*other.mass)/(self.mass + other.mass) * \
            self_vx_init + (1+k*other.mass /
                            (self.mass + other.mass))*other_vx_init
        self_vy_final = (self.mass - k*other.mass)/(self.mass + other.mass) * \
            self_vy_init + (1+k*other.mass /
                            (self.mass + other.mass))*other_vy_init
        other_vx_final = (other.mass - k*self.mass)/(self.mass + other.mass) * \
            other_vx_init + \
            (1+k*self.mass/(self.mass + other.mass))*self_vx_init
        other_vy_final = (other.mass - k*self.mass)/(self.mass + other.mass) * \
            other_vy_init + \
            (1+k*self.mass/(self.mass + other.mass))*self_vy_init

        # perubahan kecepatan akibat tumbukan
        self.vx = np.cos(angle) * self_vx_final + np.sin(angle) * self_vy_final
        self.vy = -np.sin(angle) * self_vx_final + \
            np.cos(angle) * self_vy_final
        other.vx = np.cos(angle) * other_vx_final + \
            np.sin(angle) * other_vy_final
        other.vy = -np.sin(angle) * other_vx_final + \
            np.cos(angle) * other_vy_final

    def move(self, dt, minx, maxx, miny, maxy):
        # Membuat fungsi untuk pergerakan partikel dengan metode Euler
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Syarat batas untuk dinding-dinding
        if self.x > maxx:  # Dinding kanan
            self.x = maxx - (self.x - maxx)
            self.vx = (0.8)*(-self.vx)
        elif self.x < minx:  # Dinding kiri
            self.x = -self.x
            self.vx = (0.8)*(-self.vx)
        if self.y > maxy:  # Dinding atas
            self.y = maxy - (self.y - maxy)
            self.vy = (0.8)*(-self.vy)
        elif self.y < miny:  # Dinding bawah
            self.y = -self.y
            self.vy = (0.8)*(-self.vy)

# Fungsi untuk mensimulasikan tumbukan antar partikel
def simulate(balls, dt, k, minx, maxx, miny, maxy):
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            ball1 = balls[i]
            ball2 = balls[j]
            dx = ball1.x - ball2.x
            dy = ball1.y - ball2.y
            dist = np.sqrt(dx**2+dy**2)
            if dist < 0.7: # Mengecek jarak antar partikel jika sudah dekat atau menempel
                ball1.collide(ball2, k)
        ball1.move(dt, minx, maxx, miny, maxy)

dt = 0.0001
ta = int(input('Waktu awal (s): '))
tb = int(input('Waktu akhir (s): '))
e = 1
minx = int(input('Batas kiri: '))
maxx = int(input('Batas kanan: '))
miny = int(input('Batas bawah: '))
maxy = int(input('Batas atas: '))

Nstep = int((tb-ta)/dt)
t = np.arange(ta, tb, dt)

# Membuat objek partikel dengan class "Ball"
m0 = Ball(1, 0.25*maxx, 0.5*maxy, 500, 0)
m1 = Ball(1, 0.5*maxx-0.75, 0.5*maxy, 0, 0)
m2 = Ball(1, 0.5*maxx, 0.5*maxy+0.5, 0, 0)
m3 = Ball(1, 0.5*maxx, 0.5*maxy-0.5, 0, 0)
m4 = Ball(1, 0.5*maxx+0.75, 0.5*maxy+0.7, 0, 0)
m5 = Ball(1, 0.5*maxx+0.75, 0.5*maxy, 0, 0)
m6 = Ball(1, 0.5*maxx+0.75, 0.5*maxy-0.7, 0, 0)
balls = [m0, m1, m2, m3, m4, m5, m6]
# Membuat array untuk menyimpan posisi x dan y pada setiap partikel
x_pos = [[] for _ in range(len(balls))]
y_pos = [[] for _ in range(len(balls))]

fig, ax = plt.subplots()

# Membuat plot scatter untuk setiap partikel
scatters = [ax.scatter([], [], label='m%d' % (i+1)) for i in range(len(balls))]


# Membuat batas untuk sumbu x dan sumbu y grafik
ax.set_xlim(minx, maxx)
ax.set_ylim(miny, maxy)


# Membuat fungsi untuk animasi pergerakan partikel
def update(frame):
    for i in range(len(balls)):
        balls[i].move(dt, minx, maxx, miny, maxy)
        x_pos[i].append(balls[i].x)
        y_pos[i].append(balls[i].y)
        scatters[i].set_offsets((balls[i].x, balls[i].y))
    simulate(balls, dt, e, minx, maxx, miny, maxy)
    return scatters


# Membuat objek animasi
ani = animation.FuncAnimation(fig, update, frames=Nstep, interval=0, blit=True)

# Menampilkan animasi
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title("Gerak Tumbukan Partikel")
plt.show()
