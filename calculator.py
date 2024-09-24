from GlobalVariables import memory, history

class Calculator:
    
    def __init__(self):
        pass

    def input_numbers_and_operator(self):
        try:
            num1 = float(input("Enter the first number: ").replace(",", "."))
            operator = input("Enter an operator (+, -, *, /, %, sqrt, ^): ")
            if operator != 'sqrt' and operator != '^':
                num2 = float(input("Enter the second number: ").replace(",", "."))
            else:
                num2 = None
            return num1, num2, operator
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return None, None, None

    def validate_operator(self, operator):
        valid_operators = ['+', '-', '*', '/', '%', 'sqrt', '^']
        if operator in valid_operators:
            return True
        else:
            print("Error: Invalid operator.")
            return False

    def calculate(self, num1, num2, operator):
        try:
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                if num2 == 0:
                    return "Error: Division by zero is not allowed."
                return num1 / num2
            elif operator == '%':
                if num2 == 0:
                    return "Error: Division by zero is not allowed."
                return num1 % num2
            elif operator == 'sqrt':
                if num1 < 0:
                    return "Error: Negative number cannot have a square root."
                return num1 ** 0.5
            elif operator == '^':
                return num1 ** 2
        except Exception as e:
            return f"Error: {e}"

    def memory_clear(self):
        global memory 
        memory = 0

    def memory_recall(self):
        global memory
        return memory

    def memory_store(self, value):
        global memory 
        memory = value

    def memory_add(self, value):
        self.memory += value

    def add_to_history(self, expression, result):
        global history  
        history.append(f"{expression} = {result}")

    def view_history(self):
        global history
        if not history:
            print("No history available.")
        else:
            for entry in history:
                print(entry)

    def run(self):
        while True:

            print("\nMemory Operations: MC (Memory Clear), MR (Memory Recall), MS (Memory Store), M+ (Memory Add)")
            print("Operator Options: +, -, *, /, %, √, ^")
            print("Type 'history' to view calculation history or 'exit' to quit.")

            num1_input = input("Enter the first number (or type 'history' or 'exit'): ").replace(",", ".")
            if num1_input.lower() == 'history':
                self.view_history()
                continue  
            if num1_input.lower() == 'exit':
                break

            try:
                num1 = float(num1_input)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            num2_input = input("Enter the second number (or leave empty for square operation): ").replace(",", ".")
            if num2_input.lower() == 'history':
                self.view_history()
                continue  
            if num2_input.lower() == 'exit':
                break

            num2 = None
            if num2_input.strip() != "":
                try:
                    num2 = float(num2_input)
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    continue

            operator = input("Enter an operator (+, -, *, /, %, √, ^): ").strip()

            if not self.validate_operator(operator):
                continue

            result = self.calculate(num1, num2, operator)

            expression = f"{num1} {operator} {num2 if num2 is not None else ''}"
            self.add_to_history(expression, result)
            print(f"Result: {result}")

            memory_command = input("Enter memory command (MC, MR, MS, M+) or press Enter to skip: ").strip().upper()
            if memory_command == 'MC':
                self.memory_clear()
                print("Memory cleared.")
            elif memory_command == 'MR':
                print("Memory recall:", self.memory_recall())
            elif memory_command == 'MS':
                self.memory_store(result)
                print("Memory stored:", memory)
            elif memory_command == 'M+':
                self.memory_add(result)
                print("Memory updated:", memory)

            continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
