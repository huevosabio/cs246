# HW2, Q2e, Ramon Iglesias

import scipy as sp
import scipy.linalg as lg 
import numpy as np


M = np.array([
		[1,2],
		[2,1],
		[3,4],
		[4,3]
	])


if __name__ == "__main__":
	# part 1
	U, E, V =  lg.svd(M)
	print U, E, V.transpose()
	if E[0] > E[1]: print "First element of E is larger than the second."

	# part 2
	MTM = np.dot( np.transpose(M) , M)
	evals, evecs = lg.eigh(MTM)
	sorted_ind = np.flip(np.argsort(evals),0)
	evals =  evals[sorted_ind] 
	evecs  = evecs[:,sorted_ind]
	print "evals, evecs: \n",evals, evecs 
	print evecs, V.transpose()

	#part 3
	print "The elements of Evecs and V are the same in magnitude, but not in sign."

	#part 4
	print E, np.sqrt(evals)
	print "The singular values of M equal the square root of the eigenvalues of MTM"