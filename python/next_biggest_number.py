#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    
    # create a list of ints for digits 
    digits = [int(d) for d in str(num)]

    # reverse the digits in the list 
    digits_reverse = digits[::-1]
    
    
    # Set up cases to check
    # length is 0
    if len(digits_reverse) == 0:
        return -1

    # length is 1    
    if len(digits_reverse) == 1:
        return -1

    # if length is 2
    if len(digits_reverse) == 2:
        if digits_reverse < digits:
            return -1
    
        else:
            digits_int_to_str = [str(i) for i in digits_reverse]
            result = int("".join(digits_int_to_str))
            return result
            

    # if all sorted of any length
    if digits_reverse == sorted(digits_reverse):
        return -1
        
    # Find the descending number after traversing in reverse
    for (ind,(i,j)) in enumerate(zip(digits_reverse,digits_reverse[1:])):
        if i > j:
            descend_num=j
            descend_index = ind+1
            break
            
    # Split digits using descend position         
    left_side =  digits_reverse[descend_index:]
    right_side = digits_reverse[0:descend_index]
    
    
    # Find the number on the right side that is next greater 
    # than the descending num

    # if length is 1
    if len(right_side)==1:
        min_right = right_side[0]
        
    # if length is greater than 1
    elif len(right_side)>1: 
        # Using min() + generator expression 
        min_right = min(i for i in right_side if i > descend_num)
    
    # Find the index position of the descending num
    desc_index = left_side.index(descend_num)
    
    # Find the index position of the min num on the right greater than descend num
    min_right_index = right_side.index(min_right) 

    # swap values between the 2 lists
    left_side[desc_index] = min_right
    right_side[min_right_index] = descend_num
    
    # Reverse the left side
    left_side.reverse()
    
    # Join the two sides
    answer = left_side + right_side
    
    # Convert to string and then to integer to express number
    digits_int_to_str = [str(i) for i in answer]
    result = int("".join(digits_int_to_str))
    
    return result

if __name__ == "__main__":
    main()

