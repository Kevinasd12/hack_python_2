"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

# la idea es que itere los valores y le hacemos la modificaciones y luego lo metemos en un diccionario 
def fn_hack_9(s):
   result = s
   del result["bar"]
   result["Foo"] = result.pop("foo")
   for x,y in result.items():
      if y == "fookziman":
         result[x] = "Fooziman"
         
   return result

print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))
  
