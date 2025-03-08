# # from collections import deque
# # # Problem 1: Manage Performance Stage Changes
# # # At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

# # # You are given a list changes of strings where each string represents a change action. The actions can be:

# # # "Schedule X": Schedule a performance with ID X on the stage.
# # # "Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
# # # "Reschedule": Reschedule the most recently canceled performance to be the next on stage.
# # # Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.

# # # def manage_stage_changes(changes):
# # #     # stage stack to track what is scheduled
# # #     # cancel stack to track what was canceled (top should be most recent)
    
# # #     # loop go to through all changes
# # #         # list = handle the split (str.split() -> [])
# # #         # logic based on 3 operations list[0]
# # #             # schedule and the len(split arr) is >1
# # #                 # take 2nd of the split output array
# # #                 # append to stage stack
# # #             # cancel
# # #                 # pop from stage stack
# # #                 # add that to canceled stack
# # #             # resched
# # #                 # pop from canceled stack
# # #                 # add that to stage
    
# # #     # return stage stack

# # #     if not changes:
# # #         return []
    
# # #     stage = []
# # #     canceled = []
    
# # #     for x in changes:
# # #         temp_list = x.split()
# # #         if temp_list[0] == "Schedule" and len(temp_list) > 1:
# # #             stage.append(temp_list[1])
# # #         elif temp_list[0] == "Cancel":
# # #             temp = stage.pop()
# # #             canceled.append(temp)
# # #         elif temp_list[0] == "Reschedule":
# # #             temp = canceled.pop()
# # #             stage.append(temp)
            
# # #     return stage
            

# # # print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# # # print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# # # print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

# # # Problem 2: Queue of Performance Requests
# # # You are organizing a festival and want to manage the queue of requests to perform. Each request has a priority. Use a queue to process the performance requests in the order they arrive but ensure that requests with higher priorities are processed before those with lower priorities. Return the order in which performances are processed.

# # def process_performance_requests(requests):
    



# # print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# # print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# # print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
# # # Example Output:

# # # ['Music', 'Dance', 'Drama']
# # # ['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
# # # ['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']


# # Problem 1: Manage Performance Stage Changes
# # At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

# # You are given a list changes of strings where each string represents a change action. The actions can be:

# # "Schedule X": Schedule a performance with ID X on the stage.
# # "Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
# # "Reschedule": Reschedule the most recently canceled performance to be the next on stage.
# # Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.

# # def manage_stage_changes(changes):
# #     # stage stack to track what is scheduled
# #     # cancel stack to track what was canceled (top should be most recent)
    
# #     # loop go to through all changes
# #         # list = handle the split (str.split() -> [])
# #         # logic based on 3 operations list[0]
# #             # schedule and the len(split arr) is >1
# #                 # take 2nd of the split output array
# #                 # append to stage stack
# #             # cancel
# #                 # pop from stage stack
# #                 # add that to canceled stack
# #             # resched
# #                 # pop from canceled stack
# #                 # add that to stage
    
# #     # return stage stack

# #     if not changes:
# #         return []
    
# #     stage = []
# #     canceled = []
    
# #     for x in changes:
# #         temp_list = x.split()
# #         if temp_list[0] == "Schedule" and len(temp_list) > 1:
# #             stage.append(temp_list[1])
# #         elif temp_list[0] == "Cancel":
# #             temp = stage.pop()
# #             canceled.append(temp)
# #         elif temp_list[0] == "Reschedule":
# #             temp = canceled.pop()
# #             stage.append(temp)
            
# #     return stage
            

# # print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# # print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# # print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

# # Problem 2: Queue of Performance Requests
# # You are organizing a festival and want to manage the queue of requests to perform. Each request has a priority. Use a queue to process the performance requests in the order they arrive but ensure that requests with higher priorities are processed before those with lower priorities. Return the order in which performances are processed.

# from collections import deque 
# def process_performance_requests(requests):
#     requests.sort(reverse=True)
#     return [element[1] for element in requests]


# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
# # Example Output:

# # ['Music', 'Dance', 'Drama']
# # ['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
# # ['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']

# # USING HEAP

# import heapq

# def process_performance_requests(requests):
#     # Max-heap by negating priorities
#     heap = [(-priority, performance) for priority, performance in requests]
#     heapq.heapify(heap)

#     # Extract performances in priority order
#     result = [heapq.heappop(heap)[1] for _ in range(len(heap))]
#     return result

# # Example Usage
# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))



