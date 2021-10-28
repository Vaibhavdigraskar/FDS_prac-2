def banking(trans_log):
    trans_log = trans_log.split(",")
    bal = 0
    for i in trans_log:
        i = i.split(" ")
        amount = int(i[-1])
        if i[0] == "D":
            
            bal += amount

        elif i[0] == "W":
            bal -= amount
            if bal < 0:
                print("insufficient balence")
    return bal

banking("D 300,D 300,W 200,W 100")
