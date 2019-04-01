if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for i in range(0,N):
        tmp_str= input()
        tmp_str_ar=tmp_str.strip().split(" ")
        cmd=tmp_str_ar[0]
        if(cmd=="print"):
            print(my_list)
        elif(cmd=="sort"):
            my_list.sort()
        elif(cmd=="reverse"):
            my_list.reverse()
        elif(cmd=="pop"):
            my_list.pop()
        elif(cmd=="count"):
            val=int(tmp_str_ar[1])
            my_list.count(val)
        elif(cmd=="index"):
            val=int(tmp_str_ar[1])
            my_list.index(val)
        elif(cmd=="remove"):
            val=int(tmp_str_ar[1])
            my_list.remove(val)
        elif(cmd=="append"):
            val=int(tmp_str_ar[1])
            my_list.append(val)
        elif(cmd=="insert"):
            pos=int(tmp_str_ar[1])
            val=int(tmp_str_ar[2])
            my_list.insert(pos,val)
