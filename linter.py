import syntax
import re
from os.path import abspath, exists


def awake():
    injest()

# Injests the objectscript file in question
def injest():
    # Grabs the local file path that has our sample
    f_path = abspath("bad.cls")
    if exists(f_path):
        with open(f_path) as f:
            content = f.readlines()
    # Dump lines into a list
    content = [x.strip() for x in content]
    first_order(content)

def first_order(content):
    def first_order_optional(line):
        return line.startswith(syntax.first_order_optional)
    def first_order_required(line):
        return line.startswith(tuple(syntax.first_order))

    # Default states of blocks. Set to true once found
    open_block = False
    close_block = False

    for line in content:
        if first_order_optional(line): continue
        if first_order_required(line):
            line = line.split()
            pattern = re.compile(syntax.class_definition)
            if pattern.match(line[1]): print("match definition")
            if len(line) > 1:
                if line[2].startswith('Extends'):
                    pattern = re.compile(syntax.class_extension)
                    if pattern.match(line[3]): print("match extension")
                else: print("Invalid Extend")
            #TODO: Handling of [] params in extensions
            try:
                block_begin = line.index("{")
                open_block = True
                if (block_begin) < (len(line)-1):
                    #TODO: This assumes there's a lot of logic in one line. We're not ready to tackle that
                    print("Too complex for now!")
            except:
                break
            break

        else: print("fail")




