import pygame
import random
import sys
import time

pygame.init()

# Colors for drawings
BACKGROUND = '0xfa4454'
BARS = '0x364966'
GREEN = '0x00ff00'
RED = '0xff0000'

# The height and width of the screen.
SCREEN_SIZE = WIDTH, HEIGHT = 600, 600

# Setting the display size to WIDTH | HEIGHT.
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

# Works with the pygame clock object to control algo speed
SPEED = 120

# A list of unsorted numbers from 1 to 600.
def randomize():
    return random.sample(range(HEIGHT), HEIGHT)

nums = randomize()

# Checks whether the user is trying to quit the program.
# This needs to be active during AND after sorting.
def kill_check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit(0)


# Draws all bars to the screen from the nums array.
# This needs to run inside each sorting algorithm
# during exuction to show progress of sort.
def draw_bars(nums, swap1=None, swap2=None):
    SCREEN.fill(BACKGROUND)
    for i, e in enumerate(nums):
        color = BARS
        if swap1 == e:
            color = GREEN
        elif swap2 == e:
            color = RED
        pygame.draw.rect(SCREEN, color, (i, HEIGHT-e, 1, e))
        kill_check()
    pygame.display.update()


#---------------------------------------------
#           SORTING ALGORITHMS
#---------------------------------------------

def bubble_sort(nums):
    """
    The Bubble Sort Algorithm.

    Bubble sort works by running through the length of the list and checking if the current index value
    is less than the next index value. If it is, swap them and continue. After each iteration
    the (n - i)th index, where n is the length of the list and i is the current number of iterations,
    can be removed from the search since it is guaranteed to be the biggest number. Continue
    until the list is sorted.
    """

    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        clock.tick(SPEED)
        draw_bars(nums, nums[j], nums[j+1])


def selection_sort(nums):
    """
    The Selection Sort Algorithm.

    Selection sort is basically a minimum value search that swaps the found minimum value with the 
    ith value in the list, where i is the current number of iterations. Because selection sort finds
    the smallest value each iteration you know the values at the beginning of the list are sorted
    from least to greatest and no longer need to be iterated through.
    """

    for i in range(len(nums)):
        min = i
        for j in range(i+1, len(nums)):
            if nums[min] > nums[j]:
                min = j

        nums[i], nums[min] = nums[min], nums[i]
        clock.tick(SPEED)
        draw_bars(nums, nums[i], nums[min])


def insertion_sort(nums):
    """
    The Insertion Sort Algorithm. 

    Insertion sort works by iterating through the list until an unsorted value is found. It determines that
    the value is unsorted by comparing its value to the previous value. Once an unsorted value is found
    we keep track of that value in a temporary variable and iterate backwards while comparing and swapping
    forward already sorted values until we find a sorted position for the temporary value and place it there.
    We know the value is sorted when its value is no longer lower than the previous value in the list.
    """

    for i in range(1, len(nums)):
        temp = nums[i]
        
        j = i-1
        while temp < nums[j] and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp
        clock.tick(SPEED)
        draw_bars(nums, temp, nums[i])


def merge_sort(n):
    """
    The Merge Sort Algorithm.

    This merge sort solution uses recursion to break down the input list by reducing it into smaller and smaller 
    sub-lists. Once the sub-lists contain only single values from the original list the merge function 
    sorts and combines the smaller sub-lists, working backwards up the recursion tree until a single, sorted
    list remains. 
    """

    start, end = 1, len(n)

    if start < end:
        middle = start + (end - start)//2
        left = merge_sort(n[:middle])
        right = merge_sort(n[middle:])

    else:
        return n
    
    return merge(left, right)


def merge(left, right):
    ret_list = []
    i, j = 0, 0
    offset = nums.index(left[0])

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ret_list.append(left[i])
            nums[offset] = left[i]
            offset += 1
            i += 1
        else:
            ret_list.append(right[j])
            nums[offset] = right[j]
            offset += 1
            j += 1
        draw_bars(nums, left[i-1], right[j-1])

    ret_list += left[i:]
    ret_list += right[j:]

    nums[offset:offset+len(left[i:])] = left[i:]
    nums[offset:offset+len(right[j:])] = right[j:]

    draw_bars(nums)

    return ret_list
         

def main():
    # I know it's heresy to use global variables... I KNOW.
    # ... But it was the simplest way to get this working.
    global nums

    algos = {'Bubble Sort': bubble_sort, 'Selection Sort': selection_sort, 'Insertion Sort': insertion_sort, 'Merge Sort': merge_sort}
    
    for name, func in algos.items():
        pygame.display.set_caption(name)
        nums = randomize()
        draw_bars(nums)
        time.sleep(2)
        func(nums)
        time.sleep(2)


if __name__ == "__main__":
    main()