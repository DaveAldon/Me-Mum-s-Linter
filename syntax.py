# TODO: support for:
# Include %occSAX and IncludeGenerator %occSAX
first_order_optional = "///"
global_optional = "//"

first_order = ["Class"]

class_definition = "(\w+(\.?\w+)*)[^\.]$"
class_extension = "(\%)?(\w+(\.?\w+)*)[^\.\%]$"
# Extends %CSP.Page [ System = 4 ]