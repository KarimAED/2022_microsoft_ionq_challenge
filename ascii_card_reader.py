def row_splitter(string, length):
    return (string[0 + i : length + i] for i in range(0, len(string), length))


def get_ascii_cards(fname):
    with open(fname, "r") as file:
        rows = file.readlines()

    rows = [row.rstrip("\n") for row in rows]

    cards = [[] for _ in range(15)]
    for row in rows:
        split_row = row_splitter(row, 16)

        for i, val in enumerate(split_row):
            cards[i].append(val)

    return cards


CARDS = get_ascii_cards("ascii_cards.txt")


def get_card(num, suite):
    card = CARDS[num - 1].copy()

    card = [row.replace("X", suite) for row in card]

    return card


def join_cards(cards):
    card_data = [get_card(card[0], card[1]) for card in cards]

    joint = []

    for i in range(len(card_data[0])):
        joint.append("".join([c[i] for c in card_data]))

    return joint
