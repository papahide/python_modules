import sys


def ft_check_item_amount(amount: str) -> int | None:
    try:
        qtity = int(amount)
        return qtity
    except ValueError as err:
        print(f"Error: {err}")
        print("Item amount has to be int")


def ft_add_items(itemstr: list[str], item_nbr: int, inventory: dict[str, int]) -> None:
    for item in itemstr:
        pos = 0
        for char in item:
            if char == ':':
                break
            pos += 1
        item_name = item[:pos]
        item_amount = ft_check_item_amount(item[pos+1:])
        if item_amount is not None:
            inventory.update({item_name: item_amount})


def ft_display_items(inventory: dict[str, int], total_items: int) -> None:
    for item, amount in inventory.items():
        percentage = (amount / total_items) * 100
        print(f"{item}: {amount} units ({percentage:.1f}%)")


def ft_display_exremes(inv: dict[str, int]) -> None:
    abund = max(inv.values())
    for i in range(2):
        for name, qty in inv.items():
            if qty == abund:
                print(f"Most abundant: {name} ({qty} units)")
                break
        abund = min(inv.values())
        i += 1


def ft_create_categories(categories: dict[str, dict[str, int]],
                         inv: dict[str, int]) -> None:
    for item, qty in inv.items():
        if qty > 3:
            categories["Moderate"].update({item: qty})
        else:
            categories["Scarce"].update({item: qty})


def ft_create_restock(restock: list[str], inv: dict[str, int]) -> None:
    for item, qty in inv.items():
        if qty <= 1:
            restock.append(item)


def main() -> None:
    argn = len(sys.argv)
    if argn < 2:
        print("No items added..")
        print("Usage: python3 ft_inventory_system.py <item1 name>: <item1 amount>...")
    else:
        print("=== Inventory System Analysis ===")

        inventory: dict[str, int] = {}
        ft_add_items(sys.argv[1:], argn, inventory)

        total_items = sum(inventory.values())
        print(f"Total items in inventory: {total_items}")

        unique = len(inventory)
        print(f"Unique item types: {unique}")

        print("\n=== Current Inventory ===")
        ft_display_items(inventory, total_items)

        print("\n=== Inventory Statistics ===")
        ft_display_exremes(inventory)

        print("\n=== Item Categories ===")
        categories: dict[str, dict[str, int]] = {"Moderate": {}, "Scarce": {}}
        ft_create_categories(categories, inventory)
        print(f"Moderate: {categories['Moderate']}")
        print(f"Scarce: {categories['Scarce']}")

        print("\n=== Management Suggestions ===")
        restock: list[str] = []
        ft_create_restock(restock, inventory)
        print(f"Restock needed: {", ".join(restock)}")

        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {", ".join(inventory.keys())}")
        print(f"Dictionary values: {", ".join(map(str, inventory.values()))}")
        print(f"Sample lookup - 'sword' in inventory: {"sword" in inventory}")
    


if __name__ == "__main__":
    main()