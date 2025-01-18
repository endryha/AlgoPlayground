def print_2d_array(arr):
    for row in arr:
        print(" ".join(f"{n:2}" if n != -1 else " _" for n in row))