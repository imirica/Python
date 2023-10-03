def generate(num_rows):
    if numRows == 0:
        return []
    
    # Initialize the result with the first row
    result = [[1]]
    
    for i in range(1, num_rows):
        # Generate the current row based on the previous row
        prev_row = result[-1]
        current_row = [1]
        for j in range(1, len(prev_row)):
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)
        
        # Append the current row to the result
        result.append(current_row)
    
    return result
