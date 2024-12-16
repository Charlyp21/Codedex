likedsongs = {
    'House of gold':'Twenty one pilots',
    'Sharks':'Imagine dragons',
    'MAMA':'My chemical romance',
    'I wanna be your slave':'maneskin',
    'knee socks':'Artick monkeys'
}

file = open('favsongs.txt', 'w')

def write_liked_songs_to_file(liked_songs, file_name):
    file.write('Your liked songs:\n')
    for x,y in liked_songs.items():
        file.write(f'{x} by {y} \n')
    file.close

write_liked_songs_to_file(likedsongs, 'liked songs.txt')