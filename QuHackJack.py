import math
from qiskit import QuantumCircuit, execute, Aer
from qiskit.tools.monitor import job_monitor
from qiskit.circuit import Instruction, Qubit, QuantumRegister
from azure.quantum.qiskit import AzureQuantumProvider

import strings
from ascii_card_reader import join_cards
from strings import *

provider = AzureQuantumProvider(
  resource_id="/subscriptions/b1d7f7f8-743f-458e-b3a0-3e09734d716d/resourceGroups/aq-hackathons/providers/Microsoft.Quantum/Workspaces/aq-hackathon-01",
  location="eastus"
)

use_qpu = False

easy = {
  "allowed_gates": ["i", "h", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"],
  "number_gates": 20
}

no_gate_no_cry = {
  "allowed_gates": ["i", "h", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"],
  "number_gates": 4
}

watergate = {
  "allowed_gates": ["i", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "rz"],
  "number_gates": 6
}

medium = {
  "allowed_gates": ["i", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"],
  "number_gates": 10
}

hard = {
  "allowed_gates": ["i", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "rz"],
  "number_gates": 10
}

ultra = {
  "allowed_gates": ["i", "x", "y", "z", "s", "t", "sx", "sdg", "tdg"],
  "number_gates": 10
}

cl_screen = lambda: print("\n"*100)

class Game:

  intro = \
  """
Welcome to QuHackJack!

You can either start a game by typing PLAY, or set the game mode by typing EASY, MEDIUM, HARD, ULTRA or NOGATENOCRY.
To learn more about QuHackJack, type INFO. If you are stuck, type HELP. Alternatively, type QUIT to leave the game.
  """

  options_text = "The following options are available to you: "

  responses = ("PLAY", "EASY", "MEDIUM", "HARD", "HELP", "AER", "IONQ_SIM", "QPU",
               "ULTRA", "NOGATENOCRY", "WATERGATE", "QUIT", "INFO")

  difficulty_settings = {"EASY": easy, "MEDIUM": medium, "HARD": hard,
                         "ULTRA": ultra, "NOGATENOCRY": no_gate_no_cry, "WATERGATE": watergate}

  threshold = 16

  gates = ["i", "h", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]

  backend_names = ["AER", "IONQ_SIM", "QPU"]

  backends = {"AER": Aer.get_backend("qasm_simulator"), "IONQ_SIM": provider.get_backend("ionq.qpu"),
              "QPU": provider.get_backend("ionq.qpu")}

  def __init__(self):
    self.quit = False
    self.player_cards = []
    self.dealer_cards = []
    self.circuit = self.make_random_generator()
    self.difficulty = "EASY"
    self.diff_setting = easy
    self.backend = "AER"
    self.backend_setting = self.backends["AER"]


    while not self.quit:
      cl_screen()
      print(self.intro)
      print("Game mode is %s." % self.difficulty)
      print("Backend is %s." % self.backend)
      resp = input("What do you want to do? ").upper()
      if resp not in self.responses:
        self.invalid_input()
        continue
      if resp == "PLAY":
        self.play()
      elif resp == "QUIT":
        self.quit = True
      elif resp == "INFO":
        self.info()
      elif resp == "HELP":
        self.help()
      elif resp in self.backend_names:
        self.backend = resp
        self.backend_setting = self.backends[resp]
      else:
        self.difficulty = resp
        self.diff_setting = self.difficulty_settings[resp]

  def quit(self):
    self.quit = True

  def invalid_input(self):
    print("Sorry, I didn't understand that input! Try again.")
    input("Press enter to continue")

  def win(self):
    print("Congratulations, you beat the house against all odds!")

  def tie(self):
    print("Congratulations, you beat the house against all odds!")

  def loose(self):
    print("If you know your stats, you knew this was inevitable, really...")

  def info(self):
    cl_screen()
    print(strings.info)
    input("Please press enter to continue")

  def help(self):
    cl_screen()
    print(strings.help_str)
    input("Please press enter to continue")

  def make_random_generator(self):
      nqubits = 5
      
      qr = [i for i in range(nqubits)]
      qc = QuantumCircuit(nqubits)
      
      qc.h(qr)
      
      return qc

  def read_outcome(self, string):
      suits = ["♣", "♠", "♥", "♦"]

      num = int(string, 2)

      card_value = num // 4 + 3

      suit = num % 4

      card_suit = suits[suit]
      
      return card_value, card_suit

  def draw_random(self):
      
      qc = self.circuit
      
      qc.measure_all()
      
      job = execute(qc, self.backend_setting, shots = 1)

      job_monitor(job)

      count = job.result().get_counts()

      string = list(count.keys())[0]
      
      card_value, card_suit = self.read_outcome(string)
      
      return card_value, card_suit


  def simulate_circuit(self):

    qc = self.circuit.copy()

    qc.measure_all()

    job = execute(qc, Aer.get_backend("qasm_simulator"), shots=10_000)
    job_monitor(job)

    count = job.result().get_counts()

    parsed_count = {}

    for key, val in count.items():
      parsed_key = "".join([str(i) for i in self.read_outcome(key)])
      parsed_count[parsed_key] = val

    return parsed_count

  def show_sim(self):
    cl_screen()
    data = self.simulate_circuit()

    for key, val in sorted(data.items()):
      print(key + "\t" + "*"*(val//25))

    input("Press enter to continue")

  def check_score(self, cards):
    score = sum([c[0] for c in cards])
    if score > self.threshold:
      score = 0
    return score


  def player_turn(self):
    self.player_cards.append(self.draw_random())
    player_score = self.check_score(self.player_cards)

    return player_score
  

  def dealer_turn(self):
    self.dealer_cards.append(self.draw_random())
    dealer_score = self.check_score(self.dealer_cards)
    return dealer_score


  def show_state(self):
    cl_screen()
    sep = " "*40
    joint_player = join_cards(self.player_cards)
    joint_dealer = join_cards(self.dealer_cards)
    print("Your cards: " + sep + ((len(self.player_cards)-1)*16+4)*" " + "Dealer cards: ")
    for i in range(len(joint_player)):
      print(joint_player[i] + sep + joint_dealer[i])
    print("Your total: %i" % self.player_score + sep
          + ((len(self.player_cards)-1)*16+4)*" " + "Dealer total: %i" % self.dealer_score)

  def gate_manipulation(self):
    add_gates = True
    while add_gates:
      cl_screen()
      print("Here is the circuit for the Quantum Random Number Generator. Now it's time to hack this thing!")
      print("Reminder: your total is %i." % self.player_score)
      print(self.circuit)
      print("Available gates: %s" % str(self.diff_setting["allowed_gates"]))
      print("You have %i gates left for this turn." % self.num_gates)
      gate = input("Please enter desired gate (leave blank to run circuit or enter 'sim' to simulate probabilities): ")
      if gate == "":
        add_gates = False
        continue
      if gate == "sim":
        self.show_sim()
        continue
      elif gate not in self.gates:
        print("I don't know that gate...")
        continue
      elif gate not in self.diff_setting["allowed_gates"]:
        print("Nice try, but that gate is not available at your difficulty.")
        continue
      qubit = int(input("Please enter the qubit to apply "+gate+" to: "))

      self.num_gates -= 1
      params = []
      if "r" in gate:
        phase = float(input("Enter the rotation angle for %s rotation (in π radians): " % gate))
        params.append(phase * math.pi)

      self.circuit.data.append((Instruction(name=gate, num_qubits=1, num_clbits=0, params=params),
                                [Qubit(QuantumRegister(self.circuit.num_qubits, 'q'), qubit)],
                                []))

  def play(self):
    self.num_gates = self.diff_setting["number_gates"]
    self.circuit = self.make_random_generator()
    self.player_cards = []
    self.dealer_cards = []
    keep_playing = True

    print("Let's start this game!")
    self.player_score = self.player_turn()
    self.circuit = self.make_random_generator()
    self.dealer_score = self.dealer_turn()

    while keep_playing:
        self.show_state()
        self.circuit = self.make_random_generator()
        resp = input("Do you want another card (Y/N)?")
        if resp.upper() == "Y":
          self.gate_manipulation()
          self.player_score = self.player_turn()
        elif resp.upper() == "N":
          keep_playing = False
        if self.player_score == 0:
          self.loose()
          return
    
    while (self.dealer_score < 12 or self.dealer_score < self.player_score) and self.dealer_score != 0:
      self.circuit = self.make_random_generator()
      self.dealer_score = self.dealer_turn()
      self.show_state()

    if self.player_score > self.dealer_score:
      self.win()
    elif self.player_score == self.dealer_score:
      if len(self.player_cards) < len(self.dealer_cards):
        self.win()
      elif len(self.player_cards) == len(self.dealer_cards):
        self.tie()
    else:
      self.loose()
    input("Press enter to continue")


if __name__ == "__main__":
  Game()