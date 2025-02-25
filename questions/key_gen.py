import json
import random
import os
import sys

def generate_random_questions(num_files, max_questions, output_dir, current_key_num):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(num_files):
        # num_questions = random.randint(1, max_questions)
        num_questions = max_questions
        questions = list(range(1, num_questions + 1))
        random.shuffle(questions)

        new_questions = [0]
        new_questions.extend(questions)
        
        data = {
            "questions": new_questions
        }
        
        file_path = os.path.join(output_dir, f"key_{current_key_num + i}.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
        print(f"Generated {file_path}")
        print(f"Questions: {data}")

# Parameters
num_files = 100  # Number of JSON files to generate
max_questions = 20  # Maximum number of questions in each file
output_dir = "."  # Directory to save the JSON files
current_key_num = 0  # Default starting key number

# Check for command-line argument
if len(sys.argv) > 1:
    try:
        current_key_num = int(sys.argv[1])
        num_files = 1
    except ValueError:
        print(f"Invalid argument {sys.argv[1]}, using default key number {current_key_num}")

generate_random_questions(num_files, max_questions, output_dir, current_key_num)

