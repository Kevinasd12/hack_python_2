"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""
#se puede eliminando por pop
#se puede tambien con remove
def fn_hack_4(s):
    result = s
    if len(result) > 4:
        result = list(s)
        result.pop(0)
        result.pop(-1)
    result = "".join(result)
    return result

"""
def fn_hack_4(s):
    result = s
    if result == "fooziman":
        result = list(s)
        result.remove("f")
        result.remove("n")
    elif result == "barziman":
        result = list(s)
        result.remove("b")
        result.remove("n")
    result = "".join(result)
    return result
"""
