import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Parámetros de simulación
# ============================================================

fs = 2000          # Frecuencia de muestreo [Hz]
T = 1              # Duración de la señal [s]

t = np.arange(0, T, 1/fs)
N = len(t)

# ============================================================
# 2. Señal de entrada
# ============================================================

f1 = 50            # Primera frecuencia [Hz]
f2 = 120           # Segunda frecuencia [Hz]

v = np.cos(2*np.pi*f1*t) + np.cos(2*np.pi*f2*t)

# ============================================================
# 3. Dispositivo no lineal
#
#               i = v^2
# ============================================================

i = v**2

# ============================================================
# 4. FFT de la señal de entrada
# ============================================================

V = np.fft.fft(v)

frequencies = np.fft.fftfreq(N, 1/fs)

amplitude_v = np.abs(V) / N

# Nos quedamos únicamente con frecuencias positivas
positive = frequencies >= 0

frequencies_positive = frequencies[positive]
amplitude_v_positive = amplitude_v[positive]

# Corrección para espectro de un solo lado
amplitude_v_positive[1:] *= 2

# ============================================================
# 5. FFT de la señal de salida
# ============================================================

I = np.fft.fft(i)

amplitude_i = np.abs(I) / N

# Frecuencias positivas
amplitude_i_positive = amplitude_i[positive]

# Corrección para espectro de un solo lado
amplitude_i_positive[1:] *= 2

# ============================================================
# 6. Gráficas
# ============================================================

plt.figure(figsize=(12, 8))

# ------------------------------------------------------------
# FFT de la entrada
# ------------------------------------------------------------

plt.subplot(2, 1, 1)

plt.stem(
    frequencies_positive,
    amplitude_v_positive,
    basefmt=" "
)

plt.xlim(-5, 300)

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.title("Espectro de Fourier de la señal de entrada $v(t)$")

plt.grid()

# ------------------------------------------------------------
# FFT de la salida
# ------------------------------------------------------------

plt.subplot(2, 1, 2)

plt.stem(
    frequencies_positive,
    amplitude_i_positive,
    basefmt=" "
)

plt.xlim(-5, 300)

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.title("Espectro de Fourier de la salida $i(t)=v^2(t)$")

plt.grid()

plt.tight_layout()

plt.show()