from src import masks

input_card_number = int(input())
input_account = int(input())

print(masks.get_mask_card_number(input_card_number))
print(masks.get_mask_account(input_account))
