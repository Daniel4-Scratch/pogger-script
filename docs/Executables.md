# Executables
Executales in pogger script are compressed pogger script files bundles into a single file using gzip technology. 

# Executable Structure
Executables must contain a `main.pog` file, which is the entry point for the script.
The `main.pog` file should contain the main logic of the script, and it can call other pogger script files or executables as needed.
```
MyExecutable.pogx
├── main.pog
├── script1.pog
├── script2.pog
└── script3.pog
```
The recommended suffix for executable files is `.pogx`, `pogexec`, or `.pogex`. 

# Executable Creation
Currently you can create executables using the `gziptool.py` file in the source code directory.
```
Archive: python gziptool.py archive <output_file> <input_files> 
Unarchive: python gziptool.py unarchive <input_file> <output_dir>
```
# Executing the Executable
Just pass the executable file location to the pogger script executor. It will read the suffix and execute the file.
```
pogscript <executable_file>
```