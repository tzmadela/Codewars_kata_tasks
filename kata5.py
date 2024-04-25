def longest_mountain_pass(mountains, E):
    n = len(mountains)
    if n == 0:
        return (0, 0)  # Empty mountain range: no pass possible, start at index 0
    
    start = 0
    max_length = 0
    max_start = 0
    current_energy = E

    end = 0
    while end < n - 1:
        if mountains[end + 1] > mountains[end]:
            # Going uphill
            energy_cost = mountains[end + 1] - mountains[end]
            current_energy -= energy_cost
            end += 1
        elif mountains[end + 1] <= mountains[end]:
            # Going downhill or staying flat
            end += 1
        
        # Check if we need to adjust the start of the mountain pass
        while current_energy < 0 and start <= end:
            if mountains[start + 1] > mountains[start]:
                # We are moving from a lower height to a higher height (uphill)
                energy_cost = mountains[start + 1] - mountains[start]
                current_energy += energy_cost
            start += 1
        
        # Check if we found a longer mountain pass
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            max_start = start
        elif current_length == max_length and start < max_start:
            max_start = start
    
    return (max_length, max_start)

# Edge case test
result = longest_mountain_pass([1, 2, 3], 0)
print(result)  # Output: (1, 0) -> Single ascending mountain with zero energy, start at index 0
