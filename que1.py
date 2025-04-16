try:
    print(my_variable)  # Attempt to print an undeclared variable
except NameError as e:
    print(f"NameError occurred: {e}")