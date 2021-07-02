from typing import List


def slice_less(my_list:List[int], lesser: int) -> List[int]:
    new_my_list = sorted((char for char in my_list if char > lesser), reverse=True)
    print(new_my_list)

if __name__ == "__main__":
    slice_less([45,65,78,96,74,22,32], 55)