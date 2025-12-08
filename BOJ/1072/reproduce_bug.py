
def solve_user(X, Y):
    left = 0
    right = X - Y 
    original_rate = int((Y/X * 100)) # Mimicking user logic but explicitly int-ing or relying on comparison
    # User had: original_rate= (Y/X * 100) % 100
    # Note: user did not cast to int before % 100, so it's a float.
    # But later they do if (rate >= original_rate+1).
    
    # Original user code:
    original_rate= (Y/X * 100) % 100 
    result = -1

    while left <= right:
        mid = (left + right) // 2
        rate = ((Y + mid) / (X + mid)) * 100 % 100
        if (rate >= original_rate+1):
            result = mid 
            right = mid - 1
        else: 
            left = mid + 1
    return result

def solve_correct(X, Y):
    z = (Y * 100) // X
    if z >= 99:
        return -1
    
    # We want minimal K such that (Y+K)*100 // (X+K) >= z+1
    # Binary search
    left = 0
    right = X # Sufficiently large
    ans = -1
    
    while left <= right:
        mid = (left + right) // 2
        new_z = ((Y + mid) * 100) // (X + mid)
        if new_z > z:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

if __name__ == "__main__":
    X = 100
    Y = 98
    print(f"Test case: X={X}, Y={Y}")
    user_ans = solve_user(X, Y)
    correct_ans = solve_correct(X, Y)
    print(f"User answer: {user_ans}")
    print(f"Correct answer: {correct_ans}")
    
    if user_ans != correct_ans:
        print("FAIL: User logic is incorrect.")
    else:
        print("PASS (for this case)")
