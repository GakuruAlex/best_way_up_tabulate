from typing import List
def best_way(height: int, steps: List[int]) -> List[int]:
    """_Find the best way i.e shortest list steps up a stairs of given height_

    Args:
        height (int): _Number of stairs_
        steps (List[int]): _List of steps you can take at a time_

    Returns:
        List[int]: _List of steps up given stairs_
    """
    best_way_table: List[int] = [None for _ in range(height + 1)]
    
    return best_way_table[height]