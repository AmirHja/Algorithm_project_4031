import timeit
import mmh3

def linear_search(username: str):
    start = timeit.default_timer()
    for record in DATABASE:
        value = record

        if value.strip() == username:
            return True, timeit.default_timer() - start
        
    return False, timeit.default_timer() - start

def hash_function(username: str, seed: int) -> int:
    return abs(mmh3.hash(username, seed) % BLOOM_FILTER_SIZE)

def bloom_filter(data: list):
    filter = [0 for _ in range(0, BLOOM_FILTER_SIZE)]

    for username in data:
        for seed in range(1, 7+1):
            filter[hash_function(username.strip(), seed)] = 1
    
    return filter
    
def hash_search(username: str):
    start = timeit.default_timer()
    for seed in range(1, 7+1):
        if BLOOM_FILTER[hash_function(username.strip(), seed)] == 0:
            return False, timeit.default_timer() - start
    return True, timeit.default_timer() - start

def binary_search(username: str):  # Amirreza Beik 40116103

    start = timeit.default_timer()
    end = None
    low = 0 
    high = DATABASE_SIZE

    while low <= high:
        mid = (low + high) // 2
        value = DATABASE[mid]

        if value.strip() == username:
            return True, timeit.default_timer() - start
        
        if value.strip() < username:
            low = mid + 1
            continue

        else:
            high = mid - 1
            continue
                
    return False, timeit.default_timer() - start


def get_all_searches(username: str):
    print("linear search:", linear_search(username))
    print("hash search:", hash_search(username))
    print("binary search:", binary_search(username))


PATH = "usernames.txt"
DATABASE = list(open(PATH, 'r'))
DATABASE_SIZE = len(DATABASE) - 1
BLOOM_FILTER_SIZE = 4_789_656
BLOOM_FILTER = bloom_filter(DATABASE)



get_all_searches(input("Enter a username: "))


