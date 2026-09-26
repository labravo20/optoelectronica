import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. Parámetros de simulación
# ============================================================

fs = 10000        # Frecuencia de muestreo [Hz]
T = 1             # Duración de la señal [s]

t = np.arange(0, T, 1/fs)
N = len(t)


# ============================================================
# 2. Parámetros del diodo
# ============================================================

io = 10e-12       # Corriente inversa de saturación [A]

kT_e = 26e-3      # kT/e [V]


# ============================================================
# 3. Señal de entrada
# ============================================================

f = 50            # Frecuencia de entrada [Hz]

v = 0.3 + 0.2*np.cos(2*np.pi*f*t)


# ============================================================
# 4. Corriente de salida del diodo
# ============================================================

i = io * (np.exp(v/kT_e) - 1)


# ============================================================
# 5. FFT de la señal de entrada
# ============================================================

V = np.fft.fft(v)

frequencies = np.fft.fftfreq(N, 1/fs)

amplitude_v = np.abs(V) / N


# ============================================================
# 6. FFT de la señal de salida
# ============================================================

I = np.fft.fft(i)

amplitude_i = np.abs(I) / N


# ============================================================
# 7. Seleccionamos únicamente frecuencias positivas
# ============================================================

positive = frequencies >= 0

frequencies_positive = frequencies[positive]

amplitude_v_positive = amplitude_v[positive]
amplitude_i_positive = amplitude_i[positive]


# ============================================================
# 8. Corrección para espectro de un solo lado
# ============================================================

amplitude_v_positive[1:] *= 2
amplitude_i_positive[1:] *= 2


# ============================================================
# 9. Gráficas
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

plt.xlim(-5, 500)

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud [V]")

plt.title(
    "Espectro de Fourier de la señal de entrada $v(t)$"
)

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

plt.xlim(-5, 500)

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud [A]")

plt.title(
    "Espectro de Fourier de la corriente del diodo $i(t)$"
)

plt.grid()


plt.tight_layout()

plt.show()