from quiz import Quiz
from config import IONIAN_FORMULA, NOTES, MODES


def main():
    q = Quiz()
    q.interval_guess(3)


def main2():
    starting_note = "C"
    for n in range(7):
        formula = list(IONIAN_FORMULA[n:]+IONIAN_FORMULA[:n])
        semitones = []
        steps_taken = 0
        notes = []
        for step in formula:
            semitones.append(steps_taken)
            notes.append(NOTES[steps_taken])
            if step == "W":
                steps_taken += 2
            else:
                steps_taken += 1
        print(semitones)
        print(starting_note, MODES[n], notes)


if __name__ == '__main__':
    main()
