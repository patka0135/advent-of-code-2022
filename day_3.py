def read_file(file: str):
    with open(file) as f:
        lines = f.readlines()

    lines = [x.replace("\n", "") for x in lines]

    return lines

class Rucksack():
    "This is a rucksack class"
    def __init__(self, items_inside: str):
        self.items_inside = items_inside
    
    def divide_compartments(self):
        stri_len = int(len(self.items_inside)/2)
        self.first_compartment = self.items_inside[:stri_len]
        self.second_compartment = self.items_inside[-stri_len:]
        return self

    def find_priority_item(self):
        self.priority_item = [item for item in list(self.first_compartment) if item in list(self.second_compartment)][0]
        return self

    def map_priority(self):
        if str.isupper(self.priority_item):
            self.priority = ord(self.priority_item) - 38
        else: 
            self.priority = ord(self.priority_item) - 96
        return self


def calculate_sum_priorities(input_file: str):
    file_content = read_file(input_file)
    class_list = [Rucksack(x) for x in file_content]
    compartments = [x.divide_compartments() for x in class_list]
    priority_items = [x.find_priority_item() for x in compartments]
    priorities = [x.map_priority().priority for x in priority_items]
    print(sum(priorities))
    return sum(priorities)

input_file = 'input_day_3.txt'
calculate_sum_priorities(input_file)