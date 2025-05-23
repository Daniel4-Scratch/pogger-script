# Execution
This page contains the documentation for the usage of the Pogger Script executeable.

## Script Execution Environments
- `console` live execution in the console
- `file` execution from a file
- `archive` execution from a compressed file

These can change the way file paths are handled and how the script is executed.

# OS Environments
- `nt` (Windows)
- `posix` (Linux, MacOS)
  
Stored in the config runtime dictionary as `os`. 

These don't change the core functionality of a script, slight differences can occur across different OS environments.

# Executables
Executables are compressed pogger script files bundles into a single file using gzip technology.
They must end with the `.pogx`, `pogexec`, or `.pogex` suffix so the executor can identify them and run them correctly.
```
pogscript <executable_file>
```
Learn more about executables in the [Executables](Executables.md) page.