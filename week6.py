class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, current.artist)
        current = current.next
    print()

def get_artist_frequency(playlist):
    dict = {}
    current = playlist
    while current:
        if current.artist not in dict:
            dict[current.artist] = 1
        else:
            dict[current.artist] +=1
        current = current.next

    return dict
    
    
playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))

# # # class SongNode:
# # # 	def __init__(self, song, artist, next=None):
# # #         self.song = song
# # #         self.artist = artist
# # #         self.next = next

# # # # For testing
# # # def print_linked_list(node):
# # #     current = node
# # #     while current:
# # #         print(current.song, current.artist)
# # #         current = current.next
# # #     print()

# # # def get_artist_frequency(playlist):
# # #     dict = {}
# # #     current = playlist
# # #     while current:
# # #         if current.artist not in dict:
# # #             dict[current.artist] = 1
# # #         else:
# # #             dict[current.artist] +=1
# # #         current = current.next

# # #     return dict
    
    
# # # playlist = SongNode("Saturn", "SZA", 
# # #                 SongNode("Who", "Jimin", 
# # #                         SongNode("Espresso", "Sabrina Carpenter", 
# # #                                 SongNode("Snooze", "SZA"))))

# # # get_artist_frequency(playlist)



# # class SongNode:
# #     def __init__(self, song, artist, next=None):
# #         self.song = song
# #         self.artist = artist
# #         self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist))
        current = current.next
    print()


# # # Function with a bug!
# # def remove_song(playlist_head, song):
# #     if not playlist_head:
# #         return None
# #     if playlist_head.song == song:
# #         return playlist_head.next

# #     current = playlist_head
# #     while current.next:
# #         if current.next.song == song:
# #             current.next = current.next.next  
# #             return playlist_head 
# #         current = current.next

# #     return playlist_head

# # playlist = SongNode("SOS", "ABBA", 
# #                 SongNode("Simple Twist of Fate", "Bob Dylan",
# #                     SongNode("Dreams", "Fleetwood Mac",
# #                         SongNode("Lovely Day", "Bill Withers"))))

# # print_linked_list(remove_song(playlist, "Lovely Day"))


class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# def on_repeat(playlist_head):
#     fast = playlist_head
#     slow = playlist_head
#     while fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True
#     return False
    
# song1 = SongNode("GO!", "Common")
# song2 = SongNode("N95", "Kendrick Lamar")
# song3 = SongNode("WIN", "Jay Rock")
# song4 = SongNode("ATM", "J. Cole")
# song5 =  SongNode("nosnfosn", "J. Cole")
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(on_repeat(song1))

# O(n^2) might be cuz what if loop is big circle (end.next = beginning)
def loop_length(playlist_head):
    fast = playlist_head
    slow = playlist_head
    count = 0
    startNode = playlist_head
    ifStart = False
    while fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast and ifStart is False:
            startNode = fast
            ifStart = True
            count += 1
        elif startNode == slow:
            return count
        elif ifStart is True:
            count += 1
    return 0
        
song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song5 =  SongNode("nosnfosn", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))
            