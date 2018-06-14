import syntax
import re
from os.path import abspath, exists

blocks = []


def awake():
    injest()

# Injests the objectscript file in question
def injest():
    # Grabs the local file path that has our sample
    f_path = abspath("bad.cls")
    if exists(f_path):
        with open(f_path) as f:
            content = f.read()

    # Blocks consist of Class definition, class block, and function sub blocks
    content = content.split("{", 1)
    blocks.append(content[0])
    end_block = content[1].rsplit("}", 1)
    blocks.append(end_block[0])

    class_definition(blocks[0])
    function_definitions(blocks[1])

def function_definitions(content):
    print(content)

def class_definition(content):
    def first_order_optional(line):
        return line.startswith(syntax.first_order_optional)
    def first_order_required(line):
        return line.startswith(tuple(syntax.first_order))

    # Default states of blocks. Set to true once found
    content = content.split('\n')
    for line in content:
        if first_order_optional(line): continue
        if first_order_required(line):
            line = line.split()
            pattern = re.compile(syntax.class_definition)
            if not pattern.match(line[1]): print("failed to match definition")
            if len(line) > 1:
                if line[2].startswith('Extends'):
                    pattern = re.compile(syntax.class_extension)
                    if not pattern.match(line[3]): print("failed to match extension")
                else: print("Invalid Extend")

            #TODO: Handling of [] params in extensions
            break
        else: print("Bad comment or Class form")




