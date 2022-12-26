import time

def time_delta(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    elapsed = end - start
    print(f"Elapsed time: {elapsed:.6f} seconds")
    return result
  return wrapper

@time_delta
def foo():
  time.sleep(1)

foo()  # Output: Elapsed time: 1.000071 seconds
