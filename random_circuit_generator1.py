import numpy as np
import filecmp
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import BasicAer, execute
backend1 = BasicAer.get_backend('dm_simulator')
backend2 = BasicAer.get_backend('qasm_simulator')
options = {}
q = QuantumRegister(6)
c = ClassicalRegister(6)
qc = QuantumCircuit(q, c)
qc.ccx(q[1],q[2],q[4])
qc.u2(2.7592,0.37848,q[5])
qc.u1(5.09615,q[3])
qc.u2(1.29469,0.24065,q[3])
qc.u1(0.01988,q[3])
qc.u2(1.84521,4.44888,q[5])
qc.cx(q[4],q[2])
qc.cx(q[4],q[5])
qc.u3(2.4455,0.00823,1.54083,q[2])
qc.cx(q[5],q[0])
qc.u2(5.47599,1.38151,q[3])
qc.ccx(q[0],q[3],q[1])
qc.u3(2.92573,3.05912,0.14268,q[3])
qc.u3(2.91117,0.69042,4.16295,q[5])
qc.cx(q[0],q[1])
qc.u2(1.54008,0.89818,q[4])
qc.cx(q[3],q[1])
qc.u2(4.65354,3.23322,q[0])
qc.cx(q[1],q[3])
qc.ccx(q[3],q[5],q[0])
qc.u3(1.96491,3.58183,2.68852,q[0])
qc.u3(1.62891,1.60202,0.34693,q[1])
qc.cx(q[5],q[4])
qc.u1(5.74714,q[5])
qc.ccx(q[3],q[5],q[0])
qc.u3(1.26693,0.00659,0.33206,q[4])
qc.ccx(q[0],q[3],q[1])
qc.u3(1.01862,5.26208,4.33741,q[5])
qc.ccx(q[0],q[4],q[5])
qc.u3(1.81098,5.10403,3.72515,q[2])
qc.u2(5.1396,1.48429,q[2])
qc.u2(5.61874,5.00958,q[4])
qc.u1(2.92397,q[1])
qc.u1(3.98508,q[0])
qc.u1(3.17708,q[3])
qc.cx(q[2],q[4])
qc.u1(3.78243,q[3])
qc.ccx(q[5],q[0],q[1])
qc.u2(1.33063,1.96316,q[5])
qc.ccx(q[1],q[4],q[3])
qc.u2(5.54548,1.39666,q[5])
qc.ccx(q[5],q[0],q[2])
qc.u1(5.12437,q[1])
qc.u1(3.1552,q[1])
qc.u2(0.54002,0.39858,q[4])
qc.u2(2.48001,1.51705,q[5])
qc.u1(5.38753,q[0])
qc.cx(q[2],q[5])
qc.cx(q[1],q[3])
qc.u3(2.47148,5.33871,2.39753,q[2])
qc.u2(4.34113,1.99139,q[0])
qc.u3(0.25212,0.41757,4.60321,q[4])
qc.u3(0.18024,1.1811,4.19243,q[2])
qc.u3(3.05427,4.11102,2.68507,q[2])
qc.cx(q[3],q[5])
qc.cx(q[1],q[3])
qc.ccx(q[0],q[2],q[4])
qc.u1(4.60712,q[3])
qc.cx(q[0],q[2])
qc.u3(2.59297,2.16867,1.37618,q[1])
qc.ccx(q[4],q[2],q[1])
qc.ccx(q[2],q[0],q[5])
qc.cx(q[3],q[5])
qc.ccx(q[5],q[0],q[4])
qc.u1(3.90173,q[0])
qc.u2(1.18075,3.94951,q[0])
qc.u1(4.54964,q[4])
qc.ccx(q[1],q[2],q[3])
qc.ccx(q[5],q[4],q[1])
qc.u1(2.18899,q[4])
qc.ccx(q[3],q[0],q[4])
qc.cx(q[0],q[2])
qc.ccx(q[4],q[3],q[5])
qc.ccx(q[5],q[3],q[4])
qc.ccx(q[2],q[3],q[0])
qc.u2(3.91518,2.482,q[1])
qc.cx(q[5],q[0])
qc.u3(2.80538,0.38614,2.72815,q[1])
qc.u3(1.26588,5.89102,2.52328,q[0])
qc.u2(5.21577,0.60742,q[3])
qc.u3(1.50413,5.49982,3.14411,q[3])
qc.u1(5.04023,q[4])
qc.cx(q[4],q[3])
qc.u2(2.49415,4.26668,q[0])
qc.u1(5.54078,q[2])
qc.u3(1.41665,5.72206,1.27202,q[0])
qc.u2(0.8494,2.62929,q[1])
qc.ccx(q[2],q[1],q[4])
qc.cx(q[3],q[0])
qc.u1(4.31853,q[5])
qc.ccx(q[3],q[0],q[4])
qc.cx(q[5],q[3])
qc.u2(1.04677,2.2237,q[3])
qc.u2(2.3621,0.59697,q[2])
qc.u2(4.1876,1.00328,q[2])
qc.ccx(q[1],q[2],q[0])
qc.u1(0.78868,q[4])
qc.u1(2.74302,q[5])
qc.u2(2.03696,3.43193,q[4])
qc.u3(1.54485,4.5087,0.65547,q[1])
qc.u3(1.97544,3.73226,0.86556,q[3])
qc.ccx(q[3],q[2],q[4])
qc.u3(0.23329,4.93119,2.33955,q[0])
qc.ccx(q[0],q[4],q[2])
qc.u3(2.0121,3.35968,2.2935,q[5])
qc.ccx(q[2],q[5],q[3])
qc.cx(q[0],q[2])
qc.u1(0.4943,q[2])
qc.cx(q[0],q[2])
qc.u1(0.36897,q[1])
qc.u3(0.31512,2.26599,4.18157,q[5])
qc.ccx(q[5],q[1],q[4])
qc.cx(q[3],q[2])
qc.u1(5.36408,q[4])
qc.u2(1.38744,3.18945,q[3])
qc.u3(2.91796,2.22286,3.11286,q[1])
qc.u1(2.44944,q[2])
qc.u2(3.68826,0.87362,q[2])
qc.u3(1.61192,4.67295,5.81763,q[4])
qc.u2(0.01744,0.77158,q[3])
qc.u3(1.58732,0.55494,2.07971,q[4])
qc.u2(1.53401,0.63229,q[4])
qc.u1(3.41352,q[5])
qc.ccx(q[5],q[1],q[2])
qc.u2(2.7766,0.77245,q[4])
qc.u3(1.88708,2.85068,3.91402,q[5])
qc.u3(0.88811,1.06588,1.61897,q[1])
qc.u3(2.97397,2.05244,0.35297,q[2])
qc.u1(2.19946,q[5])
qc.u1(1.22643,q[3])
qc.cx(q[0],q[5])
qc.u1(1.06806,q[4])
qc.u2(5.78761,5.33081,q[3])
qc.ccx(q[5],q[1],q[2])
qc.ccx(q[0],q[2],q[3])
qc.u3(1.28177,5.61376,2.86704,q[4])
qc.u2(4.81168,6.17144,q[1])
qc.u3(1.93772,3.15469,4.41687,q[3])
qc.u1(5.84192,q[0])
qc.u1(1.31893,q[1])
qc.ccx(q[5],q[3],q[2])
qc.cx(q[0],q[1])
qc.cx(q[5],q[2])
qc.ccx(q[2],q[3],q[5])
qc.u1(2.83071,q[5])
qc.ccx(q[5],q[4],q[0])
qc.u1(3.00509,q[5])
qc.u3(2.39883,3.03126,1.62699,q[0])
qc.cx(q[1],q[4])
qc.u1(5.62187,q[4])
qc.cx(q[3],q[1])
qc.u2(6.07618,3.58267,q[3])
qc.ccx(q[2],q[4],q[3])
qc.cx(q[4],q[1])
qc.cx(q[2],q[5])
qc.cx(q[4],q[3])
qc.u2(3.92277,2.50026,q[3])
qc.u2(0.23621,2.97526,q[2])
qc.ccx(q[1],q[0],q[2])
qc.u2(0.22434,5.50986,q[3])
qc.u1(3.12344,q[5])
qc.u2(6.21275,1.45915,q[1])
qc.ccx(q[0],q[4],q[5])
qc.u3(2.617,4.25501,1.78265,q[2])
qc.u3(1.18746,6.00944,0.86941,q[4])
qc.u1(5.03753,q[3])
qc.u3(2.59396,5.92922,1.80072,q[5])
qc.u1(1.52636,q[0])
qc.u3(2.88336,1.90331,1.97303,q[5])
qc.u1(1.84493,q[2])
qc.u2(0.86857,3.81551,q[0])
qc.ccx(q[0],q[2],q[5])
qc.u3(0.07948,4.91268,3.55532,q[3])
qc.cx(q[0],q[5])
qc.ccx(q[3],q[0],q[1])
qc.ccx(q[3],q[1],q[0])
qc.cx(q[1],q[2])
qc.cx(q[3],q[4])
qc.u3(1.9471,2.25084,5.93005,q[4])
qc.u1(4.86812,q[3])
qc.u3(1.91325,5.5638,1.14997,q[5])
qc.cx(q[0],q[4])
qc.u1(2.73543,q[4])
qc.ccx(q[1],q[3],q[0])
qc.ccx(q[4],q[5],q[0])
qc.u1(5.43229,q[5])
qc.u3(2.38608,5.33981,3.4286,q[5])
qc.ccx(q[5],q[0],q[4])
qc.cx(q[0],q[5])
qc.ccx(q[2],q[1],q[5])
qc.u3(1.89484,3.38543,0.42408,q[2])
qc.u2(0.40619,0.30259,q[5])
qc.u3(0.95128,4.38276,5.86511,q[5])
qc.u2(2.20252,2.64077,q[2])
qc.u1(6.23824,q[4])
qc.cx(q[3],q[4])
qc.ccx(q[4],q[1],q[3])
qc.u1(0.83714,q[2])
qc.cx(q[5],q[4])
qc.u1(1.71022,q[5])
qc.u3(0.90957,1.83163,4.80285,q[2])
qc.u2(5.07567,0.61625,q[5])
qc.ccx(q[0],q[3],q[5])
qc.ccx(q[0],q[3],q[4])
qc.u2(4.0627,5.93815,q[3])
qc.u2(2.40157,4.16963,q[4])
qc.ccx(q[3],q[2],q[5])
qc.cx(q[1],q[3])
qc.u3(1.85482,2.20112,3.47432,q[5])
qc.cx(q[4],q[3])
qc.u3(2.06701,0.01207,5.38023,q[4])
qc.u1(1.74327,q[1])
qc.cx(q[0],q[5])
qc.cx(q[4],q[2])
qc.u3(0.91297,3.87097,1.89109,q[4])
qc.cx(q[0],q[4])
qc.cx(q[1],q[4])
qc.u1(3.33937,q[5])
qc.u1(1.71427,q[0])
qc.u1(4.11649,q[2])
qc.u2(0.5959,5.5403,q[4])
qc.ccx(q[1],q[3],q[0])
qc.u3(0.18967,4.95778,4.96109,q[3])
qc.ccx(q[5],q[0],q[4])
qc.u2(5.41284,5.46335,q[5])
qc.cx(q[0],q[4])
qc.ccx(q[3],q[4],q[5])
qc.u1(2.44435,q[1])
qc.u2(0.40896,2.33144,q[1])
qc.u2(4.54736,4.92181,q[4])
qc.u2(3.85728,4.31158,q[3])
qc.u2(1.12524,1.66477,q[2])
qc.ccx(q[5],q[1],q[0])
qc.ccx(q[1],q[5],q[3])
qc.cx(q[3],q[2])
qc.u2(4.43868,3.82288,q[1])
qc.ccx(q[4],q[0],q[5])
qc.u3(1.83224,3.7135,1.59126,q[2])
qc.u2(0.9391,5.50182,q[5])
qc.u1(2.39372,q[4])
qc.cx(q[1],q[5])
qc.u3(3.02148,3.93117,2.43677,q[0])
qc.u3(2.432,4.99608,3.1746,q[0])
qc.ccx(q[5],q[0],q[1])
qc.u2(3.90233,4.15605,q[5])
qc.u3(0.05905,2.10705,1.46503,q[5])
qc.u1(0.06056,q[3])
qc.ccx(q[0],q[3],q[4])
qc.u1(4.63046,q[1])
qc.u2(5.63692,0.29708,q[0])
qc.u1(5.89473,q[5])
qc.u1(2.63349,q[1])
qc.ccx(q[5],q[3],q[1])
qc.ccx(q[1],q[0],q[4])
qc.u3(0.6654,0.7544,2.23518,q[3])
qc.ccx(q[2],q[4],q[5])
qc.u1(3.0972,q[3])
qc.u3(1.04681,2.81898,3.0404,q[2])
qc.cx(q[0],q[4])
qc.ccx(q[4],q[0],q[3])
qc.u1(4.52343,q[5])
qc.u2(3.31359,4.01328,q[4])
qc.u1(5.32335,q[4])
qc.u1(2.19964,q[4])
qc.cx(q[3],q[1])
qc.u2(4.71156,5.12174,q[0])
qc.u1(2.84477,q[0])
qc.u3(0.23037,4.18733,1.68053,q[4])
qc.cx(q[0],q[3])
qc.cx(q[0],q[3])
qc.cx(q[3],q[1])
qc.u2(0.11638,5.01391,q[5])
qc.u2(0.66553,0.15338,q[3])
qc.cx(q[1],q[4])
qc.cx(q[2],q[3])
qc.cx(q[0],q[3])
qc.u2(4.39186,3.67544,q[4])
qc.u3(2.96701,3.80689,1.048,q[3])
qc.u1(4.21732,q[0])
qc.u2(5.56126,2.72824,q[2])
qc.u2(2.32703,0.46943,q[4])
qc.ccx(q[4],q[5],q[0])
qc.ccx(q[2],q[1],q[0])
qc.cx(q[4],q[0])
qc.u2(1.84513,3.90741,q[0])
qc.u3(1.97305,3.33048,5.04628,q[0])
qc.u1(5.9887,q[0])
qc.ccx(q[1],q[2],q[0])
qc.ccx(q[5],q[2],q[0])
qc.u1(4.8685,q[1])
qc.u3(0.20119,5.28491,5.83238,q[4])
qc.u3(0.39157,4.53131,1.33001,q[0])
qc.u2(4.69917,5.31217,q[0])
qc.cx(q[0],q[3])
qc.u2(2.47505,1.91428,q[3])
qc.cx(q[0],q[3])
qc.cx(q[3],q[0])
qc.cx(q[2],q[0])
qc.cx(q[3],q[0])
qc.cx(q[1],q[0])
qc.u2(2.3096,2.02118,q[5])
qc.ccx(q[0],q[5],q[3])
qc.u1(5.62485,q[2])
qc.ccx(q[5],q[3],q[4])
qc.u1(1.43151,q[5])
qc.u2(2.14609,5.29964,q[5])
qc.cx(q[3],q[0])
qc.u2(4.58019,0.48309,q[0])
qc.u2(0.52609,3.13613,q[2])
qc.u3(2.02506,1.52526,2.96413,q[5])
qc.ccx(q[3],q[5],q[1])
qc.cx(q[0],q[5])
qc.u3(0.99172,4.34243,4.88027,q[3])
qc.ccx(q[2],q[3],q[4])
qc.u2(5.38423,5.46058,q[5])
qc.ccx(q[2],q[4],q[0])
qc.u3(0.60942,3.58959,5.61033,q[4])
qc.u2(0.22887,2.77272,q[3])
qc.u3(2.39112,5.21144,4.59051,q[3])
qc.u3(3.10341,3.49118,1.61894,q[5])
qc.u3(1.87081,2.87952,5.64599,q[1])
qc.u3(2.55219,2.79454,4.89236,q[0])
qc.u1(2.3472,q[4])
qc.cx(q[3],q[4])
qc.u1(0.19668,q[2])
qc.cx(q[4],q[1])
qc.u2(5.78851,3.94788,q[5])
qc.u1(0.7986,q[5])
qc.u2(1.60463,1.08947,q[0])
qc.ccx(q[3],q[2],q[0])
qc.ccx(q[1],q[2],q[0])
qc.cx(q[5],q[4])
qc.u3(0.36911,3.59176,2.30492,q[0])
qc.u1(5.53827,q[5])
qc.cx(q[4],q[3])
qc.u3(2.10355,0.51304,6.1739,q[4])
qc.u2(3.33284,0.02765,q[3])
circuits = [qc]
job = execute(circuits, backend1, **options)
result = job.result()
print(result)
job = execute(circuits, backend2, **options)
result = job.result()
print(result)
a = np.loadtxt('a.txt',dtype=complex)
b = np.loadtxt('a1.txt',dtype=complex)
p = a.real
q = a.imag
c = b.real
d = b.imag
if(np.allclose(p,c) and np.allclose(q,d)):
    print('Your result is right.')
else:
    print('Your result is wrong') 