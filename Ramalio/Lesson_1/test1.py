def to_normal_number(binar_number: str) -> int:
    bin_num_list = [int(item) for item in reversed(binar_number)]
    normal_number = 0
    new_num_list = []
    for index, value in enumerate(bin_num_list):
        if value == 1:
            new_num = 2**index
            new_num_list.append(new_num)
            normal_number += new_num
    # print(new_num_list[::-1])

    return normal_number


def to_binar_number(normal_number: int) -> str:
    binar_list = []
    while normal_number > 0:
        result = normal_number % 2
        binar_list.append(str(result))
        normal_number //= 2
    binar_number = ""
    for char in reversed(binar_list):
        binar_number += char

    return binar_number


print(to_normal_number("10011101"))
print(to_binar_number(157))


"""Разделить число на 2.
Записать остаток от деления.
Повторить шаги 1 и 2 со следующим частным, пока оно не станет равным 0.
Записать все остатки от деления в обратном порядке.
Источник: https://uchet-jkh.ru/i/perevod-iz-desyaticnoi-v-dvoicnuyu-sistemu-scisleniya"""
