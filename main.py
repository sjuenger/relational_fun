from copy import deepcopy

def compute_attribute_shell(subset, fd_list):
    result = subset[:]
    changed = True
    while changed:
        changed = False
        for elem in fd_list:
            if all(x in result for x in elem[0]):
                for char in elem[1]:
                    if char not in result:
                        result.append(char)
                        changed = True

    return result


def compute_canonical_coverage(fd_list):
    print(fd_list)
    # Linksreduktion
    for i in range(len(fd_list)):
        elem = fd_list[i]
        if len(elem[0])>1:
            for attribute in elem[0]:
                new_alpha = [item for item in elem[0] if item not in attribute]
                tmp = compute_attribute_shell(new_alpha, fd_list)
                if all(x in tmp for x in elem[1]):
                    fd_list[i][0] = new_alpha
                    elem[0] = new_alpha
    print(fd_list)

    # Rechtsreduktion
    for i in range(len(fd_list)):
        elem = fd_list[i]
        for attribute in elem[1]:
            new_fd = deepcopy(fd_list)
            new_fd[i][1] = [item for item in elem[1] if item not in attribute]
            tmp = compute_attribute_shell(elem[0], new_fd)
            if attribute in tmp:
                fd_list[i][1] = new_fd[i][1]
                elem[1] = new_fd[i][1]

    # Entfernen
    # TODO
    # Zusammenfassen
    # TODO

    return fd_list

def extract_char(schema):
    s_start = schema.find('{')
    s_end = schema.find('}')
    attributes = schema[s_start + 1:s_end].split(', ')

    return attributes

def main():
    with open('input.txt', 'r') as data:

        tmp = data.readline()
        schema = tmp[:len(tmp)-1]
        attributes = extract_char(schema)

        print('Eingabe:')
        print(schema)

        fd_list = []
        line = data.readline()
        while len(line)>0:
            if '\n' == line[len(line) - 1]:
                line = line[:len(line) - 1]
            print(line)
            if '->' in line:
                line_list = line.split('->')
                tmp_1 = extract_char(line_list[0])
                tmp_2 = extract_char(line_list[1])
                tmp = [tmp_1, tmp_2]
                fd_list.append(tmp)
            line = data.readline()

        print('\n')

    tmp = compute_canonical_coverage(fd_list)
    # tmp = compute_attribute_shell(['A'], fd_list)
    print(tmp)


if __name__ == '__main__':
    main()
