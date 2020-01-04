# print("小明")
# import random
# for i in range(5):
#     print(i)
# for j in 'string':
#     print(j)
#
# for m in range(0,5):
#     print(m*(random.random()))
#
# def insert_sort(ilist):
#     for i in range(len(ilist)):
#         print(i)
#         for j in range(i):
#             print(j)
#     #         if ilist[i] < ilist[j]:
#     #             ilist.insert(j, ilist.pop(i))
#     #             break
#     # return ilist
#
# ilist = insert_sort([4,5,6,7,3,2,6,9,8])
# print(ilist)

nums = range(2,20)
for i in nums:

    nums = filter(lambda x:x==i or x % i,nums)

nums
data={'id':1,'id1':2,'id2':2,'id3':2}
que_result=list(ProjectAccounts.objects.filter(data).values())
