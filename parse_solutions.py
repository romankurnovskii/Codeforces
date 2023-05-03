import os
import pathlib
import re
import requests
import datetime

def parse_solutions(root_path):
    contest_api_url = "https://codeforces.com/api/contest.list"

    # Fetch contest data from Codeforces API
    response = requests.get(contest_api_url)
    contests = response.json()["result"]

    # Create a mapping of contest id to start date
    contest_dates = {}
    for contest in contests:
        contest_id = contest["id"]
        start_time = contest["startTimeSeconds"]
        start_date = datetime.datetime.fromtimestamp(start_time).date()
        contest_dates[str(contest_id)] = start_date

    for root, _, files in os.walk(root_path):
        problem_files = sorted([f for f in files if f.endswith(".py")])
        if len(problem_files) == 0:
            continue

        problem_folder = os.path.basename(root)
        output_file = os.path.join("docs", "problems", f"{problem_folder}.md")

        # add description for whole page if exists
        description_file = os.path.join(root, "description.md")
        description = ""
        if os.path.exists(description_file):
            with open(description_file, "r") as desc_f:
                description = desc_f.read()

        with open(output_file, "w") as f:
            # Add date meta tag if contest start date is available
            if problem_folder in contest_dates:
                f.write(f"---\ndate: {contest_dates[problem_folder]}\n---\n\n")

            f.write(f"# {problem_folder}\n\n")
            f.write(f"{description}\n\n")

            for file in problem_files:
                problem_name = pathlib.Path(file).stem

                match = re.match(r"_([A-Za-z]+)", problem_name)
                if match:
                    problem_number, letter = match.groups()
                    problem_link = f"https://codeforces.com/problemset/problem/{problem_number}/{letter}"
                else:
                    problem_link = ""

                f.write(f"## [{problem_name}]({problem_link})\n\n")

                description_file = os.path.join(root, f"{problem_name}.md")
                if os.path.exists(description_file):
                    with open(description_file, "r") as desc_f:
                        explanation = desc_f.read()
                    f.write("### Explanation\n\n")
                    f.write(f"{explanation}\n\n")

                file_path = os.path.join(root, file)
                with open(file_path, "r") as code_f:
                    code = code_f.read()

                f.write('```python\n')
                f.write(code)
                f.write('\n```\n')


if __name__ == "__main__":
    solutions_dir = "solutions"
    docs_problems_dir = "docs/problems"

    if not os.path.exists(docs_problems_dir):
        os.makedirs(docs_problems_dir)

    parse_solutions(solutions_dir)
