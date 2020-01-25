# No. 1x
def string_case_count(string):
    """
    This function accepts a string and returns the
    number of capital letters and the number of small letters it contains
    """
    uppers = ''
    lowers = ''
    for char in string:
        if char == ' ' or not char.isalpha():
            continue
        if char == char.upper():
            uppers += string[string.find(char)]
        else:
            lowers += char

    print(
        '\nNo. of Upper Case Characters: ' + str(len(uppers)) +
        '\nNo. of Lower Case Characters: ' + str(len(lowers))
    )


def question_1():
    """
    This function validates and sanitizes the arg for string_case_count(arg)
    """
    print('\nString Case Calculator')
    string = input('Enter a word or statement: ')
    string_case_count(string)


# No. 2
def find_max(numbers):
    """
    This function accepts a series of numbers and returns the highest value
    """
    print('\nThe maximum number is: ' + str(max(numbers)))


def question_2():
    """
    This function validates and sanitizes the arg for find_max(arg)
    """
    print('\nFind Max of 3')
    print('Enter each of the numbers based on the hint given')
    print('\nEnter 3 operands one at a time')
    length = 3
    numbers = []
    index = 1
    for i in range(length):
        try:
            n = float(input(str(index) + ': '))
        except ValueError:
            err_countdown.append(1)
            print('\nERROR Expected an integer input' +
                '\nNumber of retries ' + str(len(err_countdown)))
            if len(err_countdown) == 3:
                return print('\nRetries exhausted')
            return question_2()
        numbers.append(n)
        index += 1
    find_max(numbers)


# No. 3
def check_prime(n):
    """
    This function accepts a number and checks if it is a prime number
    """
    if n == 0:
        return print('0 is not a suitable integer for this concept')
    for i in range(2, n):
        if n < 3 or n % i == 0:
            return print('\n' + str(n) + ' is NOT a prime number')
    else:
        return print('\n' + str(n) + ' is a prime number')


def question_3():
    """
    This function validates and sanitizes the arg for check_prime(arg)
    """
    print('\nCheck Prime')
    n = input('Enter the number to check if prime: ')
    if n.isnumeric():
        check_prime(int(n))
    else:
        err_countdown.append(1)
        print('\nERROR Expected an integer input' +
              '\nNumber of retries ' + str(len(err_countdown)))
        if len(err_countdown) == 3:
            return print('\nRetries exhausted')
        question_3()


def start_app():
    input_quantity = input('Enter the question number from numbers 1-3: ')
    if input_quantity == '1':
        question_1()
    elif input_quantity == '2':
        question_2()
    elif input_quantity == '3':
        question_3()
    else:
        err_countdown.append(1)
        print('\nERROR There are only 3 questions' +
              '\nNumber of retries' + str(len(err_countdown)))
        if len(err_countdown) == 3:
            return print('\nRetries exhausted')
        start_app()


err_countdown = []

start_app()
