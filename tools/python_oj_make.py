import os
import json
import hashlib
from typing import List, Dict

def generate_uid(inputs: List[str], outputs: List[str]) -> str:
    """
    Generate a unique ID based on the hash of input and output content
    
    Args:
        inputs: List of input strings
        outputs: List of output strings
        
    Returns:
        str: Hexadecimal hash string serving as UID
    """
    combined = "".join(inputs) + "".join(outputs)
    return hashlib.md5(combined.encode()).hexdigest()

def get_user_input(prompt: str) -> str:
    """
    Get user input with custom prompt
    
    Args:
        prompt: The prompt to display
        
    Returns:
        str: User input with leading/trailing whitespace removed
    """
    return input(prompt).strip()

def collect_test_case(reference_solution: str) -> Dict:
    """
    Collect a single test case from user input
    
    Args:
        reference_solution: Path to the reference solution script
        
    Returns:
        dict: Test case dictionary with uid, i, o fields
    """
    print("\n=== New Test Case ===")
    print("Enter input lines (empty line to finish inputs):")
    
    inputs = []
    while True:
        line = get_user_input("Input > ")
        if not line:
            if not inputs:
                print("At least one input line is required!")
                continue
            break
        inputs.append(line)
    
    print("\nRunning reference solution to get expected outputs...")
    
    # Run reference solution with the inputs
    process = subprocess.Popen(
        ['python', reference_solution],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    input_data = '\n'.join(inputs) + '\n'
    outputs, error = process.communicate(input=input_data)
    
    if error:
        print(f"Error in reference solution: {error}")
        return None
    
    outputs = outputs.splitlines()
    print("Reference solution outputs:")
    for i, output in enumerate(outputs):
        print(f"Output {i+1}: {output}")
    
    # Generate UID based on inputs and outputs
    uid = generate_uid(inputs, outputs)
    
    return {
        'uid': uid,
        'i': inputs,
        'o': outputs
    }

def generate_test_cases(reference_solution: str, output_file: str):
    """
    Main function to generate test cases interactively
    
    Args:
        reference_solution: Path to the reference solution script
        output_file: Path to save the generated JSON test cases
    """
    print("=== Test Case Generator ===")
    print(f"Reference solution: {reference_solution}")
    print("Enter test cases. Two empty inputs in a row will finish the process.\n")
    
    test_cases = []
    empty_count = 0
    
    while True:
        test_case = collect_test_case(reference_solution)
        if test_case is None:
            continue
        
        test_cases.append(test_case)
        print(f"\nTest case added with UID: {test_case['uid']}")
        
        # Prompt for another test case
        cont = get_user_input("\nAdd another test case? (y/n): ").lower()
        if cont != 'y':
            break
    
    # Prepare final JSON structure
    result = {
        'desc': f'Test cases for "{reference_solution}"',
        'main': test_cases
    }
    
    # Save to file
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\nSaved {len(test_cases)} test cases to {output_file}")

if __name__ == "__main__":
    import subprocess
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python python_oj_make.py <reference_solution.py> <output_file.json>")
        sys.exit(1)
    
    reference_solution = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(reference_solution):
        print(f"Error: Reference solution not found at {reference_solution}")
        sys.exit(1)
    
    generate_test_cases(reference_solution, output_file)