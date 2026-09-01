def tribonacci_sequence(start_sequence, length):
    seq=[]
    if length <= 3:
        for i in range(length):
            seq.append(start_sequence[i])
        return seq
    else:
        for i in range(3):
            seq.append(start_sequence[i])
        x=3
        while(x<length):
            temp=0
            for i in range(-1,-4,-1):
                temp+=seq[i]
            seq.append(temp)
            x+=1
    return seq