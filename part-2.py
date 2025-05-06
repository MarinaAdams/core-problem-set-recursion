# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)

# is_palindrome
def is_palindrome(text):
    if text == "":
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

# digit_match
def digit_match(a, b):
    def helper(x, y):
        if x == 0 or y == 0:
            return 0  

        last_match = 1 if x % 10 == y % 10 else 0
        return last_match + helper(x // 10, y // 10)

    if a == 0 and b == 0:
        return 1
    return helper(a, b)

