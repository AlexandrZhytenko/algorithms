# to find persons name with ending m

from collections import deque

graph = {}
# my friends
graph["you"] = ["alice", "bob", "claire"]
# my friends friends
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = deque()
search_queue += graph["you"]

def person_with_name_end_m(name, letter):
    return name[-1] == letter

def find_person_with_name_end(search_queue, graph, letter="m"):
    searched = []
    print "search_queue =>", search_queue
    while search_queue:
        person = search_queue.popleft()
        print "person =>", person
        if not person in searched:
            if person_with_name_end_m(person, letter):
                print person + " has name with ending {}".format(letter)
                return True
            else:
                search_queue += graph[person]
                print search_queue
                searched.append(person)
                print "searched", searched
    return False

print find_person_with_name_end(search_queue, graph)