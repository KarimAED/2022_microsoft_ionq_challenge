# Welcome to the QuHackJack Casinos™!

<p align="left">
  <a href="https://azure.microsoft.com/en-us/solutions/quantum-computing/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488491-609828a4-cd1f-4076-b5b2-a8d9fc2d0fa4.png" width="30%"/> </a>
  <a href="https://ionq.com/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488159-da95eb05-9277-4abe-b1ba-b49871d563ed.svg" width="20%" style="padding: 1%;padding-left: 5%"/></a>
  <a href="https://iquhack.mit.edu/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151647370-d161d5b5-119c-4db9-898e-cfb1745a8310.png" width="8%" style="padding-left: 5%"/> </a>
  <a href="" target="_blank"><img src="https://user-images.githubusercontent.com/46804607/151706840-778c7238-9dac-4062-a6ab-a909ae9606c4.png" width="60%"/> </a>
</p>

## INTRODUCTION

Welcome! Not quite sure where to start? Never even heard of quantum computing? No problem, we are always glad to help here at QuHackJack Casinos™.

We are a bunch of geeks who are taking the initiative to teach quantum operations for fun. Here you will learn how to implement quantum gates not through the usual but through a fun game using our game names QuHackJack.


This is where you can experience the weird world of quantum superposition at play! You can use the quantum tricks provided to you in the form of allowed gates at each level to rig the roulette to your advantage. Alright, with this superpower, come and use the quantum to bag yourself a huge amount! 

## Installation & Execution (The boring part)

To run the game, first clone this repository. Then make sure that the following requirements are installed:

qiskit  
azure-quantum

From pip version 10.0, you can install these directly from the pyproject.toml, or alternatively a package manager like poetry can be used.

Credentials for the aq-hackathon-01 resource group are required from the user, even though another resource group can be selected by manually editing the global provider in the QuHackJack.py file.

For a simulated backend, we strongly recommend the local Aer simulator over the hosted Ionq simulator, as there is no queue time. The IONQ_SIM and QPU backends can have long queue times for individual moves. We definitely recommend trying out the QPU backend for the feeling of ruling the world, and playing QuHackJack on god’s own legos.

Once the installation is complete, simply run QuHackJack.py to start the game. Enjoy!



## Game Basics

QuHackJack is a BlackJack inspired card game in which the player has to use the laws of quantum mechanics to win. The game itself seems simple: you draw cards, and try to get the sum of their values, e.g. 7 for a 3 and a 4, as close as possible to 16, without exceeding it. The house plays too, in the form of a dealer that draws cards against you.

Of course, you can cheat in BlackJack by counting cards - but that’s sooo last century. We offer you the unique experience of breaking the game by bending the rules of reality itself to your will.

Our deck consists of 32 cards, the values range from 3 to 10. They have the usual suits: clubs (♣), diamonds (♦), hearts (♥), and spades (♠). 

Initially each card has equal probability of being drawn and after every draw the card is put back in the deck. So, the player picks the first card at random. After this first move, the dealer draws a card for his own too.

Now the Quantum Fun begins. It turns out that this casino uses a quantum computer to generate their random cards! But they were a bit sloppy and didn’t secure it properly against access by the player. From the second card onwards, the player gets the chance to modify the state of the quantum computer that generates the cards to cheat the game. This is made possible as each card maps to a state of the quantum computer based on the binary string of the state. Counting up from 00000 we first see the 4 different 3s, then the 4 different 4s and so on. The state 01001 for example corresponds to 5♠.

By default, the quantum computer is always in the completely random superposition of all possible outcomes, making them all equally likely, as in a normal card game. This is achieved through 5 initial Hadamard gates. The player then gets to modify the circuit, and depending on the game mode, he has different kinds and numbers of gates available:

EASY: 			20	["h", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]

MEDIUM:		10	["x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]

HARD: 		10	["x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "rz"]

ULTRA:		10	["x", "y", "z", "s", "t", "sx", "sdg", "tdg"]

NOGATENOCRY: 	4	["h", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]

WATERGATE: 	6	["x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "rz"]

While editing the circuit for their next card, the player can also simulate the expected cards (on a Qiskit Aer backend for speed), to learn how different gates impact the state and the probability of different cards. Then, once you are ready, you can submit your circuit, get your card, and beat that dealer all the time.

## Game Guide

As the program is launched, you will be redirected to the Microsoft Azure login page. Once you log in, a welcome message is printed. Then, you can choose a game mode by typing the suggested string and the desired backend. Both lower and upper case strings work. Both "INFO" and "HELP" commands are available for further information.

![initial_message](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/initial_message.png?raw=true)


Once you type "PLAY", a first random card is drawn for both you and the dealer.

![play](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/play.png?raw=true)

Soon after (timing is backend dependent), the cards are shown, and the game asks you if you want another card.

![first_draw](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/first_draw.png?raw=true)

If you do, you can type "Y" and have the chance to apply gates and modify the probability distribution. A reminder of your current total is printed and then the present quantum circuit is shown. The available gates as well as the number of operations that you can apply is also presented.

![hack_pt1](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/hack_pt1.png?raw=true)

At this stage, you can choose to apply a gate operation, to simulate the present probability distribution or to run the circuit. If you are stuck here, you can type help on the main screen and receive a message that will help you to understand the logic of the game.

![help](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/help.png?raw=true)

If you immediately use "sim", you will see a probability distribution that is almost perfectly flat.

![flat_distrib](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/flat_distrib.png?raw=true)

But if you apply some gates, e.g. rotations around Y axis, things start to change. In order to add one gate you have to specify the name of the gate and then the qubit index. If the gate is a rotation then also the angle (in 𝜋 radians) is required.

![hack_pt3](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/hack_pt3.png?raw=true)

![hack_pt4](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/hack_pt4.png?raw=true)

You can always check your probability distribution again with "sim":

![hacked_distrib](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/hacked_distrib.png?raw=true)

When you are satisfied with the obtained probability distribution, you can run the circuit to draw your card.

![2nd_draw](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/2nd_draw.png?raw=true)

Then you can try to hack another card or leave the dealer to finish the game.

![dealer_final_move](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/dealer_final_move.png?raw=true)

After the game is finished, you are returned back to the main menu.


## The QuHackJack team:

[Karim Alaa El-Din ](https://www.linkedin.com/in/karimaed/)  

[Francesco Scala](https://www.linkedin.com/in/francesco-scala-839507211/)  

[Rabins Wosti](https://www.linkedin.com/in/rabins-wosti-703107152/)  

[Arunava Majumder](https://www.linkedin.com/in/arunava-majumder-33500a167/)  
