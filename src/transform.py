#!/usr/bin/env python3

def transform(s1, s2):
    s1_modify = split_return(s1)
    s2_modify = split_return(s2)
    temp = list(zip(s1_modify,s2_modify))
    
    temp = list(map(lambda L: L[0]*L[1], temp))

    return temp

def main():
    print(transform("1 5 3", "2 6 -1"))
    
def split_return(l):
    temp_list = l.split()
    temp = []
    for i in temp_list:
        temp.append(int(i))
    return temp

if __name__ == "__main__":
    main()
