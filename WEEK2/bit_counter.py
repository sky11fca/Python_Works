
def bit_counter(nr):
    cnt=0
    while nr:
        if nr%2==1:
            cnt+=1
        nr = nr//2
    return cnt

sample=24
print(bit_counter(sample))
