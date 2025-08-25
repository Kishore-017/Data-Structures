def is_palindrome_custom(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    length = len(cleaned)
    queue = []
    mid = length // 2
    for i in range(mid):
        queue.append(cleaned[i])    
    start_compare = mid if length % 2 == 0 else mid + 1
    for i in range(start_compare, length):
        if not queue:
            return False
        if cleaned[i] == queue[-1]:
            queue.pop()  
        else:
            return False
    return True
if __name__ == "__main__":
    phrase = input("Enter word/phrase: ")
    if is_palindrome_custom(phrase):
        print(f"'{phrase}' is a palindrome.")
    else:
        print(f"'{phrase}' is not a palindrome.")
