def getRow(rowIndex):
    if rowIndex < 0:
        return []
    
    # Initialize the result with the first row
    result = [1]
    
    for i in range(1, rowIndex + 1):
        # Generate the current row based on the previous row
        current_row = [1]
        for j in range(1, len(result)):
            current_row.append(result[j - 1] + result[j])
        current_row.append(1)
        
        # Update the result to the current row
        result = current_row
    
    return result
