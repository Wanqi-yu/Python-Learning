#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025/7/18 17:38
# @Author : wanqi.yu
# @File : Day_20.py
# @Software: PyCharm
'''
协程与异步
协程(co-routine):又称微线程，纤程，是一种多方协作的工作方式，协程不是进程或者线程，其执行过程类似于Python的函数调用
Python 的 asyncio 模块实现的异步IO编程框架中，协程是对使用 async 关键字定义的异步函数的调用。当前执行者在某个时刻主动让出（yield）控制流，
并记住自身当前的状态，以便在控制流返回时能从上次让出的位置恢复（resume）执行。
一个进程包含多个线程,类似于一个人体组织有多种细胞在工作，同样，一个程序可以包含多个协程。多个线程相对独立，线程的切换受系统控制。
同样，多个协程也相对独立，但是其切换由程序自己控制。简而言之，协程的核心思想就在于执行者对控制流的 “主动让出” 和 “恢复”。
相对于，线程此类的 “抢占式调度” 而言，协程是一种 “协作式调度” 方式，协程之间执行任务按照一定顺序交替执行。
协程的本质
协程是一种用户态线程，由程序员控制切换时机，具有以下核心特性：

有状态：保存执行上下文（局部变量、指令指针）

可暂停/恢复：在特定点暂停并稍后恢复

协作式调度：需显式让出控制权

轻量级：上下文切换开销极小（约100ns）

'''
import asyncio


# 协程状态示例
async def stateful_coroutine():
    counter = 0
    while True:
        counter += 1
        # 暂停点，保留counter状态
        await asyncio.sleep(1)
        print(f"Counter: {counter}")






'''
事件循环架构
事件循环是异步程序的核心引擎
+---------------------+
|     Event Loop      |
+---------------------+
|   |   |   |   |   |   |
|   v   v   v   v   v   |
| +-------------------+ |
| |   Ready Queue     | |
| | (可运行任务队列)    | |
| +-------------------+ |
|          |            |
|          v            |
| +-------------------+ |
| |   I/O Poller      | |
| | (I/O事件监视器)    | |
| +-------------------+ |
|          |            |
|          v            |
| +-------------------+ |
| |   Timer Heap      | |
| | (定时器堆)         | |
| +-------------------+ |
+-----------------------+
工作流程：

从就绪队列取出任务执行

任务遇到await暂停时：

注册I/O事件到I/O Poller

或添加定时器到Timer Heap

当I/O事件就绪或定时器到期，将关联任务加入就绪队列

循环执行


'''


'''
底层实现原理
生成器基础
Python协程基于生成器实现
'''
def simple_coroutine():
    print("-> 协程启动")
    x = yield  # 暂停点1
    print("-> 收到值:", x)
    y = yield  # 暂停点2
    print("-> 收到值:", y)

# 使用示例
coro = simple_coroutine()
next(coro)      # 启动协程 -> 协程启动
coro.send(10)   # 恢复执行 -> 收到值: 10
coro.send(20)   # 恢复执行 -> 收到值: 20


'''
async/await 语法糖
async/await 是生成器的语法增强：
'''
# # 等效转换
# async def async_coroutine():
#     await some_operation()
#
# # ≈
# def generator_coroutine():
#     yield from some_operation()


'''
协程执行状态机
+--------+     启动     +----------+     完成     +--------+
| CREATED | ----------> | PENDING  | ----------> | DONE   |
+--------+             +----------+             +--------+
                         |    ^
                         |    |
                     暂停 |    | 恢复
                         v    |
                     +----------+
                     | SUSPENDED|
                     +----------+
                     
状态转换：

CREATED: 协程对象已创建但未执行

PENDING: 正在执行中

SUSPENDED: 在await处暂停

DONE: 执行完成（正常结束或异常）

高级特性与应用
异步上下文管理器

'''


# class AsyncDatabaseConnection:
#     async def __aenter__(self):
#         self.conn = await connect_to_db()
#         return self.conn
#
#     async def __aexit__(self, exc_type, exc, tb):
#         await self.conn.close()
#
#
# # 使用
# async with AsyncDatabaseConnection() as conn:
#     data = await conn.query("SELECT...")


'''
异步迭代器

'''


class AsyncDataStream:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.i >= self.n:
            raise StopAsyncIteration

        # 模拟异步数据获取
        await asyncio.sleep(0.1)
        data = f"数据块-{self.i}"
        self.i += 1
        return data


# 使用
async for chunk in AsyncDataStream(5):
    print(chunk)



'''
异步编程:
异步编程允许程序在等待某些操作（如I/O操作、网络请求或定时器）完成时不阻塞（即不停止）主线程的执行，从而提高程序的效率和响应速度。
在异步编程中，程序可以启动一个长时间运行的任务，然后继续执行其他任务，而无需等待该任务完成
Python有哪些可以实现异步编程
1.greentlet:一个python的三方模块,通过将函数作为参数放到greenlet()中,并在函数内部通过switch()函数切换.

2.yield: 想必大家都对这个不陌生,  Python的生成器yield和yield from也可以实现协程代码

'''


def func1():
    yield 1
    yield from func2()
    yield 2


def func2():
    yield 3
    yield 4


f1 = func1()
for item in f1:
    print(item)


'''
异步编程(asyncio)
        基于async & await关键字的协程可以实现异步编程，这也是目前python异步相关的主流技术
        
什么是事件循环
事件循环，可以把他当做是一个while循环，这个while循环在周期性的运行并执行一些任务，在特定条件下终止循环。
其实也可以理解为就是创建一个死循环,比如while循环;不过这个死循环里面会周期性运行和执行任务,在特定条件下终止循环
比如利用如下asyncio可以通过此来获取和创建事件循环.

'''
import asyncio

loop = asyncio.get_event_loop()

'''
asyncio
        在Python3.4之前官方未提供协程的类库，一般大家都是使用greenlet等其他来实现。在Python3.4发布后官方正式支持协程，即：asyncio模块。
'''

import asyncio


@asyncio.coroutine
def func1():
    print(1)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    print(2)


@asyncio.coroutine
def func2():
    print(3)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

'''
注意：基于asyncio模块实现的协程比之前的要更厉害，因为他的内部还集成了遇到IO耗时操作自动切换的功能
'''


'''
async & await
async & await 关键字在Python3.5版本中正式引入，基于它编写的协程代码其实就是 上一示例 的加强版，让代码可以更加简便.
Python3.8之后 @asyncio.coroutine 装饰器就会被移除，推荐使用async & await 关键字实现协程代码。
'''
import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))


'''
关于协程有多种实现方式，目前主流使用是Python官方推荐的asyncio模块和async&await关键字的方式，例如：在tonado、sanic、fastapi、django3 中均已支持.

        程序中，如果想要执行协程函数的内部代码，需要 事件循环 和 协程对象 配合才能实现，如:

'''

import asyncio


async def func():
    print("协程内部代码")


# 调用协程函数，返回一个协程对象。
result = func()

# 方式一
# loop = asyncio.get_event_loop() # 创建一个事件循环
# loop.run_until_complete(result) # 将协程当做任务提交到事件循环的任务列表中，协程执行完成之后终止。

# 方式二
# 本质上方式一是一样的，内部先 创建事件循环 然后执行 run_until_complete，一个简便的写法。
# asyncio.run 函数在 Python 3.7 中加入 asyncio 模块，
asyncio.run(result)

'''
这个过程可以简单理解为：将协程当做任务添加到 事件循环 的任务列表，然后事件循环检测列表中的协程是否 已准备就绪（默认可理解为就绪状态），如果准备就绪则执行其内部代码。

        await是一个只能在协程函数中使用的关键字，用于遇到IO操作时挂起 当前协程（任务），当前协程（任务）挂起过程中 事件循环可以去执行其他的协程（任务），当前协程IO处理完成时，可以再次切换回来执行await之后的代码

'''

'''
Task对象
        Task用于并发调度协程, 通过asyncio.create_task(协程对象)的方式创建Task对象,这样可以让协程加入事件循环中等待被调度执行, 除了使用 asyncio.create_task() 函数以外，还可以用低层级的 loop.create_task() 或 ensure_future() 函数。不建议手动实例化 Task 对象。

        本质上是将协程对象封装成task对象，并将协程立即加入事件循环，同时追踪协程的状态。

        注意：asyncio.create_task() 函数在 Python 3.7 中被加入。在 Python 3.7 之前，可以改用低层级的 asyncio.ensure_future() 函数。

'''

import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    print("main开始")

    # 创建协程，将协程封装到Task对象中并添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
    # 在调用
    task_list = [
        asyncio.create_task(func(), name="n1"),
        asyncio.create_task(func(), name="n2")
    ]

    print("main结束")

    # 当执行某协程遇到IO操作时，会自动化切换执行其他任务。
    # 此处的await是等待所有协程执行完毕，并将所有协程的返回值保存到done
    # 如果设置了timeout值，则意味着此处最多等待的秒，完成的协程返回值写入到done中，未完成则写到pending中。
    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done, pending)


asyncio.run(main())
'''
注意：asyncio.wait 源码内部会对列表中的每个协程执行ensure_future从而封装为Task对象，所以在和wait配合使用时task_list的值为[func(),func()] 也是可以的。
'''

import asyncio


async def func():
    print("执行协程函数内部代码")

    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    response = await asyncio.sleep(2)

    print("IO请求结束，结果为：", response)


coroutine_list = [func(), func()]

# 错误：coroutine_list = [ asyncio.create_task(func()), asyncio.create_task(func()) ]
# 此处不能直接 asyncio.create_task，因为将Task立即加入到事件循环的任务列表，
# 但此时事件循环还未创建，所以会报错。


# 使用asyncio.wait将列表封装为一个协程，并调用asyncio.run实现执行两个协程
# asyncio.wait内部会对列表中的每个协程执行ensure_future，封装为Task对象。
done, pending = asyncio.run(asyncio.wait(coroutine_list))

'''
asyncio.Future对象
        asyncio中的Future对象是一个相对更偏向底层的可对象，通常我们不会直接用到这个对象，而是直接使用Task对象来完成任务的并和状态的追踪.(Task 是 Futrue的子类)Future为我们提供了异步编程中的 最终结果 的处理(Task类也具备状态处理的功能)

'''
import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result("666")


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # 创建一个任务（Future对象），没绑定任何行为，则这个任务永远不知道什么时候结束。
    fut = loop.create_future()

    # 创建一个任务（Task对象），绑定了set_after函数，函数内部在2s之后，会给fut赋值。
    # 即手动设置future任务的最终结果，那么fut就可以结束了。
    await loop.create_task(set_after(fut))

    # 等待 Future对象获取 最终结果，否则一直等下去
    data = await fut
    print(data)


asyncio.run(main())

'''
扩展：支持 await 对象语 法的对象课成为可等待对象，所以 协程对象、Task对象、Future对象 都可以被成为可等待对象。
'''

'''
 futures.Future对象
        在Python的concurrent.futures模块中也有一个Future对象，这个对象是基于线程池和进程池实现异步操作时使用的对象。
'''

import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def func(value):
    time.sleep(1)
    print(value)


pool = ThreadPoolExecutor(max_workers=5)
# 或 pool = ProcessPoolExecutor(max_workers=5)


for i in range(10):
    fut = pool.submit(func, i)
    print(fut)

'''
两个Future对象是不同的,他们是为不同的应用场景而设计,例如:concurrent.futures.Future不支持await语法等.

        在Python提供了一个将futures.Future 对象包装成asyncio.Future对象的函数 asynic.wrap_future。接下里你肯定问：为什么python会提供这种功能？

        其实，一般在程序开发中我们要么统一使用 asycio 的协程实现异步操作、要么都使用进程池和线程池实现异步操作。但如果 协程的异步和 进程池/线程池的异步 混搭时，那么就会用到此功能了。

'''
import time
import asyncio
import concurrent.futures


def func1():
    # 某个耗时操作
    time.sleep(2)
    return "SB"


async def main():
    loop = asyncio.get_running_loop()

    # 1. Run in the default loop's executor ( 默认ThreadPoolExecutor )
    # 第一步：内部会先调用 ThreadPoolExecutor 的 submit 方法去线程池中申请一个线程去执行func1函数，并返回一个concurrent.futures.Future对象
    # 第二步：调用asyncio.wrap_future将concurrent.futures.Future对象包装为asycio.Future对象。
    # 因为concurrent.futures.Future对象不支持await语法，所以需要包装为 asycio.Future对象 才能使用。
    fut = loop.run_in_executor(None, func1)
    result = await fut
    print('default thread pool', result)

    # 2. Run in a custom thread pool:
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await loop.run_in_executor(
    #         pool, func1)
    #     print('custom thread pool', result)

    # 3. Run in a custom process pool:
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(
    #         pool, func1)
    #     print('custom process pool', result)


asyncio.run(main())

'''
  应用场景：当项目以协程式的异步编程开发时，如果要使用一个第三方模块，而第三方模块不支持协程方式异步编程时，就需要用到这个功能，例如：


'''

import asyncio
import requests


async def download_image(url):
    # 发送网络请求，下载图片（遇到网络下载图片的IO请求，自动化切换到其他任务）
    print("开始下载:", url)

    loop = asyncio.get_event_loop()
    # requests模块默认不支持异步操作，所以就使用线程池来配合实现了。
    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print('下载完成')
    # 图片保存到本地文件
    file_name = url.rsplit('_')[-1]
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)


if __name__ == '__main__':
    url_list = [
        'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
        'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
        'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
    ]

    tasks = [download_image(url) for url in url_list]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

'''

'''