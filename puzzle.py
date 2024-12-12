from logic import *

# Symbols representing whether each character is a Knight or a Knave
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),  # A is either a Knight or a Knave
    Not(And(AKnight, AKnave)),  # A cannot be both
    Implication(AKnight, And(AKnight, AKnave)),  # If A is a Knight, they tell the truth
    Implication(AKnave, Not(And(AKnight, AKnave)))  # If A is a Knave, they lie
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),  # A is either a Knight or a Knave
    Or(BKnight, BKnave),  # B is either a Knight or a Knave
    Not(And(AKnight, AKnave)),  # A cannot be both
    Not(And(BKnight, BKnave)),  # B cannot be both
    Implication(AKnight, And(AKnave, BKnave)),  # If A is a Knight, the statement is true
    Implication(AKnave, Not(And(AKnave, BKnave)))  # If A is a Knave, the statement is false
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),  # A is either a Knight or a Knave
    Or(BKnight, BKnave),  # B is either a Knight or a Knave
    Not(And(AKnight, AKnave)),  # A cannot be both
    Not(And(BKnight, BKnave)),  # B cannot be both
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),  # If A is a Knight, they tell the truth
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),  # If A is a Knave, they lie
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),  # If B is a Knight, they tell the truth
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))  # If B is a Knave, they lie
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),  # A is either a Knight or a Knave
    Or(BKnight, BKnave),  # B is either a Knight or a Knave
    Or(CKnight, CKnave),  # C is either a Knight or a Knave
    Not(And(AKnight, AKnave)),  # A cannot be both
    Not(And(BKnight, BKnave)),  # B cannot be both
    Not(And(CKnight, CKnave)),  # C cannot be both
    Implication(AKnight, AKnight),  # If A is a Knight, their statement is true
    Implication(AKnave, Not(AKnight)),  # If A is a Knave, their statement is false
    Implication(BKnight, And(
        Implication(AKnight, AKnave),  # If B is a Knight, A's statement is consistent
        CKnave  # B says C is a Knave
    )),
    Implication(BKnave, Not(And(
        Implication(AKnight, AKnave),
        CKnave
    ))),  # If B is a Knave, their statement is false
    Implication(CKnight, AKnight),  # If C is a Knight, A is a Knight
    Implication(CKnave, Not(AKnight))  # If C is a Knave, A is not a Knight
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")


if __name__ == "__main__":
    main()
