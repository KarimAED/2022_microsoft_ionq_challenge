# Welcome to the quantum gaming world of QHackJack!

<p align="left">
  <a href="https://azure.microsoft.com/en-us/solutions/quantum-computing/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488491-609828a4-cd1f-4076-b5b2-a8d9fc2d0fa4.png" width="30%"/> </a>
  <a href="https://ionq.com/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488159-da95eb05-9277-4abe-b1ba-b49871d563ed.svg" width="20%" style="padding: 1%;padding-left: 5%"/></a>
  <a href="https://iquhack.mit.edu/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151647370-d161d5b5-119c-4db9-898e-cfb1745a8310.png" width="8%" style="padding-left: 5%"/> </a>
  <a href="https://azure.microsoft.com/en-us/solutions/quantum-computing/" target="_blank"><img src="https://user-images.githubusercontent.com/46804607/151706126-53e47d5f-0fdf-4244-b070-73ea7fef0886.png" width="30%"/> </a>
</p>

Welcome! Not quite sure where to start? Never even heard of quantum computing? No problem, we are always glad to help here at QuHackJack Casinos™.

We are a bunch of geeks who are taking the initiative to teach quantum operations for fun. Here you will learn how to implement quantum gates not through the usual but through a fun game using our game names QHackJack.

In QuHackJack, the random cards, ranging from 3 to 10 with the 4 classic suits, are generated from a quantum computer. Now, our quantum computer doesn’t know the cards by their numbers and suits, but instead by different states, each of them labeled by a different 5-bit string, such as 01110. Then, how do we map from these bit strings to the cards? It’s quite easy, actually.

Out of the 5 bits, the last 2 are used to indicate the suit: 00 for ♣, 01 for ♠, 10 for ♥ and 11 for ♦. The other 3 bits then form a binary number ranging from 0 (represented by 000) to 7 (represented by 111). The exact mapping looks like this:

000 - 0		010 - 2		100 - 4		110 - 6
001 - 1		011 - 3		101 - 5		111 - 7

To get from these numbers to the cards in the range 3 to 10, we add another 3 to the decoded binary value.

To understand how this works, let us walk through an example. Let’s say your first number was a 9 and now you want to reach the goal of 16 exactly in just one more card. To do this, you of course need to draw a 7.

By our above logic, that 7 actually looks like a 4 to the quantum computer, represented by the binary combination 100. That is what we are trying to get in our quantum computing!

Now of the 5 bits in our full bitstrings, these actually correspond to the quantum computer q-bits read in this order:

q_4	q_3	q_2	q_1	q_0

So, if we want to get our 7, we know that we want a bit string like 100xx where x denotes the suit bits, which don’t matter to win the game. To get this, we need to reach the following states in the qubits:

q_2	|0>
q_3	|0>
q_4	|1>

Now, the initial circuit looks like

q_0 —| H | —

q_1 —| H | —

q_2 —| H | —

q_3 —| H | —

q_4 —| H | —

In the easy game mode, you can use the Hadamard (h) gate to return these states to the |0> state, and then you can always use a Pauli-X (x) gate to turn a |0> into a |1>. In our example, we then want to apply the gates as follows:

q_0 —| H | —
q_1 —| H | —
q_2 —| H | ——| H | —
q_3 —| H | ——| H | —
q_4 —| H | ——| H | ——| X | —

Now, you are ready to get going in the easy mode, just follow these simple steps. For the other modes, try to look for other combinations that can get you the h gate. Online sources like Qiskit, QuantumInspire, IBMQ, Microsoft Quantum etc. can help, or you can just use our built-in sim command to see how different circuits affect the probability of different cards.

