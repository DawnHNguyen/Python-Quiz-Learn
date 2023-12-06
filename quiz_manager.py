import random

class QuizManager:
    def __init__(self, filename):
        self.questions = []
        self.answers = []
        self.load_quiz_data(filename)
        self.current_index = 0

    def load_quiz_data(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            quiz_content = file.read()
            quiz_items = quiz_content.split('\n\n')
            random.shuffle(quiz_items)

            for item in quiz_items:
                parts = item.split('-----')
                if len(parts) == 2:
                    self.questions.append(parts[0].strip())
                    self.answers.append(parts[1].strip())

    def get_current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def get_current_answer(self):
        if self.current_index < len(self.answers):
            return self.answers[self.current_index]
        return None

    def next_question(self):
        if self.current_index < len(self.questions) - 1:
            self.current_index += 1

    def previous_question(self):
        if self.current_index > 0:
            self.current_index -= 1
