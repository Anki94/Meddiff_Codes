def group_by_owners(my_file):
    dict = {}
    for file_name, owner_name in my_file.items():  
        dict[owner_name] = dict.get(owner_name, []) + [file_name]  
    return dict

my_file = {
    'Input.txt': 'India',
    'Code.py': 'Karnataka',
    'Output.txt': 'India'
}

print(group_by_owners(my_file))
