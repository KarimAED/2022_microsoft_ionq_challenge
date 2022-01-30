# QuHackJack Casinos™
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

q_0 —| H | —  
q_1 —| H | —  
q_2 —| H | —  
q_3 —| H | —  
q_4 —| H | —  

- Different gamemodes allow player to apply different types & numbers of gates

__Gamemodes:__

EASY  
MEDIUM  
HARD  
ULTRA  
NOGATENOCRY  
WATERGATE  

### Featuring

- Newest Ascii Graphics

![first_draw](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/first_draw.png?raw=true)


- Dynamic Circuit editing

![hack_pt3](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/hack_pt3.png?raw=true)

- Simulating probability of cards for each circuit

![flat_distrib](https://github.com/KarimAED/2022_microsoft_ionq_challenge/blob/main/QuHackJack_pictures/flat_distrib.png?raw=true)

- Different Backends (Including __REAL__ IonQ QPU)

