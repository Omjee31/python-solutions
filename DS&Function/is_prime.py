def is_prime(num):
    '''Step 1: Handle edge cases
     Numbers less than 2 (0, 1, negatives) are NOT prime by definition'''
    if num < 2:
        return False

    '''Step 2: Try to find any divisor of num
        We only check till sqrt(num) because:
        If num has a factor larger than sqrt(num),
        the corresponding smaller factor would already be found'''
    for i in range(2, int(num ** 0.5) + 1):

        '''Step 3: Check divisibility
         If num is divisible by i, it means num has a factor
         A number with a factor other than 1 and itself is NOT prime'''
        if num % i == 0:
            return False  # Exit immediately if any factor is found

    '''Step 4: Final conclusion
    # If the loop completes without finding any divisor,
    # it means num has NO factors other than 1 and itself
    # Therefore, num IS a prime number'''
    return True


# Test the function
if __name__ == "__main__":
    num = int(input("Enter Number You Want To Cheak Number IS Prime OR Not"))
    print(f"{num} IS Prime Number ? : Answer :- ",is_prime(num))   #Output

