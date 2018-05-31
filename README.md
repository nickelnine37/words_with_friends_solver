# Words With Friends Solver

To run this solver, you must edit the solver.py file. In it, you will find 
a string that looks something like:

```python
board_string = '''
 A   B   C   D   E   F   G   H   I   J   K 
 --------------------------------------------
|   |   |   |   |   |   |   |   |   |   |   | 1 
 --------------------------------------------
|   |   |   |   |   |   |   |   |   |   |   | 2 
 --------------------------------------------
|   |   |   |   |   |   |   |   | s |   |   | 3 
 --------------------------------------------
|   |   |   |   |   | t |   |   | p |   |   | 4 
 --------------------------------------------
|   |   | f | i | n | o |   |   | a |   |   | 5 
 --------------------------------------------
|   |   |   |   |   | w | o | r | d | s |   | 6 
 --------------------------------------------
|   |   |   |   |   | n |   | a | e |   |   | 7 
 --------------------------------------------
|   |   |   |   |   |   |   | g |   |   |   | 8 
 --------------------------------------------
|   |   |   |   |   |   |   | s |   |   |   | 9 
 --------------------------------------------
|   |   |   |   |   |   |   |   |   |   |   | 10 
 --------------------------------------------
|   |   |   |   |   |   |   |   |   |   |   | 11 
 --------------------------------------------
'''
```

Edit this string so that it looks like your current board configuration, 
making sure that everything lines up straight. This will create a Board
class with this as its config. Below this, you will find an instance of 
a Solver class. Feed this your current letters, for example 'djfpeys',
and run the print_solutions method. This will output all possible plays
in order of highest score. 

Enjoy and use responsibly! ;)
