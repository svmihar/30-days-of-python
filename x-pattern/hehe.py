def border(w=10,h=10): 
    output = []
    for top in range(h): 
        line = ""
        for left in range(w): 
            if top == 0 or left == 0 or top == h-1 or left == w-1 or top == left or top == w-1-left:
                line += "X"
            else: 
                line += " "
        output.append(line)
    return output




for x in border(10,10): 
    print(x)