"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    txt= result.replace("o","0") 
    txt2=txt.replace("i","1")
    txt3=txt2.replace("a","@")
    return txt3
 