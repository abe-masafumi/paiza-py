def preinput(input_text):
    out=input_text.split("\n")
    for i in out:
        yield i

def input(reset=False):
    global input_text,inp
    if reset:del inp,input_text,repeat;return
    try:return inp.__next__()
    except:
        if repeat:inp=preinput(input_text)
        return inp.__next__()

def def_input(s,isRepeat=False):
    global input_text,inp,repeat
    input_text=s
    repeat=isRepeat
    inp=preinput(input_text)