import random
from prob1 import *

if __name__=="__main__":
    lst = [random.randint(1, 100000) for _ in range(100)]
    print(lst)
    answer = sorted(lst)
    # my_ans = bubble_sort(lst)
    # my_ans = insertion_sort(lst)
    # my_ans = merge_sort(lst)
    # my_ans = quick_sort(lst)
    my_ans = radix_sort(lst, 6)
    print(f"{answer}\n{lst}")

    if answer == my_ans:
        print(f"correct")

    else:
        print("Wrong")