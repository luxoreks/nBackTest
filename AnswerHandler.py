from functools import partial
import time
from PyQt5.QtCore import QTimer

from ExcelWriter import ExcelWriter
from ProgramState import ProgramState
from constants.text import TEXT_TO_EXCEL_LEFT_ANSWER, TEXT_TO_EXCEL_RIGHT_ANSWER


class AnswerHandler:
    def __init__(self):
        self.DEFAULT_TEXT_COLOR = 12
        self.HIGHLIGHT_TEXT = 13

        self.Z_KEY_NATIVE_CODE = 44
        self.M_KEY_NATIVE_CODE = 50
        self.C_KEY_NATIVE_CODE = 46
        self.R_KEY_NATIVE_CODE = 19

        self.LEFT_CTRL_NATIVE_CODE = 29
        self.RIGHT_CTRL_NATIVE_CODE = 285

        self.test_duration_time = 60000 # 1 min in milliseconds
        self.DELAY_BETWEEN_NUMBERS = 1

        self.LEFT_ANSWER_KEY = self.Z_KEY_NATIVE_CODE
        self.RIGHT_ANSWER_KEY = self.C_KEY_NATIVE_CODE

        self.LEFT_ANSWER = TEXT_TO_EXCEL_LEFT_ANSWER
        self.RIGHT_ANSWER = TEXT_TO_EXCEL_RIGHT_ANSWER

        self.excel_writer = ExcelWriter()
        self.human_answers = []
        self.reaction_time = []
        self.correct_answers = []
        self.previous_time = time.time()
        self.test_ended = False

    def process_answer(self, program_window, keyboard_key, program_state):

        match program_state:
            case ProgramState.START_PAGE:
                if not program_window.questionnaire_window_exist and self._is_answer_key(keyboard_key):
                    program_window.next_state()
                else:
                    pass
            case ProgramState.INSTRUCTION_PAGE:
                # if self._is_answer_key(keyboard_key):
                #     widget = self._get_layout_widget(program_window, keyboard_key)
                #     self.simulate_answer_registration(program_window, widget)
                pass
            case ProgramState.MAIN_TEST_PAGE:
                if self._is_answer_key(keyboard_key):
                    correct_answer = program_window.number_provider.get_answer()
                    self.correct_answers.append(correct_answer)
                    widget = self._get_layout_widget(program_window, keyboard_key)
                    human_answer = self.LEFT_ANSWER if keyboard_key == self.LEFT_ANSWER_KEY else self.RIGHT_ANSWER
                    is_answer_correct = correct_answer == human_answer
                    self.register_answer(program_window, widget, human_answer, is_answer_correct)
            case ProgramState.END_PAGE:
                if keyboard_key == self.R_KEY_NATIVE_CODE:
                    program_window.reset_test()
                    self._set_variables_to_default()

    def register_answer(self, program_window, widget, human_answer, correct_answer):
        program_window.key_pressed = True
        self._measure_time()
        QTimer.singleShot(1000, partial(self._continue_test, program_window, widget))
        program_window.highlight_chosen_answer(widget, correct_answer)
        self.human_answers.append(human_answer)

    def simulate_answer_registration(self, program_window, widget):
        program_window.key_pressed = True
        self.previous_time = time.time()
        QTimer.singleShot(1000, partial(self._go_to_main_test, program_window, widget))
        program_window.highlight_chosen_answer(widget)

    def set_current_time(self):
        self.previous_time = time.time()

    def start_countdown(self):
        QTimer.singleShot(self.test_duration_time, self._end_test)

    def _end_test(self):
        self.test_ended = True

    def _get_layout_widget(self, program_window, keyboard_key):
        widget_pos = -1
        match keyboard_key:
            case self.LEFT_ANSWER_KEY:
                widget_pos = 0
            case self.RIGHT_ANSWER_KEY:
                widget_pos = 2
            case _:
                pass
        widget = program_window.main_test_page_layout.itemAtPosition(2, widget_pos).widget()
        return widget

    def _is_answer_key(self, keyboard_key):
        return keyboard_key == self.LEFT_ANSWER_KEY or keyboard_key == self.RIGHT_ANSWER_KEY

    def _measure_time(self):
        current_time = time.time()
        diff = current_time - self.previous_time
        self.previous_time = current_time
        self.reaction_time.append(diff)
        print(str(self.reaction_time)) #########################

    def _go_to_main_test(self, program_window, widget):
        program_window.main_labels_manager.change_bottom_label_text_color(widget, self.DEFAULT_TEXT_COLOR)
        program_window.change_number()
        program_window.next_state()

    def _continue_test(self, program_window, widget):
        program_window.key_pressed = False
        program_window.main_labels_manager.change_bottom_label_text_color(widget, self.DEFAULT_TEXT_COLOR)
        print(program_window.number_provider.is_next_number_available())
        if program_window.number_provider.is_next_number_available() and not self.test_ended:
            program_window.change_number()
        else:
            relevant_human_answers = self.human_answers[2:]
            relevant_reaction_time = self.reaction_time[2:]
            relevant_correct_answers = self.correct_answers[2:]
            correct_reaction_time = [x - self.DELAY_BETWEEN_NUMBERS for x in relevant_reaction_time[1:]]
            self.excel_writer.save_data_to_excel(relevant_correct_answers, relevant_human_answers, relevant_reaction_time, program_window.current_person)
            program_window.next_state()

    def _set_variables_to_default(self):
        self.human_answers = []
        self.reaction_time = []
        self.correct_answers = []
        self.test_ended = False
