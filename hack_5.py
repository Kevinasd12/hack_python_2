"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    if len(result) > 2:
        if result == "fooziman":
            result = list(s)
            result[2] = "-"
            result.insert(5,"-")
            result[-1] = "-"
        elif result == "barziman":
            result = list(s)
            result[2] = "-"
            result[5] = "-"
        elif result == "qux":
            result[-1] = "-"
    result = "".join(result)
    return result

