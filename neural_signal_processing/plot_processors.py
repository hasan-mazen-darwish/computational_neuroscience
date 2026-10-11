import scipy.io as sio
import matplotlib.pyplot as plt

mat_data = sio.loadmat("data/spikes.mat")
rho_data = mat_data["rho"]

plt.figure(figsize=(10, 5))
plt.plot(rho_data, label="Rho data")

plt.title("My MATLAB data")
plt.xlabel("ms")
plt.ylabel("Spike")
plt.grid(True)
plt.legend()

plt.show()
