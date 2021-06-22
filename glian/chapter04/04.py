import numpy as np

fs = 44100
t = np.arange(fs) / fs
f1 = 10
f2 = 100
r1 = 1
r2 = 2
x1 = r1 * np.sin(2 * np.pi * f1 * t)
x2 = r2 * np.sin(2 * np.pi * f2 * t)
x = x1 + x2
X = np.fft.fft(x)

# 時間平均のパワーは振幅に依存、周波数に依存しないとわかる
print(f"{np.sum(x1**2):.2f}")
print(f"{np.sum(x2**2):.2f}")
print(f"{np.sum(x**2):.2f}")

# 一定の周波数範囲について平均を求める、度の周波数帯域にどの程度のパワー
p1 = 20 * np.log10(np.sum(np.abs(X[1:20])))
p2 = 20 * np.log10(np.sum(np.abs(X[91:110])))
print(f"{p1:.2f}")
print(f"{p2:.2f}")
