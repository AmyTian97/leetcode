### Search a 2D matrix (row sorted)

Goal: Search an item in a 2D matrix that **every row is sorted** in a non-decreasing order.

A matrix: Array of array (matrix\[row\][col]).

Sorted: Consider binary search, O(log(n)) (If not, probably not optimal).

##### Variance 1:

**Row continuity:** Last item in a row is greater or equal to the first item in the previous row. <u>**O(log(m*n))**</u>

Interpret the 2D array as a 1D array => do binary search on it, **O(log(m*n))**

**Mapping system:** Map the index in 1D array to 2D array

i = 1DimensionalIndex

**row =  i // ncol**  The row an item sits in depends on the number of items per row.

**col = i % ncol**  Mod helps us with wrapping around a fix sized section: 0%4=0, 1%4=1, 2%4=2, 3%4=3, 4%4=0



##### Variance 2:

**Row discontinuity:** Column is sorted in a non-decreasing order. <u>**O(m + n)**</u>

#1 Thing to think about: **How to reduce the search space**. A reduction of search space entails a decision: go to lower value or higher value.

```python
1  4  7  11
8  9  10 20
11 12 17 30
```

Increase: right, down

Decrease: left, up

a) Start from upper left corner: go right: increase value; go down: increase value. **Can not reduce search space!** 

b) Start from lower right corner: go left: decrease value; go up: decrease value. **Can not reduce search space!** 

c) Start from upper right corner: go left: decrease value; go down: increase value. **Reduce search space by eliminating a column or a row, w/o missing information.**

e.g. target = 7

1    4    7    **11**

8    9   10   ~~20~~

11 12  17   ~~30~~

row = 0, col = 3: 11 > target => we want to decrease value; going down will only increase value => go left.

row = 0, col = 2: 7 == target => Find!

d) Start form lower left corner: works too:)





