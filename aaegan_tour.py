data_list = []

from itertools import combinations

def customer_satisfying_itinerary(data_list):

    if len(data_list) < 2:
        print("NO ITINERARY")
        return
    hop = int(data_list[0])
    customer_count = int(data_list[1])
    customer_preference_lines = data_list[2:2+customer_count]
    customers = []
    for preference in customer_preference_lines:
        preference_pairs = preference.split(", ")
        choices = []
        for i in preference_pairs:
            temp = i.split(" ")
            hop_no = int(temp[0])
            transport = temp[1]
            if "airborne" in transport:
                choices.append((hop_no, True))
            else:
                choices.append((hop_no, False))
        customers.append(choices)

    #evalution starts to find minimal airborne combinations
    for airborne in range(hop + 1):
        for airborne_hops in combinations(range(hop), airborne):
            # considering itirnerary with maximum by-sea
            itinerary = [False] * hop
            for idx in airborne_hops:
                itinerary[idx] = True

            # Check satisfaction of each customer
            satisfied = True
            for prefs in customers:
                prefs_satisfied = False
                for h, t in prefs:
                    if itinerary[h] == t:
                        prefs_satisfied = True
                        break
                if not prefs_satisfied:
                    satisfied = False
                    break

            if satisfied:
                output = []
                for i in range(hop):
                    if itinerary[i]:
                        mode = "airborne"
                    else:
                        mode = "by-sea"
                    output.append(f"{i} {mode}")
                print(", ".join(output))
                return

    print("NO ITINERARY")


try:
    with open("data.txt", "r") as file:
        for line in file:
            if line.strip():
                data_list.append(line.strip())
        customer_satisfying_itinerary(data_list)
except FileNotFoundError:
    print("File not found")