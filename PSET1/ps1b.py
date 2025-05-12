def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back using greedy strategy (returns both count and list of eggs used).
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter (unused in greedy)
    
    Returns: tuple (smallest number of eggs, list of eggs used)
    """
    egg_weights = sorted(egg_weights, reverse=True)  
    total_weight = 0
    num_eggs = 0
    eggs_used = []  

    for egg in egg_weights:
        while total_weight + egg <= target_weight:
            total_weight += egg
            num_eggs += 1
            eggs_used.append(egg)

        
        if total_weight == target_weight:
            break

    return num_eggs, eggs_used


if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected output: 9 eggs (3*25 + 2*10 + 4*1)")
    num_eggs, eggs_used = dp_make_weight(egg_weights, n)
    print("Actual output:")
    print(f"Number of eggs used: {num_eggs}")
    print(f"Eggs used: {eggs_used}")
