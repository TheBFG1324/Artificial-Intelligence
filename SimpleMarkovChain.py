import random

def nextGuess(curr):
    num = random.random()
    if curr == 'h':
        if num <= float(7/11):
            return 't'
        else:
            return 'h'
    else:
        if num <= float(7/9):
            return 'h'
        else:
            return 't'

def main():
    actual_user_string = "httthhthtth"
    for x in range(len(actual_user_string)-1):
        cur = actual_user_string[x]
        next_char = actual_user_string[x+1]
        guess = nextGuess(cur)
        
        print(x, cur, next_char, guess, guess==next_char)

main()
