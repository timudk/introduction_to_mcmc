"""
This example produces a sequence of samples for the uniform distribution
U([0,1]) using a linear congruential generator (LCG). A description of
the method can be found at 
https://en.wikipedia.org/wiki/Linear_congruential_generator.
"""
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import MaxNLocator

rc('font', **{'size':24, 'family':'serif', 'serif':['Computer Modern Roman']})
rc('text', usetex=True)

# Parameters for LCG https://en.wikipedia.org/wiki/Linear_congruential_generator
X_0 = 0
M = np.power(2, 32)
A = 1664525
C = 1013904223

NUM_DRAWS = 1000000
NUM_BINS = 100

PATH = 'output/linear_congruential_generator/uniform_samples_with_' + str(NUM_DRAWS) + '_draws_fs_24.pdf'

def compute_uniform_samples():
	"""
	Random numbers are computed according to the formula X_{n+1} = (A*X_{N} + C) mod M.
	Uniform Samples U_{i} are then computed as U_{i} = X_{i} / M for i = [1, NUM_DRAWS] 
	"""
	X_values = np.zeros(NUM_DRAWS)
	X_values[0] = X_0
	
	for i in range(0, (NUM_DRAWS-1)):
		X_values[i+1] = (A*X_values[i] + C) % M

	return (X_values/M)

def visualization(samples):
	"""
	Plotting the draws in form of a histogram clusterd in NUM_BINS bins and saving figure.
	"""
	n, bins, patches = plt.hist(samples, NUM_BINS, color='white', histtype='bar', ec='black')

	ax = plt.gca()
	ax.set_xlim([0,1])

	ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='lower'))

	plt.xlabel(r'Drawn values')
	plt.ylabel(r'Frequency')

	plt.savefig(PATH, bbox_inches='tight')
	plt.show()

samples = compute_uniform_samples()
visualization(samples)