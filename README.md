# Pogger Script
Brain rot ahh language

## Basics
### Printing
Use `yap` to print a string. Keep yapping!
```
yap:Hello, World!
```
### Clear
Use `mew` to clear the console. Keep mewing!
```
mew
```
### Exit
Use `bai` to exit the program.
```
bai
```

## Memory
Memory in pogger script is basically variables. You can store values in memory and retrieve them later.

### Storing values
There are 3 different memory types in pogger script: integers, strings and booleans. They all have their own functions. 


Types:
- `int` integer value
- `str` string value
- `bool` boolean value
```
TYPE:NAME:VALUE
```
- `TYPE` is the type of the value you want to store
- `NAME` is the name of the value you want to store. This is how you will retrieve the value later.
- `VALUE` is the value you want to store

For example, to store an integer value in memory:
```
int:myInt:10
```

### Retrieving values
To retrieve a value from memory, use `(NAME)` where `NAME` is the name of the value you want to retrieve. 
```
yap:(NAME)
```

### Deleting values
To delete a value from memory, use `del` followed by the name of the value you want to delete.
```
del:NAME
```

### Copying values
To copy a value from one memory variable to another, use `cpy` followed by the name of the memory variable you want to copy from and the name of the memory variable you want to copy to.
```
cpy:FROM:TO
```

### User input
Use `inp` to get user input and store it in a memory variable
```
inp:NAME:PROMPT
```

### Random
Use `rnd` to generate a random number between two values
```
rnd:MIN:MAX:OUTPUT
```

### Convert
Use `cnv` to convert a value to another
```
cnv:VALUE:TYPE:OUTPUT
```

### Debugging
Use `mem` to print the value of a memory variable
```
mem
```
Use `memType` to find out the type which a memory variable is
```
memType:NAME
```

## Math
Pogger script supports basic math operations. You can add, subtract, multiply and divide integers.

- `add` adds two integers
- `sub` subtracts two integers
- `mul` multiplies two integers
- `div` divides two integers
- `mod` returns the remainder of a division

``` 
math:VALUE1:VALUE2:OPERATION:OUTPUT
```
- `VALUE1` is the first integer value
- `VALUE2` is the second integer value
- `OPERATION` is the math operation you want to perform
- `OUTPUT` is the name of the memory variable you want to store the result in
  
## Conditionals
Pogger script supports basic conditionals. You can compare two values and execute different code based on the result.
Operators:
- `==` equal to
```
IF:VALUE1:OPERATOR:VALUE2:TRUE.POG:FALSE.POG
```
- `VALUE1` is the first value
- `OPERATOR` is the comparison operator
- `VALUE2` is the second value
- `TRUE.POG` is the code to execute if the condition is true
- `FALSE.POG` is the code to execute if the condition is false