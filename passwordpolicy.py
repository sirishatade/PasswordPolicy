import string

"""
This password checker verifies that a password matches the following password policy: 
1. Passwords must be 14+ characters in length 
2. Passwords must contain uppercase letters, lowercase letters, numbers and special 
characters, but no more than 3 consecutive characters from a single character class/group """


def password_checker(password):
    if len(password) >= 14 and check_policy(password, string.ascii_uppercase) \
            and check_policy(password, string.ascii_lowercase) \
            and check_policy(password, string.digits) \
            and check_policy(password, string.punctuation):  # checks if passes all requirements
        return True
    return False


def check_policy(password, policy):
    has_policy = False
    counter = 0

    for p in password:
        if p in policy:
            has_policy = True  # policy is true if at least one char matches policy
            counter += 1

            if counter > 3:  # if more than 3 consecutive of the same character group, it fails immediately
                return False
        elif p not in policy:
            counter = 0

    return has_policy

# Test Cases
# print(password_checker("ABCabcABCabc123EFGIHOIERHGOEIRGHOER"))
# print(password_checker("AB123DE345CDkfsjgHIjkI"))
# print(password_checker("AB123DE345CDjgsHIjkI!$!"))
# print(password_checker("AB123DE345CDjgsHIjkI!$!"))
