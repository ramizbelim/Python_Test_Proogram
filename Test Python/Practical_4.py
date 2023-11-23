number = int(input("Enter length of list : "))
number_list =[]
for i in range(number):
    ele = int(input("Element of list :"))
    number_list.append(ele)
target_from_user = int(input("Enter target :"))
def index_target(list):
    index = []
    for i in range(len(list)):
        for j in range(1,len(list)-1):
            if list[i] + list[j] == target_from_user :
                index.append(i)
                index.append(j)
    return index
#This give repeted index
print(index_target(number_list))
# This give not repeted index
# print(list(set(index_target(number_list))))
