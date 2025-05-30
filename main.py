#!/usr/bin/env python3
# Pogger Script Executer
import sys
sys.dont_write_bytecode = True
import os, random
import easydebugger as ed
import gziptool as gzt
from colorama import init as colorama_init
colorama_init()

config = {
    "version": "0.1.0",
    "debug": False,
    "execution_level": None, # console, file, archive == executable
    "os": os.name,
    "gizpDest": "RAM", # where to extract the gzip archive, RAM or folder location
    "permissions":[]
}
files = {
    "scripts": ["pog"],
    "executables": ["pogexec", "pogx", "pogex"],
}
memory = {} # store variables in memory
archive = None # store the archive in memory
fileN = None # file name for debugging

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def handle(text):
    # Check if text is a memory reference
    # () are used to reference memory
    if text.startswith("(") and text.endswith(")"):
        if text[1:-1] not in memory:
            Console.error(f'Memory reference "{text[1:-1]}" not found', 2, 0)
            
        return memory[text[1:-1]]
    elif text == "True" or text == "False":
        return bool(text)
    elif text.isnumeric():
        return int(text)

    return text

class Permissions:
    def check(permission):
        if permission not in config["permissions"]:
            return False
        return True
    def add(permission):
        if permission not in config["permissions"]:
            config["permissions"].append(permission)
        else:
            Console.warn(f'Permission "{permission}" already exists', 0)
    def remove(permission):
        if permission in config["permissions"]:
            config["permissions"].remove(permission)
        else:
            Console.warn(f'Permission "{permission}" not found', 0)
    

class Console:
    '''
    Errror Levels:
    0 = No Error
    1 = Warning
    2 = Fatal Error
    '''
    def error(text, level, line=None):
        # using blob2763's easydebugger :)
        if fileN != None:
            text = text + " in file: " + fileN
        ed.display_message("!", "Womp Womp", text + ". Err Lvl: " + str(level), line, "9")
        if level == 2:
            if config["execution_level"] == "file" or config["execution_level"] == "archive":
                sys.exit(1)


    def warn(text, line):
        ed.display_message("*", "Womp?", text, line, "11")

    def info(text, line):
        ed.display_message("i", "Info", text, line, "15")

    def success(text, line):
        ed.display_message("+", "Yippee", text, line, "10")

def execute(line, line_num):
    global memory
    line_split = line.split(":")
    for i in range(len(line_split)):
        line_split[i] = line_split[i].strip()
    # BASE
    if line_split[0] == "bai":
        sys.exit(0)
    elif line_split[0] == "yap":
        if len(line_split) > 1:
            print(handle(line_split[1].strip()))
        else:
            Console.error(f'Invalid yap command "{line}"', 1, line_num + 1)
    elif line.strip() == "":
        pass
    elif line_split[0] == "mew":
        if config["os"] == "nt":
            os.system("cls")
        else:
            os.system("clear")
    elif line.startswith("//"):
        pass
    elif line_split[0] == "brb":
        input("Press enter to continue...")
    elif line_split[0].startswith("#"):
        pass
    # MATH
    elif line_split[0] == "math":
        line = line.replace("math:", "")
        line_split = line.split(":")
        int1 = handle(line_split[0])
        int2 = handle(line_split[1])
        operator = line_split[2].strip()
        out = line_split[3].strip()

        if type(int1) != int or type(int2) != int:
            Console.error(f'Invalid value type for math operation "{line}"', 2, line_num + 1)
        
        def save(value):
            memory[out] = value

        if operator == "add":
            save(int1 + int2)
        elif operator == "sub":
            save(int1 - int2)
        elif operator == "mul":
            save(int1 * int2)
        elif operator == "div":
            save(int1 / int2)
        elif operator == "mod":
            save(int1 % int2)
        else:
            Console.error(f'Invalid math operator "{operator}"', 2, line_num + 1)
            

    # MEMORY MANAGEMENT
    elif line_split[0] == "str":
        memory[str(line_split[1])] = handle(line_split[2].strip()) or str(line_split[2].strip())
    elif line_split[0] == "int":
        memory[str(line_split[1])] = handle(line_split[2]) or int(line_split[2])
    elif line_split[0] == "bool":
        memory[str(line_split[1])] = handle(line_split[2]) or bool(line_split[2])
    elif line_split[0] == "del":
        del memory[str(line_split[1])]
    elif line_split[0] == "inp":
        memory[str(line_split[1])] = input(line_split[2].strip())
    elif line_split[0] == "cnv":
        line = line.replace("cnv:", "")
        line_split = line.split(":")
        # Layout VALUE:TYPE:OUTPUT
        value = handle(line_split[0])
        _type = line_split[1].strip()
        output = line_split[2].strip()

        if _type == "int":
            memory[output] = int(value)
        elif _type == "str":
            memory[output] = str(value)
        elif _type == "bool":
            memory[output] = bool(value)
        else:
            Console.error(f'Invalid value type "{_type}"', 2, line_num + 1)
    elif line_split[0] == "cpy":
        memory[str(line_split[1])] = memory[str(line_split[2].strip())]
    elif line_split[0] == "rnd":
        # Layout MIN:MAX:OUTPUT
        min = int(line_split[1])
        max = int(line_split[2])
        output = line_split[3].strip()
        memory[output] = random.randint(min, max)
    # PERMISSIONS
    elif line_split[0] == "perm":
        if len(line_split) < 3:
            Console.error(f'Invalid permission command "{line}"', 2, line_num + 1)
            return
        command = line_split[1].strip()
        permission = line_split[2].strip()
        if command == "add":
            if config["execution_level"] == "file":
                if input(f'Enable permission "{permission}"? (y/n) ').strip().lower() == "y":
                    Permissions.add(permission)
            else:
                Permissions.add(permission)
        elif command == "remove":
            Permissions.remove(permission)
        elif command == "check":
            Permissions.check(permission)
        else:
            Console.error(f'Invalid permission command "{command}"', 2, line_num + 1)
    # FILE MANAGEMENT
    elif line_split[0] == "file":
        if Permissions.check("file"):
            command = line_split[1].strip()
            if command == "write":
                if len(line_split) < 4:
                    Console.error(f'Invalid file write command "{line}"', 2, line_num + 1)
                file = line_split[2].strip()
                text = line_split[3].strip()
                if os.path.isfile(file):
                    with open(file, "a") as f:
                        f.write(text + "\n")
                else:
                    Console.error(f'File "{file}" not found', 2, line_num + 1)
            if command == "read":
                if len(line_split) < 3:
                    Console.error(f'Invalid file read command "{line}"', 2, line_num + 1)
                file = line_split[2].strip()
                if os.path.isfile(file):
                    with open(file, "r") as f:
                        memory["$file_"+file] = f.read()
                else:
                    Console.error(f'File "{file}" not found', 2, line_num + 1)
        else:
            Console.error(f'Permission "file" not granted', 1, line_num + 1)
    # CONDITIONALS
    elif line_split[0] == "if":
        # Layout VALUE:OPERATOR:VALUE:TRUE:FALSE
        if len(line_split) < 5:
            Console.error(f'Invalid if statement "{line}"', 2, line_num + 1)

        value1 = handle(line_split[1])
        operator = line_split[2].strip()
        value2 = handle(line_split[3])
        true = line_split[4].strip()
        if len(line_split) == 5:
            false = ""
        else:
            false = line_split[5].strip()

        if operator == "==":
            execute_file(true if value1 == value2 else false)
        elif operator == "!=":
            execute_file(true if value1 != value2 else false)
        elif operator == ">":
            execute_file(true if value1 > value2 else false)
        elif operator == "<":
            execute_file(true if value1 < value2 else false)
        elif operator == ">=":
            execute_file(true if value1 >= value2 else false)
        elif operator == "<=":
            execute_file(true if value1 <= value2 else false)


        else:
            Console.error(f'Invalid operator "{operator}"', 2, line_num + 1)
    # DEBUG
    elif line_split[0] == "mem":
        print(memory)
    elif line_split[0] == "cfg":
        print(config)
    elif line_split[0] == "memType":
        print(type(memory[line_split[1].strip()]))
    elif line_split[0] == "about":
        if config["execution_level"] == "console":
            print("ヾ(^ω^*)")
            print("Pogger Script Version: " + config["version"])
            print("Python Version: " + str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro))
        else:
            Console.error("Cannot use command 'about' in file execution", 2, line_num + 1)
    elif line_split[0] == "dump":
        print(config)
        print(memory)
        print(archive)
        print(fileN)

        

    # MEMORY SAVING
    elif line_split[0] == "memSave":
        file = open(line_split[1].strip(), "w")
        file.write(str(memory))
        file.close()
    elif line_split[0] == "memLoad":
        file = open(line_split[1].strip(), "r")
        memory = eval(file.read())
    elif line_split[0] == "memClear":
        memory = {}
    # FUN / SPECIAL
    elif line_split[0] == "cat":
        print(open(resource_path("./other/color.txt"), "r").read())

    elif line_split[0] == "help":
        print("no")

    else:
        Console.error(f'Invalid command "{line_split[0]}"', 2, line_num + 1)


def execute_file(file):
    global archive
    if archive != None and config["execution_level"] == "archive":
        ## find that file in the archive
        if file in archive:
            lines = archive[file].decode("utf-8").splitlines()
            for line in lines:
                execute(line, lines.index(line))
        else:
            Console.error(f'File "{file}" not found in archive', 2, 0)
    elif os.path.isfile(file) and file.endswith(tuple(files["executables"])):
        if gzt.isFileGz(file):
                fileN = file
                config["execution_level"] = "archive"
                ## execute "main.pog"
                archive = gzt.extract_custom_gzip_archive_to_memory(file)
                found = False
                for cfile in archive:
                    if cfile == "main.pog":
                        execute_file("main.pog")
                        found = True
                        break
                if not found:
                    Console.error(f'File "main.pog" not found in the executable "{file}"', 2)
        else:
            Console.error(f'File "{file}" is not a valid archive/executable', 2)
                
    elif os.path.isfile(file):
        fileN = file
        file = open(file, "r")
        lines = file.readlines()
        for line in lines:
            execute(line, lines.index(line))
        file.close()
    else:
        Console.error(f'File "{file}" not found', 2)

def main():
    config["execution_level"] = "console"
    print("Pogger Script Executer")
    print("Version: " + config["version"])
    while True:
        line = input(">>> ")
        execute(line, 0)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        if os.path.isfile(sys.argv[1]):
            config["execution_level"] = "file"
            execute_file(sys.argv[1]) 
        elif sys.argv[1] == "--archive":
            gzt.create_custom_gzip_archive(sys.argv[2], *sys.argv[3:])
        elif sys.argv[1] == "--unarchive":
            gzt.extract_custom_gzip_archive(sys.argv[2], sys.argv[3])
        else:
            Console.error(f'File "{sys.argv[1]}" not found', 2, 0)