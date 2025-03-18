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
    best_way_table[0] = []
    for index in range(height):
        if best_way_table[index] != None:
            for step in steps:
                if step + index < len(best_way_table):
                    current_best: List[int] = best_way_table[index][:]
                    current_best.append(step)
                    if best_way_table[index + step] == None or len(best_way_table[index + step]) > len(current_best):
                        best_way_table[index + step] = current_best
    return best_way_table[height]

def main()-> None:
    steps: List[int] = [1, 2]
    height: int = 5
    best: List[int] = best_way(steps= steps, height= height)
    print(f"Best eay up {height} stairs is {best}")

if __name__ =="__main__":
    main()