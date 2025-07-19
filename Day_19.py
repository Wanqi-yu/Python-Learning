#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/17 18:43
# @Author : wanqi.yu
# @File : Day_19.py
# @Software: PyCharm
'''
多进程
多进程:多进程指的是操作系统同时支持多个处理器的能力，在支持多任务操作时，一个应用程序会被分解成多个独立运行的较小的程序，操作系统会将这些
线程分配到多核处理器，以提升系统性能。
为什么要使用多进程
假设我们的计算机只有一个单核的处理器，然后同时被分配了几个任务，那么它就不得不在各个任务中来回切换，短暂地执行其中一个任务，然后中断，
然后短暂地执行下一个任务，以保持所有的进程都在运行。这就像一个厨师在做面条，切几秒钟菜，跑去揉几下面，再赶紧查看下汤。

所以同时需要完成的任务越多，同时跟踪所有的任务就越困难。这就是多进程的必要性，也是多核处理器的威力所在。

一个支持多进程的操作系统可以做到：

同时指挥多个CPU，即拥有一个以上的CPU的计算机
指挥多核CPU，即拥有两个及以上的独立处理单元的CPU
这样，计算机就可以轻松地同时执行多个任务，每个任务都可以使用自己的处理器。就像之前举的例子，现在厨房里有专门的揉面师傅，备菜师傅，煮汤师傅。事情就变得轻松多了。

用Python执行多进程
Python中的多进程是通过multiprocessing包来实现的，和多线程的threading.Thread差不多，它可以利用multiprocessing.
Process对象来创建一个进程对象。这个进程对象的方法和线程对象的方法差不多也有start(), run(), join()等方法，
其中有一个方法不同Thread线程对象中的守护线程方法是setDeamon，而Process进程对象的守护进程是通过设置daemon属性来完成的。
Python多进程实现方法一
'''
# from multiprocessing import  Process
#
# def fun1(name):
#     print('测试%s多进程' %name)
#
# if __name__ == '__main__':
#     process_list = []
#     for i in range(5):  #开启5个子进程执行fun1函数
#         p = Process(target=fun1,args=('Python',)) #实例化进程对象
#         p.start()
#         process_list.append(p)
#
#     for i in process_list:
#         p.join()
#
#     print('结束测试')
'''
上面的代码开启了5个子进程去执行函数，我们可以观察结果，是同时打印的，这里实现了真正的并行操作，就是多个CPU同时执行任务。
我们知道进程是python中最小的资源分配单元，也就是进程中间的数据，内存是不共享的，每启动一个进程，都要独立分配资源和拷贝访问的数据，
所以进程的启动和销毁的代价是比较大了，所以在实际中使用多进程，要根据服务器的配置来设定。
'''

'''
Python多进程实现方法二
'''
# from multiprocessing import  Process
#
# class MyProcess(Process): #继承Process类
#     def __init__(self,name):
#         super(MyProcess,self).__init__()
#         self.name = name
#
#     def run(self):
#         print('测试%s多进程' % self.name)
#
#
# if __name__ == '__main__':
#     process_list = []
#     for i in range(5):  #开启5个子进程执行fun1函数
#         p = MyProcess('Python') #实例化进程对象
#         p.start()
#         process_list.append(p)
#
#     for i in process_list:
#         p.join()
#
#     print('结束测试')

'''
效果和第一种方式一样。

我们可以看到Python多进程的实现方式和多线程的实现方式几乎一样。
Process类的其他方法
构造方法：

Process([group [, target [, name [, args [, kwargs]]]]])
　　group: 线程组 
　　target: 要执行的方法
　　name: 进程名
　　args/kwargs: 要传入方法的参数

实例方法：
　　is_alive()：返回进程是否在运行,bool类型。
　　join([timeout])：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。
　　start()：进程准备就绪，等待CPU调度
　　run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。
　　terminate()：不管任务是否完成，立即停止工作进程

属性：
　　daemon：和线程的setDeamon功能一样
　　name：进程名字
　　pid：进程号

Python多线程的通信
进程是系统独立调度核分配系统资源（CPU、内存）的基本单位，进程之间是相互独立的，每启动一个新的进程相当于把数据进行了一次克隆，
子进程里的数据修改无法影响到主进程中的数据，不同子进程之间的数据也不能共享，这是多进程在使用中与多线程最明显的区别。
但是难道Python多进程中间难道就是孤立的吗？当然不是，python也提供了多种方法实现了多进程中间的通信和数据共享（可以修改一份数据）
进程队列Queue
Queue在多线程中也说到过，在生成者消费者模式中使用，是线程安全的，是生产者和消费者中间的数据管道，那在python多进程中，
它其实就是进程之间的数据管道，实现进程通信。

'''

# from multiprocessing import Process,Queue
#
#
# def fun1(q,i):
#     print('子进程%s 开始put数据' %i)
#     q.put('我是%s 通过Queue通信' %i)
#
# if __name__ == '__main__':
#     q = Queue()
#
#     process_list = []
#     for i in range(3):
#         p = Process(target=fun1,args=(q,i,))  #注意args里面要把q对象传给我们要执行的方法，这样子进程才能和主进程用Queue来通信
#         p.start()
#         process_list.append(p)
#
#     for i in process_list:
#         p.join()
#
#     print('主进程获取Queue数据')
#     print(q.get())
#     print(q.get())
#     print(q.get())
#     print('结束测试')

'''
上面的代码结果可以看到我们主进程中可以通过Queue获取子进程中put的数据，实现进程间的通信。
管道Pipe
管道Pipe和Queue的作用大致差不多，也是实现进程间的通信

'''

# from multiprocessing import Process, Pipe
# def fun1(conn):
#     print('子进程发送消息：')
#     conn.send('你好主进程')
#     print('子进程接受消息：')
#     print(conn.recv())
#     conn.close()
#
# if __name__ == '__main__':
#     conn1, conn2 = Pipe() #关键点，pipe实例化生成一个双向管
#     p = Process(target=fun1, args=(conn2,)) #conn2传给子进程
#     p.start()
#     print('主进程接受消息：')
#     print(conn1.recv())
#     print('主进程发送消息：')
#     conn1.send("你好子进程")
#     p.join()
#     print('结束测试')

'''
上面可以看到主进程和子进程可以相互发送消息
Managers
Queue和Pipe只是实现了数据交互，并没实现数据共享，即一个进程去更改另一个进程的数据。那么久要用到Managers

'''

# from multiprocessing import Process, Manager
#
# def fun1(dic,lis,index):
#
#     dic[index] = 'a'
#     dic['2'] = 'b'
#     lis.append(index)    #[0,1,2,3,4,0,1,2,3,4,5,6,7,8,9]
#     #print(l)
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         dic = manager.dict()#注意字典的声明方式，不能直接通过{}来定义
#         l = manager.list(range(5))#[0,1,2,3,4]
#
#         process_list = []
#         for i in range(10):
#             p = Process(target=fun1, args=(dic,l,i))
#             p.start()
#             process_list.append(p)
#
#         for res in process_list:
#             res.join()
#         print(dic)
#         print(l)

'''
进程池
进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，
直到进程池中有可用进程为止。就是固定有几个进程可以使用。
进程池中有两个方法：

apply：同步，一般不使用

apply_async：异步
'''

from  multiprocessing import Process,Pool
import os, time, random

def fun1(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    pool = Pool(5) #创建一个5个进程的进程池

    for i in range(10):
        pool.apply_async(func=fun1, args=(i,))

    pool.close()
    pool.join()
    print('结束测试')












