import time
import scipy.io as sio
import matplotlib.pyplot as plt
from processors import AverageSpikes, SlidingWindowAveraging

mat_data = sio.loadmat("data/spikes.mat")
rho_data = mat_data["rho"]

plt.figure(figsize=(10, 5))
plt.plot(rho_data, label="Rho data", color="grey", linewidth=1)

start = time.perf_counter()
averaged = AverageSpikes(rho_data.flatten().astype(int).tolist(), 100)
end = time.perf_counter()
print(f"The time the averaging took: {(end - start) * 1000 : .2f}.")
plt.plot(averaged, label="Averaged", color="red", linewidth=3)

start = time.perf_counter()
slided = SlidingWindowAveraging(rho_data.flatten().astype(int).tolist(), 100)
end = time.perf_counter()
print(f"The time the sliding took: {(end - start) * 1000 : .2f}.")
plt.plot(slided, label="Averaged", color="blue", linewidth=1, linestyle="-.")

plt.title("My MATLAB data")
plt.xlabel("ms")
plt.ylabel("Spike")
plt.grid(True)
plt.legend()

plt.show()
