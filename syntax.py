# TODO: support for:
# Include %occSAX and IncludeGenerator %occSAX
first_order_optional = "///"
global_optional = "//"

first_order = ["Class"]

class_definition = "(\w+(\.?\w+)*)[^\.]$"
class_extension = "(\%)?(\w+(\.?\w+)*)[^\.\%]$"
# Extends %CSP.Page [ System = 4 ]

# Method_name doesn't handle numbers in function name
method_name = "\w+\((p\w+(\,\s?p\w+)*)?\)"
method_verb = "as"
method_type = "\%[A-Z](\w+)*"
method_parameters = "p\w+(\,\s?p\w+)*\)"