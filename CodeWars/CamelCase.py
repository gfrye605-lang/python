def to_camel_case(text):
    if text == "":
        return
    ind = []
    p = list(text)
    p[0] = p[0].upper()
    print(p[0])
    print(p)
    for indexing_dashes in text:
        ind.append(p.index("-"))
        ind.append(p.index("_"))
    print(ind)

to_camel_case("the_stealth_warrior")