import pygame
import random
import sys
import time

pygame.init()

clock = pygame.time.Clock()

# Colors for drawings
BACKGROUND = '0xfa4454'
BARS = '0x364966'
GREEN = '0x00ff00'
RED = '0xff0000'

# The height and width of the screen.
SCREEN_SIZE = WIDTH, HEIGHT = 600, 600

# Setting the display size to WIDTH | HEIGHT.
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

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
        clock.tick(120)
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
        clock.tick(120)
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
        clock.tick(120)
        draw_bars(nums, temp, nums[i])
         

def main(nums):

    algos = {'Bubble Sort': bubble_sort, 'Selection Sort': selection_sort, 'Insertion Sort': insertion_sort}
    
    for name, func in algos.items():
        pygame.display.set_caption(name)
        nums = randomize()
        draw_bars(nums)
        time.sleep(2)
        func(nums)
        time.sleep(2)


if __name__ == "__main__":
    main(nums)