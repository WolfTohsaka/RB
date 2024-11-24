def resistance_to_temperature(resistance):
    # Table of resistance (Ω) and corresponding temperature (°C)
    table = [
        (3004, 20),
        (1868, 30),
        (1198, 40),
        (789, 50),
        (522, 60),
        (368, 70),
        (260, 80),
        (187, 90),
        (137, 100),
        (102, 110),
        (79.2, 120),
        (59, 130),
        (46, 140),
        (36, 150),
        (29, 160),
        (23, 170)
    ]
    
    # Sort the table by resistance values
    table.sort()

    # Check if the resistance is outside the range of the table
    if resistance < table[0][0] or resistance > table[-1][0]:
        raise ValueError("Resistance value is out of range")

    # Find two points between which the resistance lies
    for i in range(len(table) - 1):
        r1, t1 = table[i]
        r2, t2 = table[i + 1]
        
        if r1 <= resistance <= r2:
            # Linear interpolation
            temperature = t1 + (t2 - t1) * ((resistance - r1) / (r2 - r1))
            return temperature

    # If no valid range is found
    raise ValueError("Resistance value is not within the valid range of the table")

