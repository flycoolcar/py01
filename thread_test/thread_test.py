import time
import _thread
import threading


# time.sleep(2)
# print('休息5秒！')

def work(n):
    print(f'{threading.current_thread().name}函数开始于{time.ctime()}')
    time.sleep(n)
    print(f'{threading.current_thread().name}函数结束于{time.ctime()}')


def main():
    print(f'【主程序开始于{time.ctime()}】')
    # work(2)
    # _thread.start_new_thread(work, (2,))
    # _thread.start_new_thread(work, (4,))
    # work(4)
    # time.sleep(4)
    threads = []
    t1 = threading.Thread(target=work, args=(4,))
    threads.append(t1)

    t2 = threading.Thread(target=work, args=(2,))
    threads.append(t2)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f'【主程序结束于{time.ctime()}】')


if __name__ == '__main__':
    main()
