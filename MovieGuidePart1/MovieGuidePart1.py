# Allyson Speagle CIS261 MovieGuidePart1

def command_menu():
    print('COMMAND MENU')
    print('list - List all movies')
    print('add - Add a movie')
    print('del - Delete a movie')
    print('exit - Exit program')
    print('\n')

movie_list = ["Howl's Moving Castle","Spirited Away","The Cat Returns"]
def list(movie_list):
    if len(movie_list) == 0:
        print('There are no movies in the list.\n')
        return
    else:
        i=1
        for movie in movie_list:
            print(str(i) + ". " +movie )
            i+=1
    print('\n')

def add(movie_list):
    name = input('Name: ')
    movie_list.append(name)
    print(name + ' was added.\n')

def delete(movie_list):
    movie_number = int(input('Number: ')) - 1
    if movie_number < 0 or movie_number > len(movie_list):
        print('Invalid movie number.\n')
    else: 
        rem_movie = movie_list[movie_number]
        movie = movie_list.remove(rem_movie)
        print(rem_movie + ' was deleted.\n')

print('The Movie List Program\n')
command_menu()
while True:
    command = input('Command: ')
    if command == 'list':
        list(movie_list)
    elif command == 'add':
        add(movie_list)
    elif command == 'del':
        delete(movie_list)
    elif command == 'exit':
        break
    else:
        print('Not a valid command. Please try again.\n')
print('Bye!')