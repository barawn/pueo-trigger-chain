import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# FIR coefficients (divide each by 32768)
coeffs = np.array([
    0, -23, 0, 105, 0, -263, 0, 526, 0, -949, 0, 1672, 0, -3216,
    0, 10342, 16384, 10342, 0, -3216, 0, 1672, 0, -949, 0, 526,
    0, -263, 0, 105, 0, -23
], dtype=float) / 32768.0

# Frequency response for positive frequencies (0..pi radians/sample)
w, h = freqz(coeffs, worN=4096, whole=False)  # w in radians/sample

# Convert to normalized frequency (cycles/sample), Nyquist = 0.5
f = w*(3000/(2*np.pi))

# Magnitude in dB (protect against log(0) with a floor)
mag_db = 20 * np.log10(np.maximum(np.abs(h), 1e-12))

# Plot
fig=plt.figure(figsize=(8, 4.8))
plt.plot(f, mag_db)
plt.title('Halfband Filter Response')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Magnitude (dB)')
plt.ylim([-62, 2])           # Y scale from -42 dB to +2 dB
plt.xlim([0,1500])           # Only positive frequencies up to Nyquist
plt.grid(True, which='both', ls='--', alpha=0.6)
plt.tight_layout()
plt.show()
fig.savefig('halfband_freq_resp.png', bbox_inches='tight')
