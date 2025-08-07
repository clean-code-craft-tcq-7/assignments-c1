import re
import pandas as pd

# Pattern: Name (DEPT)
participant_pattern = re.compile(r'^[A-Za-z ]+ \([A-Z/0-9\-]+\)$')


def split_transcript(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]

    groups = []
    current_group = []

    for line in lines:
        if participant_pattern.match(line):
            if current_group:
                groups.append(current_group)
            current_group = [line]
        else:
            if current_group:
                current_group.append(line)
    if current_group:
        groups.append(current_group)

    return groups


def get_last_name_and_dept(group):
    name_dept = None
    for line in group:
        match = participant_pattern.match(line)
        if match:
            name_dept = match.group(0)
    return name_dept


def get_github_link(group):
    for line in group:
        if 'github.com' in line:
            match = re.search(r'(https://github\.com[^\s]+)', line)
            if match:
                return match.group(1)


def groups_to_excel(groups, filename):
    all_data = []
    for group in groups:
        name_dept = get_last_name_and_dept(group)
        github_link = get_github_link(group)
        if name_dept and github_link:
            all_data.append({
                'Name': name_dept,
                'GitHub Link': github_link
            })

    df = pd.DataFrame(all_data)
    df.to_excel(filename, index=False)


if __name__ == "__main__":
    chats = split_transcript('b3_participants.txt')
    groups_to_excel(chats, 'participants.xlsx')
