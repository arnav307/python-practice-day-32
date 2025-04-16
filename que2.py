number=10
try:
    if number >9:
        raise Exception("Number is greater than 9")
except Exception as e:
    print(f"Exception occurred: {e}")