from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_one.clicked.connect(lambda: self.one())
        self.button_two.clicked.connect(lambda: self.two())
        self.button_three.clicked.connect(lambda: self.three())
        self.button_four.clicked.connect(lambda: self.four())
        self.button_five.clicked.connect(lambda: self.five())
        self.button_six.clicked.connect(lambda: self.six())
        self.button_seven.clicked.connect(lambda: self.seven())
        self.button_eight.clicked.connect(lambda: self.eight())
        self.button_nine.clicked.connect(lambda: self.nine())
        self.button_zero.clicked.connect(lambda: self.zero())
        self.button_divide.clicked.connect(lambda: self.divide())
        self.button_muitply.clicked.connect(lambda: self.multiply())
        self.button_subtract.clicked.connect(lambda: self.subtract())
        self.button_add.clicked.connect(lambda: self.add())
        self.button_equal.clicked.connect(lambda: self.equal())
        self.button_back.clicked.connect(lambda: self.back())
        self.button_clear.clicked.connect(lambda: self.clear())

    def one(self) -> None:
        """
        Method for button one
        """
        equation = self.label_equation.text()
        equation += '1'
        self.label_equation.setText(equation)

    def two(self) -> None:
        """
        Method for button two
        """
        equation = self.label_equation.text()
        equation += '2'
        self.label_equation.setText(equation)

    def three(self) -> None:
        """
        Method for button three
        """
        equation = self.label_equation.text()
        equation += '3'
        self.label_equation.setText(equation)

    def four(self) -> None:
        """
        Method for button four
        """
        equation = self.label_equation.text()
        equation += '4'
        self.label_equation.setText(equation)

    def five(self) -> None:
        """
        Method for button five
        """
        equation = self.label_equation.text()
        equation += '5'
        self.label_equation.setText(equation)

    def six(self) -> None:
        """
        Method for button six
        """
        equation = self.label_equation.text()
        equation += '6'
        self.label_equation.setText(equation)

    def seven(self) -> None:
        """
        Method for button seven
        """
        equation = self.label_equation.text()
        equation += '7'
        self.label_equation.setText(equation)

    def eight(self) -> None:
        """
        Method for button eight
        """
        equation = self.label_equation.text()
        equation += '8'
        self.label_equation.setText(equation)

    def nine(self) -> None:
        """
        Method for button nine
        """
        equation = self.label_equation.text()
        equation += '9'
        self.label_equation.setText(equation)

    def zero(self) -> None:
        """
        Method for button zero
        """
        equation = self.label_equation.text()
        equation += '0'
        self.label_equation.setText(equation)

    def divide(self) -> None:
        """
        Method for button divide
        """
        equation = self.label_equation.text()
        equation += '/'
        self.label_equation.setText(equation)

    def multiply(self) -> None:
        """
        Method for button multiply
        """
        equation = self.label_equation.text()
        equation += '*'
        self.label_equation.setText(equation)

    def subtract(self) -> None:
        """
        Method for button subtract
        """
        equation = self.label_equation.text()
        equation += '-'
        self.label_equation.setText(equation)

    def add(self) -> None:
        """
        Method for button add
        """
        equation = self.label_equation.text()
        equation += '+'
        self.label_equation.setText(equation)

    def equal(self) -> None:
        """
        Method solving the written equation
        """
        try:
            self.label_main.setText(f'Formulas')
            equation = self.label_equation.text()
            if equation == '':
                raise ValueError
            answer = str(eval(equation))
            self.label_equation.setText(answer)
        except ZeroDivisionError:
            self.label_main.setText(f'Error: can\'t divide by zero')
        except ValueError:
            self.label_main.setText(f'Error: Equation is empty')

    def back(self) -> None:
        """
        Method for going back in the equation
        """
        equation = self.label_equation.text()
        equation_list = []
        new_equation = ''
        for num in range(len(equation) - 1):
            equation_list.append(equation[num])
        for index in equation_list:
            new_equation += index
        self.label_equation.setText(new_equation)

    def clear(self):
        """
        Method to clear the equation
        """
        self.label_equation.setText('')
        self.label_main.setText(f'Formulas')

