input_list = []


def coins(input_list):
    for i in input_list:
        if i == input_list[-1]:
            return i
        elif i % 2 == 0:
            print 'No Solution!'
        else:
            print i-1
    return i


input_list.append(int(raw_input()))
while input_list[-1] != 0:
    input_list.append(int(raw_input()))

#input_list = [int(i) for i in raw_input().split(' ')]
coins(input_list)
