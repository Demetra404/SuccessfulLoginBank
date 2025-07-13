import time
def add_logfile(filename=None):
    def log(logger):
        def new_param(*args, **kwargs):
            try:
                time_1 = time.time()
                result = logger(*args, **kwargs)
                time_2 = time.time()
            except Exception as error:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{logger.__name__} error: {error}.  input: {args}, {kwargs}\n')
                else:
                    print(f'{logger.__name__} error: {error}.  input: {args}, {kwargs}\n')
            else:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'{logger.__name__} ok, start time: {time_1}, finish time: {time_2}\n')
                else:
                    print(f'{logger.__name__} ok, start time: {time_1}, finish time: {time_2}\n')
        return new_param
    return log

@add_logfile()
def my_function(a, b):
    return a / b
my_function( 10, 0)
