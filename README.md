# Quantum_Simulator
<ol><li>Define Quantum Circuit <code>qc = QuantumCircuit(n)</code></li>
  <br><li>Apply Quantum Gates to the Circuit 
  <ul><li>Pauli-X Gate : <code>qc.x(Index_of_Qubit)</code></li>
  <li>Hadamard Gate : <code>qc.h(Index_of_Qubit)</code></li> 
  <li>Pauli-Z : <code>qc.z(Index_of_Qubit)</code></li> 
  <li>Rotation Gate : <code>qc.r(Angle_in_radians,Index_of_Qubit)</code></li> 
  <li>Controll-X Gate : <code>qc.cx(Controll_Index1,Target_Index)</code></li>
  <li>Controll-Z Gate : <code>qc.cz(Controll_Index1,Target_Index)</code></li>
  <li>Controll-R Gate : <code>qc.cr(Controll_Index1,Target_Index)</code></li> 
  <li>Controll-Controll-X Gate : <code>qc.ccx(Controll_Index1,Controll_Index2,Target_Index)</code></li></ul>
  </li></br>
  <li>Simulate the Quanutm Circuit</li>
  <ul><li>To measure Qubits : <code>qc.execute()</code></li>
  <li>Prints a single unitary matrix : <code>qc.unitary()</code></li>
  <li>Prints the current quantum state of the circuit : <code>qc.state</code></li>
  <li>Prints the probability of the states : <code>qc.prob()</code></li></ul></ol>
