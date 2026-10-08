import numpy as np

fs = 512000

def load_iq(path="capture.iq"):
    # raw format: uint8 I/Q, meaning 127 is 0
    raw = np.fromfile(path, dtype=np.uint8).astype(np.float64) - 127.0
    x = raw[0::2] + 1j * raw[1::2]
    return x / 128.0, fs
