states_needed = set(["mt", "wa", "or", "id", "nv", "ut",\
                     "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()
print "stations.items() =>", stations.items()

i = 1
while states_needed:
    best_station = None
    print "loop => {}".format(i)
    states_covered = set()
    print "states_covered =>", states_covered
    for station, states in stations.items():
        covered = states_needed & states
        print "covered =>", covered
        if len(covered) > len(states_covered):
            best_station = station
            print "best_station =>", best_station
            states_covered = covered
    i += 1
    states_needed -= states_covered
    print "states_needed =>", states_needed
    final_stations.add(best_station)

print final_stations




