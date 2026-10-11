import ctypes
from pathlib import Path
from typing import cast

clib_path = Path(__file__).parent.resolve() / "library.so"

clib = ctypes.CDLL(str(clib_path))

average_spikes= clib.average_spikes
average_spikes.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_uint, ctypes.c_size_t]
average_spikes.restype = ctypes.POINTER(ctypes.c_double)

def AverageSpikes(spikes: list[int], window: int) -> list[float]:
    size: int = len(spikes)
    array_type = ctypes.c_int * size
    c_spikes = array_type(*spikes)
    result = average_spikes(c_spikes, window, size)
    return cast(list[float], result[:size])

sliding_window_averaging = clib.sliding_window_averaging
sliding_window_averaging.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_uint, ctypes.c_size_t]
sliding_window_averaging.restype = ctypes.POINTER(ctypes.c_double)

def SlidingWindowAveraging(spikes: list[int], window: int) -> list[float]:
    size: int = len(spikes)
    array_type = ctypes.c_int * size
    c_spikes = array_type(*spikes)
    result = sliding_window_averaging(c_spikes, window, size)
    return cast(list[float], result[:size])
