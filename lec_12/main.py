import random
import time

def create(name):
    with open(name, 'w') as file:
        for _ in range(100):
            line = ' '.join(str(random.randint(1, 100)) for _ in range(20))
            file.write(line + '\n')

def line_to_int_array(line):
    return list(map(int, line.split()))

def filter_nums(arr):
    return list(filter(lambda x: x > 40, arr))

def write(name, data):
    with open(name, 'w') as file:
        for line in data:
            line_str = ' '.join(map(str, line))
            file.write(line_str + '\n')

def read_file(name):
    with open(name, 'r') as file:
        for line in file:
            yield line_to_int_array(line)

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"{func.__name__} executed in {execution_time:.6f} seconds")
        return result
    return wrapper

@measure_execution_time
def main():
    create('data.txt')
    with open('data.txt', 'r') as file:
        lines = [line_to_int_array(line) for line in file]
        print("BEFORE")
        for line in lines:
            print(line)
    filtered_data = [filter_nums(line) for line in lines]
    write('filtered_data.txt', filtered_data)
    generator = read_file('filtered_data.txt')
    print("--------------------------------------------------------")
    print("AFTER")
    for line in generator:
        print(line)

main()
