import tkinter as tk
from quiz_manager import QuizManager
from tkinter.font import Font

class QuizApp(tk.Tk):
    def __init__(self, quiz_manager):
        super().__init__()
        self.quiz_manager = quiz_manager
        self.title("Quiz App")
        self.geometry("1080x720")

        large_font = Font(family="Helvetica", size=14)
        
        self.question_label = tk.Label(self, text="", wraplength=1000, font=large_font)
        self.question_label.pack(pady=20)

        self.answer_label = tk.Label(self, text="", wraplength=1000, font=large_font)
        self.answer_label.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        self.previous_button = tk.Button(button_frame, text="Previous Question", command=self.previous_question, font=large_font)
        self.previous_button.pack(side=tk.LEFT, padx=10)

        self.show_answer_button = tk.Button(button_frame, text="Show Answer", command=self.show_answer, font=large_font)
        self.show_answer_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(button_frame, text="Next Question", command=self.next_question, font=large_font)
        self.next_button.pack(side=tk.LEFT, padx=10)
        
        self.bind("<Left>", lambda event: self.previous_question())
        self.bind("<Right>", lambda event: self.next_question())
        self.bind("<space>", lambda event: self.show_answer())

        self.update_question()

    def update_question(self):
        question = self.quiz_manager.get_current_question()
        self.question_label.config(text=question)
        self.answer_label.config(text="")

    def show_answer(self):
        answer = self.quiz_manager.get_current_answer()
        self.answer_label.config(text=f"Answer: {answer}")

    def next_question(self):
        self.quiz_manager.next_question()
        self.update_question()

    def previous_question(self):
        self.quiz_manager.previous_question()
        self.update_question()

if __name__ == "__main__":
    quiz_manager = QuizManager("LSD.txt")
    app = QuizApp(quiz_manager)
    app.mainloop()
