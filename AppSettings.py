def format_result(result, decimal_places):
    if decimal_places.strip() == "":
        return result
    try:
        decimal_places = int(decimal_places)
        return f"{result:.{decimal_places}f}"
    except ValueError:
        print("Invalid number of decimal places. Using default format.")
        return result
