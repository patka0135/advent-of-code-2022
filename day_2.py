shape_dict = {
    'A': 1,
    'B': 2, 
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3}

def read_file(file: str):
    with open(file) as f:
        lines = f.readlines()

    lines = [x.replace("\n", "") for x in lines]

    return lines

def map_shape(shape: str):

    score_for_shape = shape_dict.get(shape)

    return score_for_shape

def score_line(line: str):
    score = 0
    other_shape, my_shape = [map_shape(x) for x in line if x != " " ]
    if my_shape > other_shape:
        if my_shape == 3 and other_shape == 1:
            score += 0
        else: 
            score += 6
    if my_shape < other_shape:
        if my_shape == 1 and other_shape == 3:
            score += 6
        else: 
            score += 0
    if my_shape == other_shape:
        score += 3

    score += my_shape 
    return score

def score_line_strategies(line: str):
    score = 0
    other_shape, my_shape = [map_shape(x) for x in line if x != " " ]
    if my_shape == 2:
        score += 3
        score += other_shape
    if my_shape == 1:
        score += 0
        if other_shape == 1: score += 3
        if other_shape == 2: score += 1
        if other_shape == 3: score += 2
    if my_shape == 3:
        score += 6
        if other_shape == 1: score += 2
        if other_shape == 2: score += 3
        if other_shape == 3: score += 1
        
    return score

file_content = read_file('input_day_2_test.txt')
file_scores = [score_line(x) for x in file_content]
assert(sum(file_scores) == 15)

file_scores_strategies = [score_line_strategies(x) for x in file_content]
assert(sum(file_scores_strategies) == 12)

file_content = read_file('input_day_2.txt')
file_scores = [score_line(x) for x in file_content]
print(file_scores)
print(sum(file_scores))

file_scores_strategies = [score_line_strategies(x) for x in file_content]
print(file_scores_strategies)
print(sum(file_scores_strategies))
