def triangle_counter(list):
    cnt=0

    for i in range(len(list)):
        for j in range(i+1,len(list)):
            for k in range(j+1,len(list)):
                '''
                We say a triple of a, b, c numbers can form a triangle if:
                a + b > c
                or 
                a + c > b
                or 
                b + c > a
                
                In other words, the sum of 2 sides must be greater than the third side.
                '''
                if list[i]+list[j]>list[k] and list[i]+list[k]>list[j] and list[j]+list[k]>list[i]:
                    cnt+=1
                    print(f"found a triangle with sides {list[i]}, {list[j]}, {list[k]}")


    return cnt


sample=[1,2,3,4,5,6,7,8,9]
print(f"this list {sample} has {triangle_counter(sample)} possible triangles")
