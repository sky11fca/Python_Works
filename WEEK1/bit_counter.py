def bit_counter(nr):
    bin_nr = str(bin(nr))[2:]
    cnt=0
    for bit in bin_nr:
        if bit=='1':
            cnt+=1
    return cnt

sample=24
print(bit_counter(sample))
