from os.path import abspath, exists

# Injests the objectscript file in question
def injest():
    # Grabs the local file path that has our sample
    f_path = abspath("sample.cls")
    if exists(f_path):
        with open(f_path) as f:
            content = f.readlines()
    # Dump lines into a list
    content = [x.strip() for x in content]

    print(content)

injest()

