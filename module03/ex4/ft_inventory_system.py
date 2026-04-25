import sys

class ItemError(Exception):
    pass

def check_item(arg: str) -> bool:
    for i in arg:
        if i == ':':
            return True
    return False

def create_dict(args: list[str]) -> dict[str, int]:
    inv: dict[str, int] = {}
    for arg in args:
        if check_item(arg) == True:
            name = ""
            value = ""
            for i in range(len(arg)):
                if arg[i] == ":":
                    name = arg[:i]
                    value = arg[i+1:]
        else:
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            value = int(value)
        except ValueError as err:
            print(f"Quantity error for 'key': {err}")
            continue
        if name in inv:
            print(f"Redundant item '{name}' - discarting")
            continue
        inv[name] = value
    return inv


def items_perc(inv: dict[str, int], tot: int) -> None:
    for name, value in inv.items():
        perc: float = (100 * value) / tot
        print(f"Item {name} represents {perc:.1f}%")


def mabund_item(inv: dict[str, int]) -> None:
    max_val: int = 0
    for val in inv.values():
        if val > max_val:
            max_val = val

    for name, val in inv.items():
        if val == max_val:
            print(f"Item most abundant: {name} with quantity {val}")
            break


def labund_item(inv: dict[str, int]) -> None:
    values: list[int] = list(inv.values())
    min_val: int = values[0]
    for val in inv.values():
        if val < min_val:
            min_val = val

    for name, val in inv.items():
        if val == min_val:
            print(f"Item least abundant: {name} with quantity {val}")
            break


def main() -> None:
    argn = len(sys.argv)
    if argn < 2:
        print("No items added..")
        print("Usage: python3 ft_inventory_system.py <item1 name>: <item1 amount>...")
    else:
        print("=== Inventory System Analysis ===")
        inventory: dict[str, int] | None = create_dict(sys.argv)
        print(f"Got inventory: {inventory}")
        invlist: list[str] = list(inventory.keys())
        print(f"Item list: {invlist}")
        total_items: int = sum(inventory.values())
        print(f"Total quantity of the {len(inventory)} items: {total_items}")
        items_perc(inventory, total_items)
        mabund_item(inventory)
        labund_item(inventory)
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()