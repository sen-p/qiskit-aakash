# importing Qiskit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import BasicAer, execute

backend = BasicAer.get_backend('dm_simulator') # run on local simulator by default

# Creating registers
q = QuantumRegister(3)
c = ClassicalRegister(3)

# quantum circuit to make an entangled bell state
qc = QuantumCircuit(q, c)
qc.x(q[0])
#qc.measure(q[0], c[0])
qc.h(q[1])
#qc.measure(q[1], c[1])
#qc.cx(q[0], q[1])
qc.measure(q[0],c[0])
circuits = [qc]
job = execute(circuits, backend, shots=2)
result = job.result()
print(result)

#print(result.get_statevector())
