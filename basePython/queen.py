"""
   队列的先进先出
"""
import collections


class Quenqu(object):
    def __init__(self):
        self.item = []
    def push(self,value):
        # 参考栈的写法
        self.item.append(value)
    def pop(self):
        # 按照数组的特性弹出
        return self.item.pop(0)


    pass




class Mystack(object):
    def __init__(self):
        self.stack = collections.deque([])

    def push(self,x):
        self.stack.append(x)
        q = self.stack
        for i in range(len(q)-1):
            q.append(q.popleft())

    def pop(self):
        return self.stack.popleft()

if __name__ == '__main__':
    # q = Quenqu()
    # q.push(1)
    # q.push(2)
    # q.push(3)
    #
    # print(q.pop())
    # print(q.pop())
    # print(q.pop())

    stack = Mystack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
# select * from a_table a inner join b_table b on a.id == b.id;
#



