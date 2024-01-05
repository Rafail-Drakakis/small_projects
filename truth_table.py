from itertools import product

def truth_table(expression):
    """
    The `truth_table` function generates a truth table for a given logical expression.
    
    :param expression: The `expression` parameter in the `truth_table` function is a string that
    represents a logical expression. It can contain uppercase letters as variables and logical operators
    such as `and`, `or`, `not`, and parentheses. The function will generate a truth table for the given
    expression, showing all possible
    """
    variables = set()
    for char in expression:
        if char.isalpha() and char.isupper():
            variables.add(char)

    variables = sorted(list(variables))
    header = " | ".join(variables + [expression])
    separator = "-" * len(header)
    print(header)
    print(separator)

    for values in product([0, 1], repeat=len(variables)):
        value_dict = dict(zip(variables, values))
        result = eval(expression, value_dict)
        values_str = " | ".join(str(value) for value in values)
        print(f"{values_str} | {result}")
