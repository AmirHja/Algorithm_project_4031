import timeit

def linear_search(username: str):
    start = timeit.default_timer()
    for record in DATABASE:
        value = record

        if value.strip() == username:
            return True, timeit.default_timer() - start
        
    return False, timeit.default_timer() - start




def get_all_searches(username: str):
    print("linear search:", linear_search(username))

PATH = "usernames.txt"
DATABASE = list(open(PATH, 'r'))
DATABASE_SIZE = len(DATABASE) - 1


get_all_searches(input("Enter a username: "))


