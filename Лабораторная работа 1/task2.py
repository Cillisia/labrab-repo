# TODO Найдите количество книг, которое можно разместить на дискете
import math
size_of_one_in_bytes = 100*50*25*4
memory_in_bytes = 1.44*1024*1024
num_of_books = math.floor(memory_in_bytes/size_of_one_in_bytes)
print("Количество книг, помещающихся на дискету:", num_of_books)
