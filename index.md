# QuHackJack Casinos™
This is our submission with which we achieved 2nd place in the MIT iQuHack 2022 Microsoft IonQ Division.
<p>
  <a href="" target="_blank"><img src="https://user-images.githubusercontent.com/46804607/151706840-778c7238-9dac-4062-a6ab-a909ae9606c4.png" width="60%"/> </a>
</p>
Cheating with Quantum Computers since 2022

### The Team

[Karim Alaa El-Din ](https://www.linkedin.com/in/karimaed/)  

[Francesco Scala](https://www.linkedin.com/in/francesco-scala-839507211/)  

[Rabins Wosti](https://www.linkedin.com/in/rabins-wosti-703107152/)  

[Arunava Majumder](https://www.linkedin.com/in/arunava-majumder-33500a167/)  


### Introduction

- BlackJack is a game of chance where the player tries to reach a sum of 21 with his card values, without going over
- The player is opposed by a dealer, who plays by the same rules
- Whoever gets closer to 21 wins

But that's gambling, we can't allow that...

- Counting cards makes it a game of skill
- But it's hard and requires thinking

__Introducing: QuHackJack__

### Game Concept

- Use quantum computer to generate all random numbers
- Random numbers correspond to playing cards being drawn
- Allow the user to manipulate the quantum circuit before drawing a card, to change their odds

### Rules

- deck of 32 cards, values 3 to 10 and suits ♣, ♠, ♥, ♦
- The player and dealer compete to reach as close as possible to a total of 16, without going over
- Each card corresponds to a 5 q-bit computational basis state
- Random outcomes are achieved through a single hadamard gate on each q-bit

![hack_pt1](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/hack_pt1.png?raw=true)

- Different gamemodes allow player to apply different types & numbers of gates

__Gamemodes:__

EASY  
MEDIUM  
HARD  
ULTRA  
NOGATENOCRY  
WATERGATE  

Some have no element of luck, others have some! All require a good amount of puzzling.

### Featuring

- Newest Ascii Graphics

![first_draw](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/first_draw.png?raw=true)


- Dynamic Circuit editing

![hack_pt3](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/hack_pt3.png?raw=true)

- Simulating probability of cards for each circuit

![flat_distrib](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/flat_distrib.png?raw=true)

- Different Backends (Including __REAL__ IonQ QPU)

<p align="left">
  <a href="https://azure.microsoft.com/en-us/solutions/quantum-computing/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488491-609828a4-cd1f-4076-b5b2-a8d9fc2d0fa4.png" width="30%"/> </a>
  <a href="https://ionq.com/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488159-da95eb05-9277-4abe-b1ba-b49871d563ed.svg" width="20%" style="padding: 1%;padding-left: 5%"/></a>
</p>

- Comprehensive UI messages and tons of introduction

![help](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/help.png?raw=true)

### Achievements

- Created a fully-fletched, _fun_ game
- Useful as a teaching device (tried and tested on friends & family)
- Extensive documentation of quantum computing concepts & independent exploration of different gates
- Very fun puzzle game (We have spent some time puzzling ourselves)
- Tons of variety through random 1st cards & different gamemodes

### Potential improvements

- Limited to a non-standard deck by the use of q-bit basis
- Hardware noise may mess with the user, even if all the gates are correct (_It's NISQ, Baby!_)
- Queued jobs make the game quite slow
- The victory, loss messages could use some work

### Thoughts & Reflections

- Incredible Experience throughout
- Extremely creative & fun challenge (Thanks @Microsoft & @IonQ)
- Met people from all across the world (4 people, 4 timezones & countries)


## Thank you!
