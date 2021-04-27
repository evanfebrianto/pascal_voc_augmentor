from multiprocessing import set_start_method, get_context
import logging
from threading import Thread
from queue import Queue
from logging.handlers import QueueListener, QueueHandler
from multiprocessing import Pool

def setup_logging():
    # Logs get written to a queue, and then a thread reads
    # from that queue and writes messages to a file:
    _log_queue = Queue()
    QueueListener(
        _log_queue, logging.FileHandler("out.log")).start()
    logging.getLogger().addHandler(QueueHandler(_log_queue))

    # Our parent process is running a thread that
    # logs messages:
    def write_logs():
        while True:
            logging.error("hello, I just did something")
    Thread(target=write_logs).start()

def runs_in_subprocess():
    print("About to log...")
    logging.error("hello, I did something")
    print("...logged")

if __name__ == '__main__':
    set_start_method("spawn")
    setup_logging()

    # Meanwhile, we start a process pool that writes some
    # logs. We do this in a loop to make race condition more
    # likely to be triggered.
    while True:
        with get_context('spawn').Pool() as pool:
            pool.apply(runs_in_subprocess)



# from os import fork, getpid

# print("I am parent process", getpid())
# if fork():
#     print("I am the parent process, with PID", getpid())
# else:
#     print("I am the child process, with PID", getpid())


# from threading import Thread, enumerate
# from os import fork
# from time import sleep

# # Start a thread:
# Thread(target=lambda: sleep(60)).start()

# if fork():
#     print("The parent process has {} threads".format(
#         len(enumerate())))
# else:
#     print("The child process has {} threads".format(
#         len(enumerate())))