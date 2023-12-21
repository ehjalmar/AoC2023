import numpy as np

file = open('Day13/input.txt', 'r')
lines = file.read().splitlines()


blocks = [[]]

for line in lines:
    if(line == ""):
        newBlock = []
        blocks.append(newBlock)
        continue
    
    new_line = []
    for char in line:
        new_line.append(char)
    blocks[-1].append(new_line)

def is_valid_index(row_indexes: list, list: list):
    for index in row_indexes:
        if index < 0 or index >= len(list):
            return False
    return True

rows_above = []
columns_to_left = []



for block_index, block in enumerate(blocks):

    # Look for horizontal reflection
    found_match = False
    for row_index, row in enumerate(block):
        if(row_index < len(block)-1):
            if (block[row_index+1] == row):
                # Walk outwards and check match on other rows
                steps = 1
                is_matching = True
                while is_valid_index([row_index-steps, row_index+1+steps], block):
                    if block[row_index-steps] != block[row_index+1+steps]:
                        is_matching = False
                        break
                   
                    steps +=1
                
                if is_matching:
                    print(f'Match in block {block_index+1}:')
                    print(f'row: {row_index+1} and {row_index+2}')
                    rows_above.append(row_index+1)
                    found_match = True
        
        if found_match:
            break

    # Look for vertical reflection
    found_match = False
    np_block = np.array(block)
    for col_index in range(len(block[0])-1):
        col_value1 = np_block[:, col_index] # Get specific column for each row
        col_value2 = np_block[:,col_index+1]
        
        if np.array_equal(col_value1, col_value2):
            # Walk outwards and check match on other columns
            is_matching = True
            left = col_index-1
            right = col_index+2
            while is_valid_index([left, right], np_block[0]):
                # print(f'left: {np_block[:,left]}')
                # print(f'right: {np_block[:,right]}')
                if not np.array_equal(np_block[:,left], np_block[:,right]):
                    is_matching = False
                    break
                left -=1
                right +=1
            
            if is_matching:
                found_match = True
                print(f'Match in block {block_index+1}:')
                print(f'col: {col_index+1} and {col_index+2}')
                columns_to_left.append(col_index+1)
        
        if found_match:
            break

            



    # Look for vertical reflection
    #for col in 

print(sum(rows_above)*100)
print(sum(columns_to_left))
print(sum(rows_above)*100 + sum(columns_to_left))