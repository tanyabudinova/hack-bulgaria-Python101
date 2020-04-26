import time


def performance(file):
    def inner(func):
        def log(*arguments):
            with open(file, 'w') as f:
                start = time.time()
                func(*arguments)
                end = time.time()
                f.write("{} was called and took {} seconds to complete\n".format(func.__code__.co_name, end - start))
        return log
    return inner


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"


something_heavy()
