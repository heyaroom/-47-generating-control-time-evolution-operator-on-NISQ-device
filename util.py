"""
Written by Kentaro Heya
"""
import numpy as np

I = np.array([[1.+0.j, 0.+0.j],[0.+0.j, 1.+0.j]])
X = np.array([[0.+0.j, 1.+0.j],[1.+0.j, 0.+0.j]])
Y = np.array([[ 0.+0.j, -0.-1.j],[ 0.+1.j,  0.+0.j]])
Z = np.array([[ 1.+0.j,  0.+0.j],[ 0.+0.j, -1.+0.j]])

def calculate_energy(wave_function,hamiltonian):
	# when you want to experiment, please replace this function with Pauli decomposition measurement
    energy = (wave_function.T.conj()@hamiltonian@wave_function).real
    return energy

def tensor(gates):
    out = gates[0]
    for g in gates[1:]:
        out = np.kron(g,out)
    return out