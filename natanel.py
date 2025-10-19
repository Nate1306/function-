def guest_name():
    return input("enter a guest")
def less_than(lst,N):
    return len(lst) < N
def check_in(nm,lst):
    return nm in lst


guest_list=[]
for x in range(3):
    guest_list.append(guest_name())
print(guest_list)
while less_than(guest_list,12):
    n=guest_name()
    if not(check_in(n,guest_list)):
        if (len(guest_list)+1)%2==0:
            guest_list.insert(0,n)
        else:
            guest_list.append(n)
    else:
        print(n,"is already invited")
print(guest_list)
