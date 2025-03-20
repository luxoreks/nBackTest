class ProgramState:
    START_PAGE = "StartPage"
    INSTRUCTION_PAGE = "InstructionPage"
    MAIN_TEST_PAGE = "MainTest"
    END_PAGE = "EndScreen"

    def __init__(self):

        self.START_PAGE = ProgramState.START_PAGE
        self.INSTRUCTION_PAGE = ProgramState.INSTRUCTION_PAGE
        self.MAIN_TEST_PAGE = ProgramState.MAIN_TEST_PAGE
        self.END_PAGE = ProgramState.END_PAGE

        self.current_state = self.START_PAGE
        self.program_states = [self.START_PAGE, self.INSTRUCTION_PAGE, self.MAIN_TEST_PAGE, self.END_PAGE]

    def change_state(self, new_state):
        match new_state:
            case self.START_PAGE:
                self.current_state = self.START_PAGE
            case self.INSTRUCTION_PAGE:
                self.current_state = self.INSTRUCTION_PAGE
            case self.MAIN_TEST_PAGE:
                self.current_state = self.MAIN_TEST_PAGE
            case self.END_PAGE:
                self.current_state = self.END_PAGE

    def get_current_state(self):
        return self.current_state