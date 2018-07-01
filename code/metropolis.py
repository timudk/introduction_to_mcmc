"""
This examples produces a sequence of samples drawn from the non-normalized 
distribution f(x) = 0.3exp(-0.2x^2) + 0.7exp(-0.2(x-10)^2) using the Metropolis
algorithm with a normal proposal distribution 
"""
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc
import math

rc('font', **{'size':24, 'family':'serif', 'serif':['Computer Modern Roman']})
rc('text', usetex=True)

# Parameters
NUM_BINS = 100
NUM_DRAWS = 100000

STD_DEVIATION_PROP_DIST = 10

ACC_TARGET_DIST = 30001
LEFT_LIM = -10
RIGHT_LIM = 20

PATH = 'output/metropolis/stochastic_project_with_' + str(NUM_DRAWS) + '_draws_fs_24.pdf'

def draw_sample(x_i):
	return np.random.normal(x_i, STD_DEVIATION_PROP_DIST)

def non_normalized_target(x):
	return 0.3*np.exp(-0.2*x*x) + 0.7*np.exp(-0.2*np.power((x-10), 2)) 

def normalized_target(x):
	return (np.sqrt(0.2)/np.sqrt(math.pi))*non_normalized_target(x)

def one_step_of_metropolis_algorithm(current_x):
	"""
	Runs one step of the Metropolis algorithm 
	"""
	uniform_sample = np.random.uniform(0,1)

	x_proposal = draw_sample(current_x)

	acceptance_rate = min(1, (non_normalized_target(x_proposal))/(non_normalized_target(current_x)))

	if uniform_sample < acceptance_rate:
		return x_proposal
	else:
		return current_x

def visualization(samples):
	"""
	Plotting the draws in form of a histogram clusterd in NUM_BINS bins and saving figure.
	"""
	plt.hist(samples, NUM_BINS, color='white', histtype='bar', ec='black', normed=True)

	target_distribution = np.linspace(LEFT_LIM, RIGHT_LIM, ACC_TARGET_DIST)

	plt.plot(target_distribution, normalized_target(target_distribution), color='k', linestyle='-', linewidth=2)

	plt.xlabel(r'Drawn samples')
	plt.ylabel(r'Bin counts')
	plt.xlim(-10,20)

	plt.savefig(PATH, bbox_inches='tight')
	plt.show()

samples = np.zeros(NUM_DRAWS)
samples[0] = 0

for i in range(0, (NUM_DRAWS-1)):
	samples[i+1] = one_step_of_metropolis_algorithm(samples[i])

visualization(samples)