import time
from typing import Pattern

password = ''

def try_guess(guess) -> bool:
    """ Returns True if guess is correct password else False

    Arguments:
        guess: guess to check password (str)
    """
    global password
    return guess == password

def str_add_1(string: str) -> str:
    """ Add one to the string
    Arguments:
        string: string to add one to (str)
    Returns:
        The string with one added to it

    Example:
        string = '15za1z'
        Returns: '16za2a'
    """

    # if is letter then a -> b -> c -> ... -> y -> z -> a
    # if is digit then 0 -> 1 -> 2 -> ... -> 8 -> 9 -> 0
    # e.g. '00bd34z' -> '00bd35a'
    for index, p in enumerate(reversed(string)):
        if p == '9':
            # replace character at index position with '0'
            string = string[:len(string) - index - 1] + '0' + string[len(string) - index:]
        elif p == 'z':
            # replace character at index position with 'a'
            string = string[:len(string) - index - 1] + 'a' + string[len(string) - index:]
        else:
            # if i is a digit then add 1
            # if i is a letter then add 1 to the next letter
            string = string[:len(string) - index - 1] + chr(ord(p) + 1) + string[len(string) - index:]
            break
    return string

def brute_force(pattern: str):
    """ Returns number of iterations needed to find password and found password

    Arguments:
        pattern: pattern used to find the password (str)
                d - digit\n
                l - lowercase letter

    Example:
        passwords = '15za1c'

        brute_force('ddlldl') -> 2805428, '15za1c'
    """
    # Start position of guess depending on the pattern d -> 0, l -> a
    guess = pattern.replace('d', '0').replace('l', 'a')

    # Complexity is calculated if d multiplies by 10 if l multiplies by 26
    complexity = 1
    for c in pattern:
        complexity *= (10 if c == 'd' else 26 if c == 'l' else 1)

    print(f'Max number of iterations: {complexity}\n')

    for num in range(complexity):
        if try_guess(guess):
            print(f'Password is: \'{guess}\' found in {num + 1} guesses\n')
            break
        else:
            guess = str_add_1(guess)
    else:
        print('Password not found\n')

    return num + 1, guess

def main():
    global password

    password = input('Enter password: ')
    pattern = input('Enter pattern (d for digit, l for lowercase letter): ')

    start_time = time.perf_counter()
    brute_force(pattern)
    end_time = time.perf_counter()

    time_seconds = end_time - start_time
    hours = int((time_seconds // (60 ** 2)) % 60)
    minutes = int((time_seconds // 60) % 60)
    seconds = time_seconds % 60
    print(f'Time taken: {hours:02d}:{minutes:02d}:{seconds:02.4f}')

if __name__ == '__main__':
    main()
