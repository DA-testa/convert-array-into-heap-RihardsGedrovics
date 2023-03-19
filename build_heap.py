def parse_input_user():
    n_var = int(input())
    data_var = list(map(int, input().strip().split(' ')))
    return n_var, data_var

def parse_input_file(file_name_var):
    file_var = open(file_name_var, "r", -1, "utf-8")
    n_var = int(file_var.readlinlke().strip())
    data_var = list(map(int, file_var.readline().strip().split(' ')))
    return n_var, data_var

def build_heap(data_var):
    n_var = len(data_var)
    swaps_var = []
    for i_var in range(n_var // 2, -1, -1):
        top_var = i_var
        while True:
            left_var = 2 * top_var + 1
            right_var = 2 * top_var + 2
            if left_var < n_var and data_var[left_var] < data_var[top_var]:
                top_var = left_var
            if right_var < n_var and data_var[right_var] < data_var[top_var]:
                top_var = right_var
            if i_var != top_var:
                data_var[i_var], data_var[top_var] = data_var[top_var], data_var[i_var]
                swaps_var.append((i_var, top_var))
                i_var = top_var
            else:
                break
    return swaps_var

def main():
    n_var = 0
    input_data_var = []
    try:
        key_var = input().strip()
        if (key_var.upper() == "I"):
            n_var, input_data_var = parse_input_user()
        elif (key_var.upper() == "F"):
            file_name_var = input().strip()
            if (file_name_var.lower() == "a"):
                pass
            n_var, input_data_var = parse_input_file("tests/" + file_name_var)
    except:
        pass
    assert len(input_data_var) == n_var
    swaps_var = build_heap(input_data_var)
    print(len(swaps_var))
    for i_var, j_var in swaps_var:
        print(i_var, j_var)

if __name__ == "__main__":
    main()
