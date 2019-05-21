def count_vowels(string):
    return sum(1 for x in string if x in 'AEIOUaeiou')
