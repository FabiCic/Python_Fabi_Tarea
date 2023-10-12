"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    txt= result.replace("o","0") 
    txt2=txt.replace("i","1")
    txt3=txt2.replace("a","@")    
    txt4=txt3.upper()
    lista=[]
    for v in txt4:
        lista.append(v)
    return lista