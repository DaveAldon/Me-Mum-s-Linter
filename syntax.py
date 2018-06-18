# TODO: support for:
# Include %occSAX and IncludeGenerator %occSAX
class_comment = "///"
comment = "//"

class_declaration = ["Class"]

class_definition = "(\w+(\.?\w+)*)[^\.]$"
class_extension = "(\%)?(\w+(\.?\w+)*)[^\.\%]$"
# Extends %CSP.Page [ System = 4 ]

method_name = "\w+\((p\w+(\,\s?p\w+)*)?\)"
method_verb = "as"
method_type = "\%[A-Z](\w+)*"
method_parameters = "p\w+(\,\s?p\w+)*\)"