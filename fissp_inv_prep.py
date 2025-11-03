import numpy as np 
import pyana 
from astropy.io import fits
import sys

# Open fissp file:

fissp = fits.open(sys.argv[1])

# Save intensity as a separate pyana cube:

pyana.fzwrite("obs01_fissp.f0", fissp[0].data.astype(np.float32), 0, 'bla')

# Make wavelength grid:

ll = fissp[1].data

np.savetxt("fissp_lgrid.dat", ll.T, fmt='%1.7e', header=str(len(ll)),comments='')

# Make a mask although it's not really needed here:

mask = np.ones(len(ll))

np.savetxt("fissp_mask.dat", mask.T, fmt='%1.7e', header=str(len(mask)),comments='')

