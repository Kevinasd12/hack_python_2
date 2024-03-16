"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = s
    contador = 1
    strr = 0
    two = 1
    while contador < len(result) + 1:
        par_impar = contador % 2
        if len(result) < 2:
            if 0 in result:
                break
            result.append(0)
            break 
        if par_impar == 1:
            result[strr] = f"{contador}"
            strr += 2
        elif par_impar == 0:  
            result[two] = two + 1
            two += 2
        contador +=1
    return result

print(fn_hack_7(["b","c","d","e","a","b","c","d","e","a","b","c","d","e"]))


