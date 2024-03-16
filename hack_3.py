"""
generic script
text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    a = "@"
    e = "3"
    i = "¡"
    o = "0"
    u = "v"
    q = "Q"
    result = s.replace("a",a).replace("e",e).replace("i",i).replace("o",o).replace("u",u).replace("q",q)
    if len(result) >= 3:
        lista = list(result)
        lista[-1] = lista[-1].upper()
        lista[0] = lista[0].upper()
        result = "".join(lista)
    return result

