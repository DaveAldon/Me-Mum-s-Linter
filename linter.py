import syntax
import re
from os.path import abspath, exists

# Holds organized sections of code
class_structure = []
blocks = []
block_structure = [{}]

def awake():
    injest()

# Injests the objectscript file in question
def injest():
    # Grabs the local file path that has our sample
    f_path = abspath("bad.cls")
    if exists(f_path):
        with open(f_path) as f:
            content = f.read()
    content = remove_comments(content)

    # Blocks consist of Class definition, class block, and function sub blocks
    content = content.split("ClassMethod")
    #end_block = content[1].rsplit("}", 1)[0]
    class_structure.append([content[0]])

    build_class(class_structure[0][0])
    for x in content[1:]:
        build_functions(x)
    for x in blocks:
        parse_function(x)

    print("Found " + str(len(blocks)) + " functions")

def parse_function(content):
    # Function definition parsing
    try:
        definition = content[0].split()
        body = content[1]

        method_name = re.compile(syntax.method_name)
        method_verb = re.compile(syntax.method_verb)
        method_type = re.compile(syntax.method_type)

        if len(definition) > 3: raise Exception()
        if not method_name.match(definition[0]):
            print("Bad Method Name")
            params = definition[0].split("(")[1]
            if len(params) > 1:
                print(params)
                method_parameters = re.compile(syntax.method_parameters)
                if not method_parameters.match(params): print("Bad Parameters")
        if not method_verb.match(definition[1]): print("Bad Method Verb")
        if not method_type.match(definition[2]): print("Bad Method Type")
    except:
        print("Malformed ClassMethod Definition")
        return

    # Good Form Function Definition parsing
    try:
        # Get the parameters from the function definition into a list
        parameters = definition[0].split("(")[1][:-1].split(",")
        return_type = definition[-1]
        function_name = definition[0].split("(")[0]
    except:
        print("Malformed ClassMethod Definition")
        return

    # Function Body Parsing
    try:
        # Check for unused parameters in the function definition
        for x in parameters:
            if x not in body: print("Unused parameter " + x)

        commands = re.split("(write|set|if)", body, 999999)
        command = ""
        for x in commands:
            x = x.replace("\n", "")
            if x.isspace():
                continue
            if x in syntax.verbs:
                command = x
                continue
            verb = re.compile(syntax.verbs[command])
            if not verb.match(command + x): print("Bad " + command)
            else: print("Good " + command)


        #TODO: Comprehensive syntax checking for common commands

    except:
        print("Malformed ClassMethod Body")
        return

# Removes inline comments and commented lines
def remove_comments(content):
    content = content.split("\n")
    new_content = []
    for x in content:
        if x.startswith(syntax.comment): continue
        if syntax.comment in x:
            x = x.split(syntax.comment)[0]
        new_content.append(x)
    return "\n".join(new_content)

# Recursion over methods inside the class
def build_functions(content):
    if not content.isspace():
        content = content.split("{", 1)
        definition = content[0]
        body = content[1]

        # Put lines in block
        blocks.append([definition, body])

# Class definition validation
def build_class(content):
    def first_order_optional(line):
        return line.startswith(syntax.class_comment)
    def first_order_required(line):
        return line.startswith(tuple(syntax.class_declaration))

    # Default states of blocks. Set to true once found
    content = content.split('\n')
    for line in content:
        if first_order_optional(line): continue
        if first_order_required(line):
            line = line.split()
            pattern = re.compile(syntax.class_definition)
            if not pattern.match(line[1]): print("failed to match definition")
            if len(line) > 2:
                if line[2].startswith('Extends'):
                    pattern = re.compile(syntax.class_extension)
                    if not pattern.match(line[3]): print("failed to match extension")
                else: print("Invalid Extend")

            #TODO: Handling of [] params in extensions
            break
        else: print("Bad comment or Class form")




