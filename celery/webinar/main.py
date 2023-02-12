import datetime
from tasks import hard_function


def main():
    async_result_1 = hard_function.delay(2)
    async_result_2 = hard_function.delay(2)

    print(async_result_1.get())
    print(async_result_2.get())


if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    print(datetime.datetime.now() - start)
