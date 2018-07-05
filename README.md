# Introduction to Markov chain Monte Carlo methods
This project has been developed as part of the class AMATH777 - Stochastic Processes in the Physical Sciences at the University of Waterloo. The code is entirely written in Python. A documentation in form of a report as well as a presentation can be found [here](https://github.com/timudk/introduction_to_mcmc/tree/master/documentation).

# Code description
The code is based on the following packages:
* numpy 
* matplotlib

Check (and potentially download the two packages) using pip:
```console
foo@bar:~$ pip install numpy matplotlib
```

## uniform_samples_using_linear_congruential_generator.py
This example produces a sequence of samples for the uniform distribution U([0,1]) using a linear congruential generator (LCG). A description of the method can be found at https://en.wikipedia.org/wiki/Linear_congruential_generator.

Parameter list:
* abc

## pi_monte_carlo.py
This example approximates pi numerically using a Monte Carlo estimator I = (4/N) SUM_{i=1}^{N} h(x^(i), y^(i)) where h() is the indicator function h(x,y) = {1 if x^2+y^2 <= 1 and 0 otherwise} and the tupels (x^(i), y^(i)) are drawn from the uniform distribution U([0,1]x[0,1]).

## metropols.py
This examples produces a sequence of samples drawn from the non-normalized distribution f(x) = 0.3exp(-0.2x^2) + 0.7exp(-0.2(x-10)^2) using the Metropolis algorithm with a normal proposal distribution (see [Andrieu et al.](http://www.cs.ubc.ca/~arnaud/andrieu_defreitas_doucet_jordan_intromontecarlomachinelearning.pdf) for further details).

