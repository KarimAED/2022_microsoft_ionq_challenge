info = """
Welcome to the QuHackJack!

This is where you can experience the weird world of quantum superposition at play!
You can use the quantum tricks provided to you in the form of allowed gates at each level to rig the roulette
to your advantage. Alright, with this superpower, come and use the quantum to bag yourself a huge amount! 

QuHackJack is a BlackJack inspired card game in which the player has to use the laws of quantum mechanics to win.
The game itself seems simple: you draw cards, and try to get the sum of their values, e.g. 7 for a 3 and a 4,
as close as possible to 16, without exceeding it. The house plays too,
in the form of a dealer that draws cards against you.

Of course, you can cheat in BlackJack by counting cards - but that’s sooo last century.
We offer you the unique experience of breaking the game by bending the rules of reality itself to your will.

Our deck consists of 32 cards, the values range from 3 to 10.
They have the usual suits: clubs (♣), diamonds (♦), hearts (♥), and spades (♠). 

Initially each card has equal probability of being drawn and after every draw the card is put back in the deck.
So, the player picks the first card at random. After this first move, the dealer draws a card for his own too.

Now the Quantum Fun begins. It turns out that this casino uses a quantum computer to generate their random cards!
But they were a bit sloppy and didn’t secure it properly against access by the player.
From the second card onwards, the player gets the chance to modify the state of the quantum computer
that generates the cards to cheat the game. This is made possible as each card maps to a state of the quantum computer 
based on the binary string of the state. Counting up from 00000 we first see the 4 different 3s,
then the 4 different 4s and so on. The state 01001 for example corresponds to 5♠.

By default, the quantum computer is always in the completely random superposition of all possible outcomes,
making them all equally likely, as in a normal card game. This is achieved through 5 initial Hadamard gates.
The player then gets to modify the circuit, and depending on the game mode,
he has different kinds and numbers of gates available:

EASY:          20    ["h", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]
MEDIUM:        10    ["x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]
HARD:          10    ["x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "rz"]
ULTRA:         10    ["x", "y", "z", "s", "t", "sx", "sdg", "tdg"]
NOGATENOCRY:   4     ["h", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]
WATERGATE:     6     ["x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "rz"]

While editing the circuit for their next card, the player can also simulate the expected cards(on a Qiskit Aer
backend for speed), to learn how different gates impact the state and the probability of different cards.
Then, once you are ready, you can submit your circuit, get your card, and beat that dealer all the time.
"""

help_str = """
Not quite sure where to start? Never even heard of quantum computing?
No problem, we are always glad to help here at QuHackJack Casinos™.

In QuHackJack, the random cards, ranging from 3 to 10 with the 4 classic suits, are generated from a quantum computer.
Now, our quantum computer doesn’t know the cards by their numbers and suits, but instead by different states,
each of them labeled by a different 5-bit string, such as 01110.
Then, how do we map from these bit strings to the cards? It’s quite easy, actually.

Out of the 5 bits, the last 2 are used to indicate the suit:
00 for ♣, 01 for ♠, 10 for ♥ and 11 for ♦.
The other 3 bits then form a binary number ranging from 0 (represented by 000) to 7 (represented by 111).
The exact mapping looks like this:

000 - 0        010 - 2        100 - 4        110 - 6
001 - 1        011 - 3        101 - 5        111 - 7

To get from these numbers to the cards in the range 3 to 10, we add another 3 to the decoded binary value.

To understand how this works, let us walk through an example. Let’s say your first number was a 9 and
now you want to reach the goal of 16 exactly in just one more card. To do this, you of course need to draw a 7.

By our above logic, that 7 actually looks like a 4 to the quantum computer, represented by the binary combination 100.
That is what we are trying to get in our quantum computing!

Now of the 5 bits in our full bitstrings, these actually correspond to the quantum computer q-bits read in this order:

q_4    q_3    q_2    q_1    q_0

So, if we want to get our 7, we know that we want a bit string like 100xx where x denotes the suit bits,
which don’t matter to win the game. To get this, we need to reach the following states in the qubits:

q_2    |0>
q_3    |0>
q_4    |1>

Now, the initial circuit looks like

q_0 —| H | —
q_1 —| H | —
q_2 —| H | —
q_3 —| H | —
q_4 —| H | —

In the easy game mode, you can use the Hadamard (h) gate to return these states to the |0> state,
and then you can always use a Pauli-X (x) gate to turn a |0> into a |1>.
In our example, we then want to apply the gates as follows:

q_0 —| H | —
q_1 —| H | —
q_2 —| H | ——| H | —
q_3 —| H | ——| H | —
q_4 —| H | ——| H | ——| X | —

Now, you are ready to get going in the easy mode, just follow these simple steps. For the other modes,
try to look for other combinations that can get you the h gate. Online sources like Qiskit, QuantumInspire, IBMQ,
Microsoft Quantum etc. can help, or you can just use our built-in sim command to see how
different circuits affect the probability of different cards.

"""

intro = """
****************************************************************************************************
Welcome to QuHackJack!
****************************************************************************************************

You can either start a game by typing PLAY, or set the game mode by typing the keywords EASY, MEDIUM, HARD, ULTRA,
NOGATENOCRY and WATERGATE. Optimizing the circuit to draw the favorable card gets harder with each difficulty level.
Here is the number and the list of allowed gates with their keywords for each difficulty level.

EASY:             20    ["h", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]
MEDIUM:        10    ["x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]
HARD:         10    ["x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "rz"]
ULTRA:        10    ["x", "y", "z", "s", "t", "sx", "sdg", "tdg"]
NOGATENOCRY:      4    ["h", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]
WATERGATE:      6    ["x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "rz"]

Keywords for using the available backends to run the game: 
AER : Aer Qasm Simulator
IONQ_SIM : Ionq simulator (deactivated, requires valid credentials)
QPU : Ionq QPU (deactivated, requires valid credentials)

You can check your odds of winning by running the game on simulators and then execute on the real hardware.
Note that results on the real hardware are subject to noise and long queues. It's the NISQ era!

To learn more about QuHackJack, type INFO. If you are stuck, type HELP. Alternatively, type QUIT to leave the game.

"""
