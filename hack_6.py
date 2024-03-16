"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    ls = []
    conteo = 1
    if len(result) == 0:
        ls = ["0"]
    for recorre in result:
        ls.append(recorre)
        par_impar = len(ls) % 2
        if par_impar == 1:
            ls[-1] = str(conteo)
            conteo += 2
        elif par_impar == 0:
            ls[-1] = "-"
    result = ls
    return result
