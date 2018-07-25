def convlastsen(stre,delim="!?.",n=0):
    import string#importing string
    from pyavrophonetic import avro
    import enchant
    d = enchant.DictWithPWL("en_GB","data/bdict4.txt")
    strret=""
    english=0
    bengali=0
    startendsign=""
    try:
        while stre[n]!="." and stre[n]!="?" and stre[n]!="!":
            # Iterating from the back of the sentence
            strret+=stre[n]
            n += 1
        else:
          endendsign=stre[n]  
    except:
        return "Done"
    strlst=strret.split()
    lenghty=len(strlst)
    for element in range(lenghty):
        flag1=0
        flag2=0
        if d.check(strlst[element]):
            flag1+=1
        elementben=avro.parse(strlst[element])
        if d.check(elementben):
            flag2+=1
        if flag1==1 and flag2==0:
            english+=1
        elif flag1==0 and flag2==1:
            bengali+=1
        elif flag1==1 and flag2==1:
            english+=1
            bengali+=1
        else:
            pass
    if english>bengali:
        pass
        strret=" ".join(strlst)
    elif bengali>english:
        for element in range(lenghty):
            flag1=0
            flag2=0
            if d.check(strlst[element]):
                flag1+=1
            elementben=avro.parse(strlst[element])
            if d.check(elementben):
                flag2+=1
            if flag1==1 and flag2==0:
                pass
            elif flag1==0 and flag2==1:
                strlst[element]=elementben
            elif flag1==1 and flag2==1:
                pass
            else:
                pass
            
        strret= " ".join(strlst)
    else:
        pass
    strret=startendsign+strret+avro.parse(endendsign)
    print (strret,)
    convlastsen(stre,n=n+1)

#Usage: convlastsen("Folder zip korte hobe abar . ami korbo na.")
