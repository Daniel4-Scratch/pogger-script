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
    "execution_level": None,
    "os": os.name
}
files = {
    "scripts": ["pog"],
    "executables": ["pogexec", "pogx", "pogex"],
}
memory = {}
archive = None

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

class Console:
    def error(text, level, line):
        # using blob2763's easydebugger :)
        ed.display_message("!", "Womp Womp", text + ". Err Lvl: " + str(level), line, "9")
        if level == 2:
            if config["execution_level"] == "file":
                exit()

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
        exit()
    elif line_split[0] == "yap":
        print(handle(line_split[1].strip()))
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
    elif line_split[0] == "rainbow":
        import other.color as color
        color.colorize_and_export_ascii(line_split[1].strip(), line_split[2].strip())
        print(open(line_split[2].strip(), "r").read())
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
        if gzt.isFileGz(sys.argv[1]):
                config["execution_level"] = "archive"
                ## execute "main.pog"
                archive = gzt.extract_custom_gzip_archive_to_memory(sys.argv[1])
                for file in archive:
                    if file == "main.pog":
                        execute_file("main.pog")
                        found = True
                        break
                if not found:
                    Console.error(f'File "main.pog" not found in archive', 2, 0)
                
    elif os.path.isfile(file):
        file = open(file, "r")
        lines = file.readlines()
        for line in lines:
            execute(line, lines.index(line))
        file.close()
    else:
        Console.error(f'File "{file}" not found', 2, 0)

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
        else:
            Console.error(f'File "{sys.argv[1]}" not found', 2, 0)