def get_mask_card_number(number_card: int) -> str:
    """Функцию маскировки номера банковской карты """
    str_number_card = str(number_card)
    masked = str_number_card[:6] + "*" * 6 + str_number_card[-4:]

    count = 0
    slice_masc = ""
    for i in masked:
        count += 1
        slice_masc += i
        if count % 4 == 0:
            slice_masc += " "
    return slice_masc


def get_mask_account(number_acc: int) -> str:
    """Функцию маскировки номера банковского счета """
    str_number_acc = str(number_acc)
    masked = "**" + str_number_acc[-4:]
    return masked
