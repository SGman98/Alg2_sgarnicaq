# Password guesser using brute force

## Summary

Try to guess the password using all possible combinations of characters using a
given pattern.

The functions used in this code are:

`try_guess(guess: str) -> bool:` check whether the guess is equal to the
password or not, return the boolean of the process

`str_add_1(string: str) -> str` add 'one' to the string value taking into
account if the 'digit' is a letter or number

`brute_force(pattern: str) -> int, str` main function iterate over all possible
combinations with a given pattern

## Analysis

Considering n as the number of characters of the password

`try_guess()` since the only operation it has is a comparison, its complexity
is O(1)

`str_add_1()` this function iterates once over the string with the password
length therefore its complexity is O(n)

`brute_force()` to calculate the complexity of this function you have to take
into account the pattern that is given

First for each character it tries each possible combination

- if the character is a 'lowercase letter' then its complexity increases by 26,

- if the character is a 'digit' then it increases by 10

The pattern format is: 'l' = 'lowercase letter', 'd' = 'digit'

If the given pattern is 'lllddd' then it means 3 lowercase letters followed by
3 digits

And its complexity is: `26 * 26 * 26 * 10 * 10 * 10`

Assuming the number of lowercase characters is `l = 26` and the number of
digits is `d = 10` then the complexity is `l ** 3 * d ** 3`

Finally we have that `brute_force()` has a complexity of `l ** 3 * d ** 3` and
it calls for each iteration `str_add_1()` therefore the final complexity is `l
** 3 * d ** 3 * n`

