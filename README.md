Files: 
    `sorer` -- main method to parse and store data from file
    `sor.py` -- class definition for SoR, which is a data structure containing a 2D list of data, a schema detailing what datatype each column is, and a number of columns. It also has various methods to be performed on the SoR class.
    `util.py` -- document containing various util methods to be used that aren't specific to the SoR class


Part 1: Determine Schema
First, we read the first 500 lines of the file (or the entire file, if the file is less than 500 lines). From here, we determine the schema. This is done in the method `generateSchema()` as part of the `SoR` class

We parse each line of the file into a list of the elements in it, discarding any line with invalid 
elements. We determine an invalid element to be any element inside of a `"<>"` that has spaces in it
without starting and ending with a double quote. 

We create a list composed of each parsed line of the file. We now have a 2D list where each row was each
line from the file, and each column is a column of one particular datatype. 

Then, we determine the datatype contained in each colum. We do this in the function `getType`. To determine
the datatype of the column, we look at all of the elements in the column one by one. First, we check to
see if these elements are booleans. If we find an element with an integer value, this column must not be 
booleans. If we find an element with a float value, this column must not be booleans or integers. If we
find an element that isn't a boolean, integer, or float, it must be a column of strings. 

Once we have identified a type for each column, we save this in the `SoR` field `schema`.

Part 2: Store Data
Then we store the data from the file we read in. We do this in the method `generateData()` in the `SoR` class.
We start reading from either the beginning of the file or the offset provided to us with the flag `-start`. 
If the numerical value for `-start` is not equal to zero, we discard the first line of the file, assuming that
the line wasn't complete. We stop reading when we get to the end of the file or when we have read the number
of bytes provided to us with the flag `-len`. In the case that we have read all the bytes we are allowed to read
and we still have not reached the end of the file, we discard the last line we read, assuming it is incomplete. 

We parse each row as we read it into a list of its elements, and we then store that list of elements in the field 
`data` in our `SoR` class. Now, our `data` field is a 2D list representation of the section of the file that we read in. 

If, when we parse the row, we determine that the row is missing elements (ie. the length of the parsed row is less
than the length of the file schema (stored by the field `numColumns` in `SoR`)), we add empty strings at the end 
of the list to make it the same length as `numColumns` and represent missing elements.


Part 3: Print Data
Option 1: `print_col_type`

We take the index of the column from the arguments, and call the method `getColumnType()` from the `SoR` class, which
returns the type (one of: INT, BOOL, FLOAT, STRING) of the column as a string. This is then printed. 

Option 2: `print_col_idx`

We get the element at the specified row and column location with `getElement()` from the `SoR` class, make sure it matches the
type we have determined the column to be (checked with `getColumnType()` and `compareType()` from the `util.py` file), and 
then we print the element. 


Option 3: `is_missing_idx`
We get the element at the specified row and column location as we do for `print_col_idx`. Then, we check if this element is
an empty string. If so, we print 1 for True, since the element is missing. Otherwise, we print 0 for false since the element
is not missing. 
