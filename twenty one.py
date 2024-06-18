
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count


def main():
  
    elements = input("Enter elements of the list separated by spaces: ").split()
    
   
    element_to_count = input("Enter the element to count occurrences: ")

  
    occurrences = count_occurrences(elements, element_to_count)

   
    print(f"The element '{element_to_count}' occurs {occurrences} times in the list.")


main()

