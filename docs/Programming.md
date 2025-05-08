
# **Programming in Pogger Script**
Welcome to the documentation for Pogger Script! This guide provides everything you need to know to get started with Pogger Script.

## **Basics**

### **Printing**
Use `yap` to print a string to the console.  
**Syntax**:  
```
yap:MESSAGE
```
**Example**:  
```
yap:Hello, World!
```

### **Clear Console**
Use `mew` to clear the console.  
**Syntax**:  
```
mew
```

### **Exit Program**
Use `bai` to exit the program.  
**Syntax**:  
```
bai
```

---

## **Memory**

Memory in Pogger Script allows you to store, retrieve, and manage variables. Variables can be integers, strings, or booleans.

### **Storing Values**
Use the following syntax to store a value in memory:  
```
TYPE:NAME:VALUE
```
- **TYPE**: The data type (`int`, `str`, `bool`).  
- **NAME**: The variable name.  
- **VALUE**: The value to store.  

**Example**:  
```
int:myInt:10
```

### **Retrieving Values**
To retrieve a stored value, reference its name using parentheses.  
**Syntax**:  
```
yap:(NAME)
```

**Example**:  
```
yap:(myInt)
```

### **Deleting Values**
Use `del` to delete a variable from memory.  
**Syntax**:  
```
del:NAME
```

**Example**:  
```
del:myInt
```

### **Copying Values**
Copy a value from one variable to another using `cpy`.  
**Syntax**:  
```
cpy:FROM:TO
```

**Shortcut**: Use the value directly in a memory operation:  
```
TYPE:NAME:(FROM)
```

**Example**:  
```
cpy:myInt:newInt
```

### **User Input**
Use `inp` to capture user input and store it in memory as a string.  
**Syntax**:  
```
inp:NAME:PROMPT
```

**Example**:  
```
inp:username:Enter your name:
```

### **Random Number Generation**
Generate a random number within a range using `rnd`.  
**Syntax**:  
```
rnd:MIN:MAX:OUTPUT
```

**Example**:  
```
rnd:1:100:randomNum
```

### **Type Conversion**
Convert a value to another type using `cnv`.  
**Syntax**:  
```
cnv:VALUE:TYPE:OUTPUT
```

**Example**:  
```
cnv:123:str:stringValue
```

### **Debugging Memory**
- Print current memory: `mem`  
- Get a variable's type: `memType:NAME`

**Example**:  
```
mem
memType:myInt
```

### **Clearing Memory**
Clear all memory using `memClear`.  
**Syntax**:  
```
memClear
```

### **Saving and Loading Memory**
- Save memory to a file: `memSave:FILENAME`  
- Load memory from a file: `memLoad:FILENAME`

**Examples**:  
```
memSave:backup.mem
memLoad:backup.mem
```

---

## **Math**

Perform basic arithmetic operations using `math`.  
**Syntax**:  
```
math:VALUE1:VALUE2:OPERATION:OUTPUT
```
- **VALUE1** and **VALUE2**: Operands.  
- **OPERATION**: The operation (`add`, `sub`, `mul`, `div`, `mod`).  
- **OUTPUT**: The variable to store the result.

**Example**:  
```
math:10:5:add:sum
```

---

## **Conditionals**

Execute different code based on conditions using `IF`.  
**Syntax**:  
```
IF:VALUE1:OPERATOR:VALUE2:TRUE.POG:FALSE.POG
```
- **VALUE1**: First value.  
- **OPERATOR**: Comparison operator (`==`, `!=`, `<`, `>`, `>=`, `<=`).  
- **VALUE2**: Second value.  
- **TRUE.POG**: Code to execute if true.  
- **FALSE.POG**: Code to execute if false.  

**Example**:  
```
IF:(score):>=:50:pass.pog:fail.pog
```
---
test