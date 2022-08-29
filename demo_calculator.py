class Calculator(object):
    empty_list = []
    initial = True

    # Exit parenthesis
    ex_pare = False
    # in number
    in_num = False
    # in operator
    in_operator = False

    operators = ('+', '-', '*', '/', '^')
    bodmas = (('^',), ('*', '/'), ('+', '-'))

    def compile(self, user_input_split):
        for character in user_input_split:
            try:
                # To check if its a number
                current = int(character)
                self.in_operator = False
                # To checks if it's a new digit to a previous number
                if self.in_num:
                    # add it to the previous number
                    self.add_new_num(current)
                else:
                    # it's a new number add it to empty_list
                    self.add_new_num(current)
                    self.in_num = True
            except ValueError:
                self.in_num = False
                # To check if it's an operator
                if character in self.operators:
                    if not self.empty_list:
                        raise Exception("You can not start an expression with an operator")
                    if self.in_operator:
                        raise Exception("Invalid argument")
                    else:
                        self.append_element(character)
                        self.in_operator = True
                elif character == '(':
                    self.add_new_perentheses()
                    self.in_operator = True
                elif character == ')':
                    self.ex_pare = True
                    self.in_operator = False
                else:
                    raise Exception("Invalid argument")


            if self.initial:
                self.initial = False

    def get_last_position(self):
        " Returns the last inner most list in the empty_list "

        list_ref = list_prev = self.empty_list
        try:
            # While there's a list 
            while list_ref[-1] == []:
                if isinstance(list_ref[-1], list):
                    list_prev = list_ref
                    list_ref = list_ref[-1]
                else:
                    break

            if self.ex_pare == True:
                self.ex_pare = False
                return list_prev
            else:
                self.ex_pare = False
                return list_ref
        except IndexError:
            if self.ex_pare == True:
                self.ex_pare = False
                return list_prev
            else:
                self.ex_pare = False
                return list_ref

    def append_element(self, el):
        last_position = self.get_last_position()
        last_position.append(el)

    def add_new_num(self, num):
        if not self.empty_list or self.get_last_position() == []:
            self.append_element(num)
        else:
            prev_c = self.get_last_position()[-1]
            # To check if previous char is a number
            is_int = isinstance(prev_c, int)
            if is_int:
                self.add_to_previous_num(num, self.empty_list)
            elif prev_c in self.operators:
                self.append_element(num)
            else:
                is_list = isinstance(self.empty_list[-1], list)
                if is_list:
                    list_ref = self.get_last_position()
                    self.add_to_previous_num(num, list_ref)
                else:
                    raise Exception("something is broken")

    def add_to_previous_num(self, num, empty_list):
        try:
            last_pos = self.get_last_position()
            last_pos[-1] = last_pos[-1] * 10 + num
        except IndexError:
            last_pos.append(num)

    def add_new_perentheses(self):
        last_pos = self.get_last_position()
        last_pos.append([])

    def calculate(self, user_input):
        self.compile(''.join(user_input.split()))

        result = self.recursion_calculator(self.empty_list)
        # We initialize the empty_list "
        self.empty_list = []

        return result

    def recursion_calculator(self, empty_list):
        while len(empty_list) > 1:
            for i in range(len(self.bodmas)):
                for j in range(len(empty_list)): 
                    try:
                        if isinstance(empty_list[j], list):
                            result = self.recursion_calculator(empty_list[j])
                            del empty_list[j]
                            empty_list.insert(j, result)
                        elif empty_list[j] in self.bodmas[i]:
                            result = self.calculator_binary(empty_list, j, empty_list[j])
                            del empty_list[j-1]
                            del empty_list[j-1]
                            del empty_list[j-1]
                            empty_list.insert(j-1, result)
                    except IndexError:
                        break
                else:
                    continue
                break

        return empty_list[0]

    def calculator_binary(self, empty_list, index, operator):
        x = empty_list[index-1]
        y = empty_list[index+1]

        if operator == '+':
            x += y
        elif operator == '-':
            x -= y
        elif operator == '*':
            x *= y
        elif operator == '/':
            x /= y
        elif operator == '^':
            x **= y

        return x

if __name__ == '__main__':
    calc = Calculator()
    print("*******************************************************")
    print("*                   Under Constraction                *")
    print("* Please Note My Calculater Can Only Support Integers *")
    print("*                    Python Calculator                *")
    print("*******************************************************")
    print()
    print("You're limited to use below oparators:\n'+'     Addition\n'-'     Subtraction\n'*'     Multiplication\n'/'     Division\n'^'     Exponentiation")
    print()
    calculator_on = True
    while calculator_on:
        user = input("Do you wish to continue(Y/N); ").lower()
        if user == "y":
            print("Your Answer is: " + str(calc.calculate(input('''Enter your calculation: '''))))
        elif user == "n":
            print("Goodbye...")
            calculator_on = False
        else:
            print("Invalid input. Please try again")