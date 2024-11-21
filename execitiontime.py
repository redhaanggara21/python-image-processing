import time

def timer(func):
    """Function decorator to measure execution time of functions."""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # End time
        execution_time = end_time - start_time  # Calculate execution time
        print(f'{func.__name__} executed in: {execution_time} seconds')
        return result
    return wrapper