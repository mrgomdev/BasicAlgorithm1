def ants(length, number_ants, ants_list):
    for i in ants_list:
        if i * 2 < length:
            shortest_distance.append(i)
        else:
            shortest_distance.append(length - i)
    shortest_distance.sort()
    print shortest_distance[-1],

    for i in ants_list:
        if i * 2 < length:
            longest_distance.append(length - i)
        else:
            longest_distance.append(i)
    longest_distance.sort()
    print longest_distance[-1]
    return shortest_distance, longest_distance


input_list = []
input_list = [int(i) for i in raw_input().split(' ')]
length = input_list[0]
number_ants = input_list[1]
ants_list = []
ants_list = [int(i) for i in raw_input().split(' ')]
shortest_distance = []
longest_distance = []
ants(length, number_ants, ants_list)
