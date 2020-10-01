import random
import time

from config import NOTES, INTERVALS
from note import Note


class Quiz(object):
    def __init__(self):
        pass

    def interval_guess(self, num_of_games):
        start = time.time()
        num_correct = 0
        for _ in range(num_of_games):
            low_note = Note(random.choice(NOTES))
            semitones = random.choice(range(len(INTERVALS)))
            note_to_guess = Note(low_note.up(semitones))

            question = self.ask_interval_question(low_note, semitones)
            if self.handle_interval_response(low_note, note_to_guess, question, semitones):
                num_correct += 1
        print(f"Answered {num_correct} correct in {round(time.time()-start, 2)} seconds.")

    @staticmethod
    def handle_interval_response(low_note, note_to_guess, question, semitones):
        correct = True
        answer = False
        while not answer:
            resp = input(question)
            if resp == note_to_guess.name or resp == note_to_guess.enharmonic:
                print('Correct!')
                answer = True
            elif resp.lower() == 'n':
                print(f"{low_note} up by {semitones} semitones is {note_to_guess.name} ({INTERVALS[semitones]})")
                return False
            else:
                print('Incorrect!')
                correct = False
        return correct

    @staticmethod
    def ask_interval_question(low_note, semitones):
        question_type = random.choice([1, 2])
        question = "What is "
        if question_type == 1:
            question += f"{semitones} semitone"
            if semitones != 1:
                question += "s"
        else:
            question += f"a {INTERVALS[semitones]}"
        question += f" higher than {low_note.name}? (Type 'n' to give up)\n"
        return question
