import threading
import time


def write_words(word_count, file_name):
    file = file_name
    with open(file, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')

func_start_time = time.perf_counter()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
func_end_time = time.perf_counter()
func_elapsed_time = func_end_time - func_start_time
print(f'Время функции: {func_elapsed_time:.6f}')

thread_start_time = time.perf_counter()
threads = [
    threading.Thread(target=write_words, args=(word_count, file_name))
    for word_count, file_name in [(10, 'example5.txt'), (30, 'example6.txt'),
                                  (200, 'example7.txt'), (100, 'example8.txt')]
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

thread_end_time = time.perf_counter()
thread_elapsed_time = thread_end_time - thread_start_time
print(f'Время выполнения потоков: {thread_elapsed_time:.6f} секунд')