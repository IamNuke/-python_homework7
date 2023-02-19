def num_of_vocals(p_string, v_string):
    count = 0
    for letter in p_string:
        count += v_string.count(letter)
    return count

my_string = input("Введите стихотворение (на русском алфавите): ")
# my_string = "пара-ра-рам рам-пам-папам па-ра-па-да"
vocals = "уеыаоэяию"
new_list = my_string.split()
new_set = {num_of_vocals(item, vocals) for item in new_list}
if len(new_set) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
