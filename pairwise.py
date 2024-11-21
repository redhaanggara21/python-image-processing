from itertools import pairwise

def main():
    lst = [1,2,3,4,5]
    print("Original list - ", lst)
    print("Successive overlapping pairs - ", list(pairwise(lst)))

    string = "hello educative"
    print("Successive overlapping pairs of characters in a string- ", list(pairwise(string)))
    
if __name__ == "__main__":
    main()