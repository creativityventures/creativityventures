"""Documentary model of EIP-2930 access-list accounting.

It isolates the accounting rule so an estimator can expose assumptions instead
of silently treating every storage read as equally priced.
"""
COLD_ACCOUNT = 2600
WARM_ACCOUNT = 100
COLD_STORAGE = 2100
WARM_STORAGE = 100
ACCESS_LIST_ADDRESS = 2400
ACCESS_LIST_STORAGE_KEY = 1900

def access_list_cost(addresses: int, storage_keys: int) -> int:
    return addresses * ACCESS_LIST_ADDRESS + storage_keys * ACCESS_LIST_STORAGE_KEY

def first_touch_cost(accounts: int, slots: int) -> int:
    return accounts * COLD_ACCOUNT + slots * COLD_STORAGE

def warm_touch_cost(accounts: int, slots: int) -> int:
    return accounts * WARM_ACCOUNT + slots * WARM_STORAGE

def net_delta(accounts: int, slots: int) -> int:
    return access_list_cost(accounts, slots) + warm_touch_cost(accounts, slots) - first_touch_cost(accounts, slots)

if __name__ == "__main__":
    print(net_delta(1, 2))
