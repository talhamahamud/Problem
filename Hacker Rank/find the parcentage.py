if __name__ == '__main__':
    n = int(input('how many student; '))
    student_marks = {}
    for _ in range(n):
        name, *line = input('name and marks: ').split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input('whos; ')
    expected_list=student_marks[query_name]
    n=0
    for i in expected_list:
        n=n+i
    division=n/len(expected_list)
    print(division)
    
