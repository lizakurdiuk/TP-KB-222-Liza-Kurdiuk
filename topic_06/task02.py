filename = "_input06.txt"

try:
    with open(filename, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File '{filename}' not found. Creating a new file.")
    lines = []

for line in lines:
    name, score = line.strip().split(',')
    print(f'Name: {name}, Score: {score}')

sorted_by_name = sorted(lines, key=lambda x: x.strip().split(',')[0])
print("\nSort by name:")
for line in sorted_by_name:
    print(line)

sorted_by_score = sorted(lines, key=lambda x: int(x.strip().split(',')[1]))
print("\nSorting by score:")
for line in sorted_by_score:
    print(line)

with open("Sort_by_name.txt", "w") as name_file:
    name_file.writelines(sorted_by_name)

with open("Sorting_by_score.txt", "w") as score_file:
    score_file.writelines(sorted_by_score)

    
    