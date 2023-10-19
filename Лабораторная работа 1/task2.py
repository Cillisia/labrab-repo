# TODO Найдите количество книг, которое можно разместить на дискете
num_of_pages = 100
num_of_lines = 50
num_of_char = 25
weight_one_char = 4
size_of_one_in_bytes = num_of_pages * num_of_lines * num_of_char * weight_one_char

volume = 1.44
Mb_2_Kb = 1024
Kb_2_b= 1024
memory_in_bytes = volume*Mb_2_Kb*Kb_2_b
num_of_books = int(memory_in_bytes//size_of_one_in_bytes)
print("Количество книг, помещающихся на дискету:", num_of_books)

