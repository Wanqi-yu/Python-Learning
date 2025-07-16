#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/16 17:52
# @Author : wanqi.yu
# @File : Day_18.py
# @Software: PyCharm
'''
备注:笔者由于暂时不太理解，所以将教程内容写入，后续实际使用时更新
目前笔者处于学习阶段，之前也有学习过PYthon，但经常是三天打鱼，两天晒网，三分钟热度，一度学习到自动化办公，后续因为一直未使用，就忘掉了

一直到今年才决定开始认真学习，确认了学习方向，制定了学习计划
每周一到周五学习，周六日练习
学习目的是为了提升个人能力，将编程与工作结合，本身工作为运维工程师，但由于运维的系统稳定，不常使用脚本等
现在学习主方向为Python，本身已学习了关系型数据库，后续辅修C#，转向测试或运维开发方向
学习感悟:不用定太久太难的计划，可以先定一下简单快速，如100天学习，每天学习30-60分钟，要有足够的练习，以及要提升逻辑思维
以及一定要自己编写代码，只有自己编写才能发现自己学习的不足
教材来源:CSDN

版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
原文链接：https://blog.csdn.net/Xiao_Liu_OvO/article/details/138716321


多线程基础
对于一个Python程序，如果需要同时大量处理多个任务，有使用多进程和多线程两种方法。
在python中，实现多线程主要通过threading模块，而多进程主要通过multiprocessing模块。
这两个模块的主要区别是：threading模块基于线程，而multiprocessing模块基于进程
需要注意的是，由于python中的GIL锁的存在，Python解释器只允许一个Python进程使用，这意味着对于一个解释器只允许一个进程在运行，
这也是为什么threading模块无法适用于CPU密集型这类需要大量CPU资源的任务，因为一个进程的CPU资源有限，无论开启多少个线程，
总的资源就只有那些，总耗时不会有太大变化。而multiprocessing模块则可以开多个进程，能够更快速的处理CPU密集型任务。

多线程:线程(thread)是操作系统中能够进行运算的最小单位，包含于进程之中，一个进程可以有多个线程，这意味着一个进程中可以并发多个线程，即为多线程
并发:学习多线程时会遇到一个名词 并发，这是属于操作系统中的词汇，与并发类似的还有并行
并发的概念
并发是指一个处理器同时处理多个任务
并行
并行是指多个处理器或多核处理器同时处理多个不同的任务
并发与并行的不同
并发是逻辑上的同时发生，而并行是物理上的同时发生
来个比喻
并发是一个人同时吃三个东西，而并行是三个人同时吃三个东西
并发:(concurrency)：指在同一时刻只能有一条指令执行，但多个进程指令被快速的轮换执行，使得在宏观上具有多个进程同时执行的效果，
但在微观上并不是同时执行的，只是把时间分成若干段，使多个进程快速交替的执行。
并行(parallel)：指在同一时刻，有多条指令在多个处理器上同时执行。
线程完整生命周期
一个线程完整的生命周期包括新建——就绪——运行——阻塞——死亡。

新建：即新创建一个线程对象
就绪：调用start方法后，线程对象等待运行，什么时候开始运行取决于调度
运行：线程处于运行状态
阻塞：处于运行状态的线程被堵塞，通俗理解就是被卡住了，可能的原因包括但不限于程序自身调用sleep方法阻塞线程运行，或调用了一个阻塞式I/O方法，被阻塞的进程会等待何时解除阻塞重新运行
死亡：线程执行完毕或异常退出，线程对象被销毁并释放内存

主线程与子线程
我们讲的多线程实际上指的就是只在主线程中运行多个子线程，而主线程就是我们的python编译器执行的线程，所有子线程和主线程都同属于一个进程。
在未添加子线程的情况下，默认就只有一个主线程在运行，他会将我们写的代码从开头到结尾执行一遍，后文中我们也会提到一些主线程与子线程的关系。
下面是代码示例
'''

'''
使用Thread创建线程对象
Thread类创建新线程的基本语法如下：

Newthread = Thread(target=function, args=(argument1,argument2,...))

Newthread: 创建的线程对象
function: 要执行的函数
argument1,argument2: 传递给线程函数的参数，为tuple类型

'''
#导入threading库中的Thread函数
from threading import Thread
#导入time库
import time
#导入time库中的sleep函数
from time import sleep


def task(threadName, number, letter):
    print(f"【线程开始】{threadName}")
    m = 0
    while m < number:
        sleep(1)
        m += 1
        current_time = time.strftime('%H:%M:%S', time.localtime())
        print(f"[{current_time}] {threadName} 输出 {letter}")
    print(f"【线程结束】{threadName}")


# thread1 = Thread(target=task, args=("thread_1", 4, "a"))  # 线程1：执行任务打印4个a
# thread2 = Thread(target=task, args=("thread_2", 2, "b"))  # 线程2：执行任务打印2个b
#
# thread1.start()  # 线程1开始
# thread2.start()  # 线程2开始
#
# thread1.join()
# thread2.join()

'''
这个例子中，线程thread1和thread2同时开始，thread2打印2个b后结束，而thread1继续打印a直到完成。
'''


'''
使用join阻塞线程
在前一个实例中我们可以看到在结尾有thread1.join()和thread2.join()两个语句，这两个语句出现在末尾表示主线程会等待所有的子线程执行完成，
当然了，由于默认我们创建的子线程是前台线程（这个概念会在后面提到），如果没有join语句主线程也会等待所有子线程执行完毕才退出。

join方法可以用于阻塞主线程的顺序执行，因此，在主线程中使用可以调整各个子线程的执行顺序，了解完这些之后，我们来看下一个实例。

'''
thread1 = Thread(target=task, args=("thread_1", 6, "a"))  # 线程1：假设任务为打印6个a
thread2 = Thread(target=task, args=("thread_2", 4, "b"))  # 线程2：假设任务为打印4个b
thread3 = Thread(target=task, args=("thread_3", 2, "c"))  # 线程3：假设任务为打印2个c

thread1.start()  # 线程1启动
thread2.start()  # 任务2启动
thread2.join()  # 等待线程2
thread3.start()  # 线程2完成任务后线程3才启动
thread1.join()  # 等待线程1完成线程
thread3.join()  # 等待线程3完成线程
'''
输出:【线程开始】thread_1
【线程开始】thread_2
[13:44:20] thread_2 输出 b
[13:44:20] thread_1 输出 a
[13:44:21] thread_2 输出 b
[13:44:21] thread_1 输出 a
[13:44:22] thread_2 输出 b
[13:44:22] thread_1 输出 a
[13:44:23] thread_2 输出 b
【线程结束】thread_2
[13:44:23] thread_1 输出 a
【线程开始】thread_3
[13:44:24] thread_3 输出 c
[13:44:24] thread_1 输出 a
[13:44:25] thread_1 输出 a
[13:44:25] thread_3 输出 c
【线程结束】thread_3
【线程结束】thread_1

由输出可以看出，由于join的加入，thread2.join使得主进程一直在等待thread2线程完成任务，因此直到线程thread2结束后，thread3才开始任务。

由于这里thread1一共打印6个a，thread2打印4个b，thread3打印2个c。thread1的工作量等于thread2+thread3的工作量之和，因此整个程序可以看成是thread1与thread2+thread3并行运行。

'''


'''
重写父类threading.Thread创建线程
实例1和2中，我们已经介绍了如何直接导入Thread函数创建线程以及如何利用join方法，但是这种创建线程的方法本质上使用的是其父类的默认设置，具有局限性。
在实例3中，将进一步深入探讨如何继承并重写父类threading.Thread类创建子线程。
'''
import threading

# class myThread(threading.Thread):
#     # 重写父类的构造函数
#     def __init__(self, number, letter):
#         threading.Thread.__init__(self)
#         self.number = number  # 添加number变量
#         self.letter = letter  # 添加letter变量
#
#     # 重写父类中的run函数
#     def run(self):
#         print(f"【线程开始】{self.name}")
#         task1(self.name, self.number, self.letter)
#         print("【线程结束】", self.name)
#
#     # 重写父类析构函数
#     def __del__(self):
#         print("【线程销毁释放内存】", self.name)


# 自定义的函数，此处可以替换成任何其他想要多线程执行的任务
# def task1(threadName, number, letter):
#     m = 0
#     while m < number:
#         sleep(1)
#         m += 1
#         current_time = time.strftime('%H:%M:%S', time.localtime())
#         print(f"[{current_time}] {threadName} 输出 {letter}")
#
#
# thread1 = myThread(4, "a")  # 创建线程thread1：任务耗时2s
# thread2 = myThread(2, "b")  # 创建线程thread2：任务耗时4s
#
# thread1.start()  # 启动线程1
# thread2.start()  # 启动线程2
#
# thread1.join()  # 等待线程1
# thread2.join()  # 等待线程2


'''
输出为:
【线程开始】Thread-1
【线程开始】Thread-2
[10:37:58] Thread-1 输出 a
[10:37:58] Thread-2 输出 b
[10:37:59] Thread-1 输出 a
[10:37:59] Thread-2 输出 b
【线程结束】 Thread-2
[10:38:00] Thread-1 输出 a
[10:38:01] Thread-1 输出 a
【线程结束】 Thread-1
【线程销毁释放内存】 Thread-1
【线程销毁释放内存】 Thread-2
从输出中，我们可以清楚的看到两个并行任务从开始到结束，最后一起销毁并释放内存的全过程，很好的体现了线程的一个完整生命周期过程。

最后实现的效果与实例1实现的效果相同，但是使用继承重写父类的方法，可以让我们更加自由的定义各项参数以及定义线程处理的任务，也能让我们对threading模块的理解更加深入。

'''

'''
前台线程与后台线程
在前面的所有实例中，我们忽略了threading.Thread的daemon参数，其默认为False，表示线程默认就是一个前台线程。

前台线程表示当所有的前台线程都执行完毕时，整个程序才退出。将daemon参数设定为True是表示线程是一个后台线程，此时主进程结束时，所有未执行完成的后台线程也都会直接自动结束。
在上一个实例的基础上，在初始化部分加入self.daemon=True，并去掉末尾的join方法，替换成sleep方法来阻塞主程序的运行

'''


# class myThread(threading.Thread):
#     # 重写父类的构造函数
#     def __init__(self, number, letter):
#         threading.Thread.__init__(self)
#         self.number = number  # 添加number变量
#         self.letter = letter  # 添加letter变量
#         self.daemon = True  # 默认前台线程
#
#     # 重写父类中的run函数
#     def run(self):
#         print(f"【线程开始】{self.name}")
#         task1(self.name, self.number, self.letter)
#         print("【线程结束】", self.name)
#
#     # 重写父类析构函数
#     def __del__(self):
#         print("【线程销毁释放内存】", self.name)
#
#
# # 自定义的函数，此处可以替换成任何其他想要多线程执行的任务
# def task1(threadName, number, letter):
#     m = 0
#     while m < number:
#         sleep(1)
#         m += 1
#         current_time = time.strftime('%H:%M:%S', time.localtime())
#         print(f"[{current_time}] {threadName} 输出 {letter}")

'''
输出为
【线程开始】Thread-1
【线程开始】Thread-2
[10:31:45] Thread-1 输出 a
[10:31:45] Thread-2 输出 b
[10:31:46] Thread-1 输出 a
[10:31:46] Thread-2 输出 b
我们用sleep方法强行阻塞了主程序3s，但是由于我们将线程设定为了后台线程，3s过后，主程序将执行完毕，此时两个子线程thread1和thread2无论是否执行完成，都将强行结束。
'''

'''
线程同步（线程锁）
我们设想一下这种情况，当多线程同时执行时，由于threading模块的中线程的变量和数据结构共享，可能会出现多个线程同时修改一个数据的情况，这绝对是不行的。

为了将各个线程同步，我们引入线程锁的概念。当某个线程访问数据时，先对其加锁，其他线程若再想访问这个数据就会被阻塞，直到前一个线程解锁释放。
在threading模块中，加锁和释放锁主要使用Lock类，使用其中的acquire()和release()方法
Lock = threading.Lock()  # 在threading模块中获得锁类
Lock.acquire()  # 设置锁
Lock.release()  # 释放锁
'''
import threading
import time


# 子类myThread继承父类threading.Thread，并进行重写
class myThread(threading.Thread):
    # 重写父类构造函数
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    # 重写父类run函数，在调用start()时自动调用run函数
    def run(self):
        print(f"【线程开始】{self.name}")
        Lock.acquire()  # 设置线程锁
        edit_list(self.name, self.number)
        Lock.release()  # 释放线程锁

    # 重写父类析构函数
    def __del__(self):
        print("【线程销毁】", self.name)


# 自定义的任务函数
def edit_list(threadName, number):
    while number > 0:
        time.sleep(1)
        data_list[number - 1] += 1
        current_time = time.strftime('%H:%M:%S', time.localtime())
        print(f"[{current_time}] {threadName} 修改datalist为{data_list}")
        number -= 1
    print(f"【线程{threadName}完成工作】")


data_list = [0, 0, 0, 0]
Lock = threading.Lock()

# 创建3个子线程
thread1 = myThread(1)
thread2 = myThread(2)
thread3 = myThread(3)

# 启动3个子线程
thread1.start()
thread2.start()
thread3.start()

# 主进程等待所有线程完成
thread1.join()
thread2.join()
thread3.join()

print("【主进程结束】")

'''
【线程开始】Thread-1
【线程开始】Thread-2
【线程开始】Thread-3
[09:55:22] Thread-1 修改datalist为[1, 0, 0, 0]
【线程Thread-1完成工作】
[09:55:23] Thread-2 修改datalist为[1, 1, 0, 0]
[09:55:24] Thread-2 修改datalist为[2, 1, 0, 0]
【线程Thread-2完成工作】
[09:55:25] Thread-3 修改datalist为[2, 1, 1, 0]
[09:55:26] Thread-3 修改datalist为[2, 2, 1, 0]
[09:55:27] Thread-3 修改datalist为[3, 2, 1, 0]
【线程Thread-3完成工作】
【主进程结束】
【线程销毁】 Thread-1
【线程销毁】 Thread-2
【线程销毁】 Thread-3

 当三个线程都需要使用同一个数据时，我们只需要对线程的run方法中进行加锁和释放锁的操作即可。此时三个子线程将会进行顺序操作，
 前一个子线程执行完成释放锁后，后一个线程才会继续执行。要注意的是，这三个子线程使用的需要是同一把锁。
 

'''


















if __name__ == "__main__":
    run_code = 0
