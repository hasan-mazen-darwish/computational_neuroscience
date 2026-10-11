import ctypes
from pathlib import Path

clib_path = Path(__file__).parent.resolve() / "library.so"

clib = ctypes.CDLL(str(clib_path))

average_spikes= clib.average_spikes
average_spikes.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_uint, ctypes.c_size_t]
average_spikes.restype = ctypes.POINTER(ctypes.c_double)

sliding_window_averaging = clib.sliding_window_averaging
sliding_window_averaging.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_uint, ctypes.c_size_t]
sliding_window_averaging.restype = ctypes.POINTER(ctypes.c_double)
