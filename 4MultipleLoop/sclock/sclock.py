def input():
    return int(raw_input())


def main(n):
    def print_triangle(is_top):
        if is_top:
            space_range = range(0, n // 2 + 1)
        else:
            space_range = range(n // 2 - 1, -1, -1)

        for space in space_range:
            count_asterisks = n - 2 * space - 1

            line = ''
            for i in range(space):
                line += ' '
            
            if not is_top:
                line += '$'
            for i in range(count_asterisks):
                line += '*'
            if is_top:
                line += '$'
            print line
    print_triangle(True)
    print_triangle(False)
    # for space in range(0, n // 2 + 1):
    #     line = ''
    #     for i in range(space):
    #         line += ' '
    #     for i in range(n - 1 - (space * 2)):
    #         line += '*'
    #     line += '$'
    #     print line
    # for space in range(n // 2 - 1, -1, -1):
    #     line = ''
    #     for i in range(space):
    #         line += ' '
    #     line += '$'
    #     for i in range(0, 2 * (n // 2 - space), 1):
    #         line += '*'
    #     print line


n = input()
main(n)
