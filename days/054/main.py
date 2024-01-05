import time

def timing_decorator(repeat=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(repeat):
                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    print(f"Hata: {e}")
                    result = None
                end_time = time.time()
                elapsed_time = end_time - start_time
                total_time += elapsed_time
                print(f"{func.__name__} çalışma süresi: {elapsed_time} saniye")
            print(f"Ortalama çalışma süresi: {total_time / repeat} saniye")
            return result
        return wrapper
    return decorator

@timing_decorator(repeat=3)
def calculation(x, y):
    result = 0
    for _ in range(1000000):
        result += x * y
    return result


result = calculation(2, 3)
print("Sonuç:", result)
