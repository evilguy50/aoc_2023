import regex as re
import wordnum

with open("./input.txt", "r") as file:
    lines = file.read().splitlines()

result = 0
for line in lines:
    matches = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
    newMatches = []
    for match in matches:
        newMatches.append(wordnum.replace_words_with_numbers(match))
    match_count = len(matches)
    if match_count < 1:
        continue
    first_num = newMatches[0]
    results = newMatches[0] + newMatches[0]
    if match_count > 1:
        last_num = newMatches[matches.__len__() - 1]
        results = first_num + last_num
    result += int(results)

print(result)