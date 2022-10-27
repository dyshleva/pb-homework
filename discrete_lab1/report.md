# Report for discrete maths lab work
*For more detailed documentation, check the code's documentation*

**The function reads from `base.txt` and writes to**
- `transitive_closure.txt`
- `symmetric_closure.txt`
- `reflexive_closure.txt`
- `equality_class_division.txt`


*Should there occur any problem with the code, please contact Petro Mozil <mozil.petryk@gmail.com>*

For the lab work, we used python, which is counterproductive.

### The functions are as such:
- symmetric_closure - makes a symmetric closure of matrix representation of a relation
- symmetric_check - check if the matrix representation is symmetric
- reflexive_closure - makes a reflexive closure of matrix representation of a relation
- reflexive_check - check if the matrix representation if reflexive
- transitive_closure - makes a transitive closure of matrix representation of a relation
- transitive_check - check if a relation is transitive
- equivalence_class - creates a davision of a set by the equivalence relation (if makes it equivalent)

### The next functions are rather self-explanatory
- read_file
- write_matrix
- write_set

### Here's the breakdown of all the complexities:
- symmetric_closure - O(n²)
- symmetric_check - O(n²)
- reflexive_closure - O(n)
- reflexive_check - O(n)
- transitive_closure - O(n³)
- transitive_check - O(n³)
- equivalence_class - O(n²)
- read_file - O(n²)
- write_matrix - O(n²)
- write_set - O(n²)

## Notes
- **There is a check of matrixe's squareness in all the closures**
```python
assert all(len(matrix) == len(x) for x in matrix) and matrix is not None
```
- **Also, the transitive check is O(n³) because the function makes a transitive closure of a matrix**
