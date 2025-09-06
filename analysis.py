
import matplotlib.pyplot as plt


def display_correlation_clean(corr, threshold=100):
    plt.plot([i if i > 100 else 0 for i in corr])

def get_positions_of_correlation_spikes(corr, threshold=100):
    return [i for i, j in enumerate(corr) if j > threshold]
