# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:40:08 2020

@author: AmyTian
"""

# Search for an item that equals to the target, return bool
# Property of the matrix:
# Every row is sorted in a non-decreasing order

# Variant 1:
# The first integer of each row is greated or equal to 
# the last integer of the previous row
def search_matrix_1(matrix, target): # matrix: array of array (matrix[row][col])
    nrow = len(matrix)
    ncol = len(matrix[0])
    l = 0
    r = nrow * ncol - 1
    while l <= r:
        mid = (l + r) // 2
        row = mid // ncol
        col = mid % ncol
        val = matrix[row][col]
        if val == target:
            return True
        elif val > target:
            r = mid - 1
        else:
            l = mid + 1
    return False


# Variant 2:
# Every column is sorted in a non-decreasing order
def search_matrix_2(matrix, target):
    # Start from upper right corner (or lower left corner)
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) | col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False



if __name__ == "__main__":
    matrix = [[1,2,3,5],[6,7,9,10]]
    print("Searching for 6:", search_matrix_1(matrix, 6))
    print("Searching for 11:", search_matrix_1(matrix, 11))
    
    matrix_2 = [[1,2,3,5],[4,7,8,10],[5,9,11,13]]
    print("Searching for 6:", search_matrix_2(matrix_2, 6))
    print("Searching for 11:", search_matrix_2(matrix_2, 11))