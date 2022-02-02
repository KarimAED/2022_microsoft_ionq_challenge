import math, time
from qiskit import QuantumCircuit, execute, Aer
from qiskit.tools.monitor import job_monitor
from qiskit.circuit import Instruction, Qubit, QuantumRegister
from azure.quantum.qiskit import AzureQuantumProvider

import strings
from ascii_card_reader import join_cards

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

cl_screen = lambda: print("\n" * 100)


class QuantumDeck:

    def __init__(self, backend):
        self.circuit = self.make_random_generator()
        self.backend = backend

    def __str__(self):
        return self.circuit.__str__()

    @staticmethod
    def make_random_generator():
        nqubits = 5

        qr = [i for i in range(nqubits)]
        qc = QuantumCircuit(nqubits)

        qc.h(qr)

        return qc

    @staticmethod
    def read_outcome(string):
        suits = ["♣", "♠", "♥", "♦"]

        num = int(string, 2)

        card_value = num // 4 + 3

        suit = num % 4

        card_suit = suits[suit]

        return card_value, card_suit

    def reset(self):
        self.circuit = self.make_random_generator()

    def add_gate(self, gate, qubit, params):
        self.circuit.data.append((Instruction(name=gate, num_qubits=1, num_clbits=0, params=params),
                                  [Qubit(QuantumRegister(self.circuit.num_qubits, 'q'), qubit)],
                                  []))

    def draw(self):

        qc = self.circuit

        qc.measure_all()

        job = execute(qc, self.backend, shots=1)

        job_monitor(job)

        count = job.result().get_counts()

        string = list(count.keys())[0]

        card_value, card_suit = self.read_outcome(string)

        self.reset()

        return card_value, card_suit

    def initial_draws(self):

        initial_stack = []

        qc = self.circuit

        qc.measure_all()

        job = execute(qc, self.backend, shots=10)

        job_monitor(job)

        count = job.result().get_counts()

        for key, val in count.items():
            for i in range(val):
                initial_stack.append(self.read_outcome("".join(key.split(" "))))

        self.reset()

        return initial_stack

    def simulate(self):

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


class Game:
    options_text = "The following options are available to you: "

    responses = ("PLAY", "EASY", "MEDIUM", "HARD", "HELP", "AER", "IONQ_SIM", "QPU",
                 "ULTRA", "NOGATENOCRY", "WATERGATE", "QUIT", "INFO")

    difficulty_settings = {"EASY": easy, "MEDIUM": medium, "HARD": hard,
                           "ULTRA": ultra, "NOGATENOCRY": no_gate_no_cry, "WATERGATE": watergate}

    threshold = 16

    gates = ["i", "h", "x", "y", "z", "s", "t", "sx", "sdg", "tdg", "rx", "ry", "rz"]

    backend_names = ["AER"]  # , "IONQ_SIM", "QPU"]

    backends = {"AER": Aer.get_backend("qasm_simulator")}
    # , "IONQ_SIM": provider.get_backend("ionq.qpu"), "QPU": provider.get_backend("ionq.qpu")}

    def __init__(self):
        self.quit = False
        self.player_cards = []
        self.dealer_cards = []
        self.difficulty = None
        self.diff_setting = None
        self.backend = None
        self.deck = None
        self.set_difficulty("EASY")
        self.set_backend("AER")

        while not self.quit:
            cl_screen()
            print(strings.intro)
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
                self.set_backend(resp)
            else:
                self.set_difficulty(resp)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.diff_setting = self.difficulty_settings[difficulty]

    def set_backend(self, backend):
        self.backend = backend
        self.deck = QuantumDeck(self.backends[backend])

    @staticmethod
    def invalid_input():
        print("Sorry, I didn't understand that input! Try again.")
        input("Press enter to continue")

    @staticmethod
    def win():
        print("\n\n" + "#"*100)
        print("Congratulations, you beat the house against all odds!")
        print("#" * 100 + "\n\n")

    @staticmethod
    def tie():
        print("\n\n" + "#"*100)
        print("Odd, I don't remember a draw as an option... But there you have it: a tie.")
        print("#" * 100 + "\n\n")

    @staticmethod
    def loose():
        print("\n\n" + "#"*100)
        print("If you know your stats, you knew this was inevitable, really...")
        print("#" * 100 + "\n\n")

    @staticmethod
    def info():
        cl_screen()
        print(strings.info)
        input("Please press enter to continue")

    @staticmethod
    def help():
        cl_screen()
        print(strings.help_str)
        input("Please press enter to continue")

    def show_sim(self):
        cl_screen()
        print("Simulating...")
        data = self.deck.simulate()

        for key, val in sorted(data.items()):
            print(key + "\t" + "*" * (val // 25))

        input("Press enter to continue")

    def check_score(self, cards):
        score = sum([c[0] for c in cards])
        if score > self.threshold:
            score = 0
        return score

    def player_turn(self):
        self.player_cards.append(self.deck.draw())
        player_score = self.check_score(self.player_cards)

        return player_score

    def dealer_turn(self, stack):
        self.dealer_cards.append(stack.pop())
        dealer_score = self.check_score(self.dealer_cards)
        return dealer_score

    def show_state(self):
        cl_screen()
        sep = " " * 40
        joint_player = join_cards(self.player_cards)
        joint_dealer = join_cards(self.dealer_cards)
        print("*"*100)
        print("QuHackJack Casinos presents: QuHackJack")
        print("*"*100)
        print("\nMaximum total: 16\n\n")
        print("Your cards: " + sep + ((len(self.player_cards) - 1) * 16 + 4) * " " + "Dealer cards: ")
        for i in range(len(joint_player)):
            print(joint_player[i] + sep + joint_dealer[i])
        print("Your total: %i" % self.player_score + sep
              + ((len(self.player_cards) - 1) * 16 + 4) * " " + "Dealer total: %i" % self.dealer_score)

    def gate_manipulation(self):
        add_gates = True
        while add_gates:
            cl_screen()
            print("Here is the circuit for the Quantum Random Number Generator. Now it's time to hack this thing!")
            print("Reminder: your total is %i." % self.player_score)
            print(self.deck)
            print("Available gates: %s" % str(self.diff_setting["allowed_gates"]))
            print("You have %i gates left for this turn." % self.num_gates)
            gate = input(
                "Please enter desired gate (leave blank to run circuit or enter 'sim' to simulate probabilities): ")
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
            qubit = int(input("Please enter the qubit to apply " + gate + " to: "))

            self.num_gates -= 1
            if self.num_gates == 0:
                add_gates = False
            params = []
            if "r" in gate:
                phase = float(input("Enter the rotation angle for %s rotation (in π radians): " % gate))
                params.append(phase * math.pi)

            self.deck.add_gate(gate, qubit, params)

    def play(self):
        self.num_gates = self.diff_setting["number_gates"]
        stack = self.deck.initial_draws()
        self.player_cards = []
        self.dealer_cards = []
        keep_playing = True

        print("Let's start this game!")
        self.player_cards.append(stack.pop())
        self.player_score = self.check_score(self.player_cards)
        self.dealer_score = self.dealer_turn(stack)

        while keep_playing:
            self.show_state()
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
            print("Dealer is drawing...")
            time.sleep(3)
            self.dealer_score = self.dealer_turn(stack)
            self.show_state()

        if self.player_score > self.dealer_score:
            self.win()
        elif self.player_score == self.dealer_score:
            self.tie()
        else:
            self.loose()
        input("Press enter to continue")


if __name__ == "__main__":
    Game()
