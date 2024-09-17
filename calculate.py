def calculate(num1, num2, operator):
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
    elif operator == '√':
        if num1 < 0:
            return "Error: Negative number cannot have a square root."
        return num1 ** 0.5
    elif operator == '^2':
        return num1 ** 2
    else:
        return "Error: Invalid operator."

memory = 0
history = []

def memory_clear():
    global memory
    memory = 0

def memory_recall():
    return memory

def memory_store(value):
    global memory
    memory = value

def memory_add(value):
    global memory
    memory += value

def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

def view_history():
    if not history:
        print("No history available.")
    else:
        for entry in history:
            print(entry)

def main():
    global memory
    while True:
        try:
            print("\nMemory Operations: MC (Memory Clear), MR (Memory Recall), MS (Memory Store), M+ (Memory Add)")
            print("Operator Options: +, -, *, /, %, √, ^2")
            print("Type 'history' to view calculation history or 'exit' to quit.")
            
            num1 = input("Enter the first number: ").replace(",", ".")
            if num1.lower() == 'history':
                view_history()
                continue
            if num1.lower() == 'exit':
                break

            num1 = float(num1)

            num2_input = input("Enter the second number (or leave empty for square operation): ").replace(",", ".")
            if num2_input.lower() == 'history':
                view_history()
                continue
            if num2_input.lower() == 'exit':
                break

            num2 = None
            operator = ''
            if num2_input.strip() == "":
                operator = '^2'
            else:
                num2 = float(num2_input)
                operator = input("Enter an operator (+, -, *, /, %, √, ^2): ")

            result = calculate(num1, num2 if num2 is not None else 0, operator)

            if isinstance(result, (int, float)):
                decimal_places = input("Enter the number of decimal places (or press Enter for default): ")
                if decimal_places.strip() == "":
                    formatted_result = result
                else:
                    try:
                        decimal_places = int(decimal_places)
                        formatted_result = f"{result:.{decimal_places}f}"
                    except ValueError:
                        print("Invalid number of decimal places. Using default format.")
                        formatted_result = result
            else:
                formatted_result = result

            print("Result:", formatted_result)

            expression = f"{num1} {operator} {num2 if num2 is not None else ''}"
            add_to_history(expression, formatted_result)

            while True:
                memory_command = input("Enter memory command (MC, MR, MS, M+) or press Enter to skip: ").strip().upper()
                if memory_command == 'MC':
                    memory_clear()
                    print("Memory cleared.")
                    break
                elif memory_command == 'MR':
                    print("Memory recall:", memory_recall())
                    break
                elif memory_command == 'MS':
                    memory_store(result)
                    print("Memory stored:", memory)
                    break
                elif memory_command == 'M+':
                    memory_add(result)
                    print("Memory updated:", memory)
                    break
                elif memory_command == '':
                    break
                else:
                    print("Invalid memory command. Please enter MC, MR, MS, M+, or press Enter to skip.")
        
            continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()