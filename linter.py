import syntax
import re
from os.path import abspath, exists

# Holds organized sections of code
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
    end_block = content[1].rsplit("}", 1)[0]
    blocks.append([content[0]])

    class_definition(blocks[0][0])
    function_definitions(end_block, 1)
    for x in blocks:
        print(x)

# Recursion over methods inside the class
def function_definitions(content, times):
    #print("TRIED" +str(times) + repr(content))
    if not content.isspace():
        content = content.split("{", 1)
        definition = content[0]
        body = content[1].split("}", 1)
        content = body[1]
        body = body[0]

        # Put lines in block
        blocks.append([definition, body])
        # Recursion over all methods
        function_definitions(content, times + 1)

        #print("definition" + definition)
        #print("body" + body)
        #print("content" + content)

# Class definition validation
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




