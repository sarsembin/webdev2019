if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        stroka = input()
        splitter = stroka.split(" ")
        imya = splitter[0]
        n1=float(splitter[1])
        n2=float(splitter[2])
        n3=float(splitter[3])
        n_avg=(n1+n2+n3)/3.0
        student_marks[imya]="%.2f" % n_avg
    s_name=input()
    print(student_marks[s_name])
