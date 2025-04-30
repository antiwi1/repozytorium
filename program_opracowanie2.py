import numpy as np
import matplotlib.pyplot as plt

# funkcja modelujaca trajektorie punktu na scenie 2d
def trajektoria(x):
    return x * np.sin(x)

# pierwsza pochodna trajektorii (predkosc ruchu)
def pochodna1(x, h=1e-5):
    return (trajektoria(x+h) - trajektoria(x-h)) / (2*h)

# druga pochodna trajektorii (krzywizna ruchu)
def pochodna2(x, h=1e-5):
    return (trajektoria(x+h) - 2 * trajektoria(x) + trajektoria(x-h)) / (h**2)

# generowanie punktow na osi x
x = np.linspace(0.1, 10, 1000)

# obliczenia wartosci funkcji oraz jej pochodnych
y = trajektoria(x)
y_pochodna1 = pochodna1(x)
y_pochodna2 = pochodna2(x)

# tworzenie wykresu
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(x, y, label='trajektoria')
plt.title('trajektoria obiektu w czasie')
plt.grid()
plt.legend()

# wykres pierwszej pochodnej
plt.subplot(3, 1, 2)
plt.plot(x, y_pochodna1, color='green', label='predkosc')
plt.title('predkosc obiektu (pierwsza pochodna)')
plt.grid()
plt.legend()

# wykres drugiej pochodnej
plt.subplot(3, 1, 3)
plt.plot(x, y_pochodna2, color='red', label='krzywizna')
plt.title('krzywizna trajektorii (druga pochodna)')
plt.grid()
plt.legend()

# wyswietlenie wykresow
plt.tight_layout()
plt.show()
