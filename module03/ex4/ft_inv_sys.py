import sys, 


def check_items(args: list[str]) -> bool:
    for arg in args:
        for i in arg:
            if i == ':':
                return True
    return False

def create_dict(args: list[str]) -> dict:
    inv: dict[str, int] = {}
    for arg in args:
        for i in range(len(arg)):
            if arg[i] == ":":
                name = arg[:i]
                value = arg[i+1]
        try:


def main() -> None:
    
