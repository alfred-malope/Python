import re

class Calculator():
    def __init__(self, tokens):
        try:
            self._tokens = tokens
            self._current = tokens[0]
        except Exception as e:
            return e
        
    def exp(self):
        try:
            result = self.term()
            while self._current in ('+', '-'):
                if self._current == '+':
                    self.next()
                    result += self.term()
                if self._current == '-':
                    self.next()
                    result -= self.term()
            return result
        except Exception as e:
            return e

    def factor(self):
        result = None
        if self._current[0].isdigit() or self._current[-1].isdigit():
            result = float(self._current)
            self.next()
        elif self._current == '(':
            self.next()
            result = self.exp()
            self.next()
        return result

    def next(self): 
        self._tokens = self._tokens[1:]
        self._current = self._tokens[0] if len(self._tokens) > 0 else None

    def term(self):
        result = self.factor()
        while self._current in ('*', '/'):
            if self._current == '*':
                self.next()
                result *= self.term()
            if self._current == '/':
                self.next()
                result /= self.term()
        return result

if __name__ == '__main__':
    print("*******************************************************")
    print("*                    Python Calculator                *")
    print("*******************************************************")
    print()
    print("You're limited to use the below oparators:\n'+'     Addition\n'-'     Subtraction\n'*'     Multiplication\n'/'     Division")
    print()
    calculator_on = True
    user = input("Do you wish to continue(Y/N); ").lower()
    while calculator_on:
        if user == "y":
            try:
                tokens = re.findall(r'[\d.]+|[+-/*()]', input("Enter your calculation: ").replace(' ', ''))
                print(Calculator(tokens).exp())
                user = input("Do you like try again(Y/N):").lower()
            except Exception as e:
                print("Invalid input. Please try again") 
                user = input("Do you like try again(Y/N):").lower()
        elif user == "n":
            print("Goodbye...")
            calculator_on = False
        else:
            print("Invalid input. Please try again")
            user = input("Do you wish to continue(Y/N); ").lower()
