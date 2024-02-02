#!/usr/bin/python3
def safe_print_division(a, b):
    answer = 0
    try:
        answer = a / b
    except (ValueError, ZeroDivisionError):
        answer = None
    finally:
        print("Inside result: {}".format(answer))
    return answer
