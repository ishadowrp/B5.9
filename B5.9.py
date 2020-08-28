import time

class Benchmark:

    def __init__(self, NUM_RUNS = 10):
        self.NUM_RUNS = NUM_RUNS
        self.t0 = 0
        self.t1 = 0

    def __call__(self, func):
        def runs_benchmark(*args, **kwargs):
            total = 0
            for i in range(self.NUM_RUNS):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/self.NUM_RUNS))
            return return_value
        return runs_benchmark

# Для того чтоб получить ответ отличный от нуля лучше всего задавать максимально большое значение, например: 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
max_element_of_list = input("Введите максимальный элемент для рассчета последовательности Фибоначи: ")

time_this = Benchmark(10)

@time_this
def CreateFibonachiList(maxElement):
    flag = True
    FibonachiList = []
    while flag:
        if len(FibonachiList) < 2:
            FibonachiList.append(1)
            FibonachiList.append(2)
        else:
            newEl = FibonachiList[-1]+FibonachiList[-2]
            if newEl < maxElement:
                FibonachiList.append(newEl)
            else:
                flag = False
    
    return FibonachiList


CreateFibonachiList(int(max_element_of_list))