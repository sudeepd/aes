'''
Generix Utility function that rotates an array a given number of steps to the 
right or left
'''
def rotLeft(row, places):
    right = row[places- len(row):]
    left = row[:places]
    result = right + left
    return result

'''
    Rotates elements of an array give spaces towards the higher orders (think as circular left shift)
'''
def rotRight(row,places):
    if (places == 0 ): return row
    left = row[-places:]
    right = row[:len(row) - places]
    result = left + right
    return result
