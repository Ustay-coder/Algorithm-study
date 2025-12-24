import argparse
import os
import sys

def create_problem_directory(title):
    try:
        # Create main directory
        os.makedirs(title, exist_ok=False)
        print(f"Directory '{title}' created.")

        # Create inputs directory
        os.makedirs(os.path.join(title, "inputs"), exist_ok=True)
        print(f"Directory '{title}/inputs' created.")

        # Create main.py
        main_py_path = os.path.join(title, "main.py")
        with open(main_py_path, "w") as f:
            f.write("import sys\n\n\ndef solve():\n    pass\n\n\nif __name__ == \"__main__\":\n    solve()\n")
        print(f"File '{title}/main.py' created.")

        # Create README.md
        readme_path = os.path.join(title, "README.md")
        problem_id = os.path.basename(title)
        readme_content = f"""# [Problem Title]
[Problem Name]

## Source
[Link](https://www.acmicpc.net/problem/{problem_id})

## Description
[Description]

## Input

[Input Description]

```bash
[Input Example]
```

## Output
(Output format)
[Output Description]
```bash
[Output Example]
```
"""
        with open(readme_path, "w") as f:
            f.write(readme_content)
        print(f"File '{title}/README.md' created.")

    except FileExistsError:
        print(f"Error: Directory '{title}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Project Utils CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new problem directory")
    create_parser.add_argument("--title", required=True, help="Title of the problem/directory")

    args = parser.parse_args()

    if args.command == "create":
        create_problem_directory(args.title)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
