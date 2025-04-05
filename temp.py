
# """
# - Given a list of songs, find thes song with target 'length'
# - Binary search - 
# - length of list / 2 = middle
# - middle > length
# - middle < length
# - middle == length

# - list is length 0 - return -1
# - if target length is negative, return -1 

# """

# def find_perfect_song(playlist, length):
# 	#edge cases
#     if len(playlist) == 0 or length < 0:
#         return -1
    
#     lenPlaylist = len(playlist)

#     left = 0
#     right = len(playlist)-1

#     while left <= right:

#         middle = (left+right) // 2

#         if playlist[middle] < length:
#             #go to the right
#             left = middle
#             left += 1


#         elif playlist[middle] > length:
#             #go to the left
#             right = middle
#             right -= 1


#         elif playlist[middle] == length: #playlist[middle] == length
#             return middle
        
#         #update left and right
    
#     return -1

# # 
# # print(find_perfect_song([101, 102, 103, 104, 105], 103))
# print(find_perfect_song([201, 202, 203, 204, 205], 206))

'''
Given:
sorted lis int (tour_dates)
int (available)

Find:
function can_attend() 
return true if attendable
false otherwise
O(log n)

PLAN
use indices to slice the list 
recreate list to to recurse function

'''

def can_attend(tour_dates, available):
    earlier = 0
    later = len(tour_dates) - 1
    middle =  (earlier + later) // 2

    if (len(tour_dates) == 1) and (tour_dates[0] != available):
        return False

    if tour_dates[middle] < available:
        new_dates = tour_dates[(middle+1):(later+1)]

    elif tour_dates[middle] > available:
        new_dates = tour_dates[earlier:middle]

    else:
        return True     

    return can_attend(new_dates, available)



print(can_attend([1, 3, 7, 10, 12], 12))
print(can_attend([1, 3, 7, 10, 12], 5))

def my_sqrt(x):
    pass

# Test cases
print(my_sqrt(4))   # 2
print(my_sqrt(8))   # 2
print(my_sqrt(16))  # 4
print(my_sqrt(1))   # 1
print(my_sqrt(0))   # 0
print(my_sqrt(27))  # 5



