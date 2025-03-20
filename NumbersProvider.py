class NumbersProvider:
    def __init__(self):

        self.numbers = [5, 9, 5, 8, 8, 1, 4, 1, 2, 1, 3, 1, 3, 6, 2, 3, 2, 1, 6, 4, 9, 2, 9, 7, 6, 2, 3, 7, 1, 2, 5, 9, 2, 1,
                   2, 1, 9, 1, 5, 9, 5, 6, 7, 2, 7, 3, 3, 2, 3, 7, 9, 7, 6, 5, 5, 8, 5, 1, 1, 6, 8, 6, 3, 9, 9, 4, 2, 5,
                   2, 5, 3, 4, 3, 7, 1, 8, 2, 9, 2, 1, 7, 6, 3, 4, 5, 4, 9, 1, 7, 2, 7, 3, 7, 6, 3, 6, 5, 5, 3, 5, 1, 1,
                   9, 1, 3, 9, 7, 3, 7, 6, 4, 6, 5, 3, 4, 3, 5, 4, 3, 4, 6, 1, 7, 8, 8, 1, 8, 7, 5, 2, 5, 8, 5, 1, 3, 8,
                   3, 8, 9, 3, 9, 7, 6, 6, 8, 3, 8, 7, 8, 7, 6, 5, 3, 5, 4, 9, 3, 5, 2, 2, 8, 2, 3, 2, 8, 6, 4, 9, 4, 8,
                   6, 4, 6, 4, 8, 2, 7, 5, 7, 3]

        self.correct_answers = ['n', 'n', 'p', 'n', 'n', 'n', 'n', 'p', 'n', 'p', 'n', 'p', 'p', 'n', 'n', 'n', 'p', 'n',
                           'n', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'p', 'p',
                           'n', 'p', 'n', 'n', 'p', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'p', 'n', 'n', 'p', 'n', 'n',
                           'n', 'n', 'p', 'n', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'n', 'n', 'n', 'p', 'p', 'n', 'n',
                           'p', 'n', 'n', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'n',
                           'p', 'n', 'p', 'n', 'n', 'p', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'n',
                           'p', 'n', 'n', 'p', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'n', 'n', 'n',
                           'p', 'n', 'n', 'n', 'p', 'n', 'p', 'n', 'n', 'n', 'p', 'p', 'n', 'n', 'p', 'n', 'n', 'n',
                           'n', 'n', 'p', 'n', 'p', 'p', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'p',
                           'n', 'p', 'n', 'n', 'n', 'n', 'p', 'n', 'n', 'n', 'p', 'p', 'n', 'n', 'n', 'n', 'p', 'n']
        self.current_number_index = 0

    def get_next_number(self):
        if self.is_next_number_available():
            self.current_number_index += 1
            number = self.numbers[self.current_number_index]
            return number
        else:
            return None

    def get_first_number(self):
        self.current_number_index = 0
        return self.numbers[0]

    def get_answer(self):
        return self.correct_answers[self.current_number_index]

    def is_next_number_available(self):
        return self.current_number_index < (len(self.numbers)-1)

