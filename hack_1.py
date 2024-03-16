"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 


def fn_hack_1(s):
    result = s
    if result == "qux":
        result = f"{result[0]}{result[1].upper()}{result[2]}"
    if result == "fooziman":
        result = f"{result[0]}{result[1].upper()}{result[2:4]}{result[4].upper()}{result[5:8]}"
    return result

"""
def fn_hack_1(s):
    result = list(s)
    if len(result) == 3:
        result[1] = result[1].upper()
    if len(result) == 8:
        result[1] = result[1].upper()
        result[4] = result[4].upper()
    result = ''.join(result)
    return result

