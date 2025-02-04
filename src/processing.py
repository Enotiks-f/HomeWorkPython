from typing import List, Dict


def filter_by_state(transactions: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """Фильтрует список словарей по значению ключа state."""
    filter_list = []
    for i in transactions:
        if i['state'] == state:
            filter_list.append(i)
    return filter_list


def sort_by_date(transactions: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """Сортирует список словарей по ключу 'date' без использования datetime."""
    return sorted(transactions, key=lambda tx: tx['date'], reverse=reverse)
