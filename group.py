#Task 1

#function groups_of_3() will take one parameter of list[int]. It will
#group the elements of the input list into groups of 3 values
#(consecutively). It will return a list of type list[list[int]] where
#each sublist (excluding, perhaps, the last) is a group of three values.

def groups_of_3(num_list: list[int])->list[list[int]]:
    new_list = [num_list[i:i+3] for i in range(0, len(num_list), 3)]
    return new_list


