DEFAULT_SAMPLE_RATE_KHZ = 16

def windows(tensor, wsize=None):
    #     window_ms = 25
    #     window_s = window_ms / 1000
    #     window_size = int(window_s * DEFAULT_SAMPLE_RATE_KHZ * 1000)

    window_size = wsize
    overlap_percent = 50
    step_size = int(window_size // (1 // (overlap_percent / 100)))

    return tensor.unfold(1, window_size, step_size)