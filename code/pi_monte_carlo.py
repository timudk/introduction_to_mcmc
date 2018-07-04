"""
This example approximates pi numerically using a Monte Carlo estimator:
I = (4/N) SUM_{i=1}^{N} h(x^(i), y^(i)) where h() is the indicator 
function h(x,y) = {1 if x^2+y^2 <= 1 and 0 otherwise} and the tupels 
(x^(i), y^(i)) are drawn from the uniform distribution U([0,1]x[0,1])
"""
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import rc
import math
from math import log10, floor
from matplotlib.ticker import MaxNLocator

rc('font', **{'size':12, 'family':'serif', 'serif':['Computer Modern Roman']})
rc('text', usetex=True)

# Parameters for simulation
NUM_RUNS = 10
NUM_DRAW_STEPS = 5

STEP_MULTIPLIER = 10
STEP_START = 100

PRECISION = 6

PATH_FIG = 'pi_monte_carlo.pdf'
PATH_DATA = 'pi_monte_carlo.txt'

def round_sig(x, sig):
	return round(x, sig-int(floor(log10(abs(x))))-1)

def indicator_function(x, y):
	if (np.power(x, 2) + np.power(y, 2)) <= 1:
		return 1
	else:
		return 0

def approximation(num_draws):
	"""
	Approximation of pi with (num_draws) number of draws
	"""
	samples = np.random.uniform(-1, 1, (num_draws, 2))

	draws_in_circle = 0

	for i in range(0, num_draws):
		draws_in_circle += indicator_function(samples[i,0], samples[i,1])

	return 4*(draws_in_circle/num_draws)

def simulation():
	"""
	The approximation is run (NUM_RUNS)x(NUM_DRAW_STEPS)
	"""
	pi_approximations = np.zeros((NUM_DRAW_STEPS, NUM_RUNS))

	num_draws = STEP_START

	for i in range(0, NUM_DRAW_STEPS):
		for j in range(0, NUM_RUNS):
			pi_approximations[i,j] = approximation(num_draws)

		num_draws *= STEP_MULTIPLIER

	return pi_approximations

def visualization(pi_approximations):
	"""
	Plotting the expected values of the simulation
	"""
	fig, ax = plt.subplots() 

	labels = [r'$10^2$', r'$10^3$', r'$10^4$', r'$10^5$', r'$10^6$']
	x = [0, 1, 2, 3, 4]

	ax.plot([-0.5, NUM_RUNS], [math.pi, math.pi], color='k', linestyle='-', linewidth=1)
	ax.plot(pi_approximations,'kx',markersize=2)

	plt.xlabel(r'Number of draws')
	plt.ylabel(r'Expected value $I(h)$')
	plt.xlim(-0.5, NUM_DRAW_STEPS-0.5)
	ax.xaxis.set_major_locator(MaxNLocator(integer=True))
	plt.xticks(x, labels)

	plt.savefig(PATH_FIG, bbox_inches='tight')
	plt.show()

def data(pi_approximations):
	"""
	Saving the data of the expected values 
	"""
	data_file = open(PATH_DATA, 'w')

	for i in range(0, NUM_DRAW_STEPS):
		expecation_sum = 0

		for j in range(0, NUM_RUNS):
			roundend_expactation = round_sig(pi_approximations[i, j], PRECISION)
			expecation_sum += roundend_expactation

			data_file.write(str(roundend_expactation) + ' ')

		mean = round_sig((expecation_sum/NUM_RUNS), PRECISION)

		data_file.write('\t' + str(mean))
		data_file.write('\n')

approximation = simulation()

visualization(approximation)
data(approximation)
