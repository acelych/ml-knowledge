import subprocess
import sys
import os
import json
from typing import Dict, List, Tuple, Optional

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class TestCase:
    """Class representing a single test case"""
    def __init__(self, uid: str, inputs: List[str], outputs: List[str]):
        self.uid = uid
        self.inputs = inputs
        self.outputs = outputs

class TestResult:
    """Class representing the result of a test case"""
    def __init__(self, uid: str, passed: bool, user_output: str, expected_output: str):
        self.uid = uid
        self.passed = passed
        self.user_output = user_output
        self.expected_output = expected_output

def load_test_cases(json_file_path: str) -> Tuple[str, List[TestCase]]:
    """
    Load test cases from JSON file
    
    Args:
        json_file_path: Path to JSON file containing test cases
        
    Returns:
        Tuple: (description, list of TestCase objects)
        
    Raises:
        ValueError: If JSON file is malformed
    """
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
        
        description = data.get('desc', 'No description provided')
        test_cases = []
        
        for case in data.get('main', []):
            if 'uid' not in case or 'i' not in case or 'o' not in case:
                raise ValueError("Test case missing required fields (uid, i, o)")
            
            test_cases.append(TestCase(
                uid=str(case['uid']),
                inputs=case['i'],
                outputs=case['o']
            ))
        
        return description, test_cases
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {str(e)}")

def run_test_case(user_script_path: str, test_case: TestCase) -> TestResult:
    """
    Run a single test case against user script
    
    Args:
        user_script_path: Path to user's Python script
        test_case: TestCase object to run
        
    Returns:
        TestResult object with results
    """
    try:
        # Combine inputs with newlines to simulate user entering each line
        input_data = '\n'.join(test_case.inputs) + '\n'
        
        # Run user script
        process = subprocess.Popen(
            [sys.executable, user_script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Get output and error
        user_output, error_output = process.communicate(input=input_data)
        
        # Handle runtime errors
        if error_output:
            return TestResult(
                uid=test_case.uid,
                passed=False,
                user_output=f"Runtime Error: {error_output}",
                expected_output='\n'.join(test_case.outputs)
            )
        
        # Normalize outputs for comparison
        user_output_normalized = user_output.rstrip()
        expected_output_normalized = '\n'.join(test_case.outputs).rstrip()
        
        # Compare outputs
        passed = user_output_normalized == expected_output_normalized
        
        return TestResult(
            uid=test_case.uid,
            passed=passed,
            user_output=user_output_normalized,
            expected_output=expected_output_normalized
        )
        
    except Exception as e:
        return TestResult(
            uid=test_case.uid,
            passed=False,
            user_output=f"System Error: {str(e)}",
            expected_output='\n'.join(test_case.outputs)
        )

def run_oj(user_script_path: str, test_cases_json_path: str, specific_uid: Optional[str] = None) -> Dict[str, TestResult]:
    """
    Main OJ function to run all or specific test cases
    
    Args:
        user_script_path: Path to user's Python script
        test_cases_json_path: Path to JSON file with test cases
        specific_uid: Optional UID to run only one test case
        
    Returns:
        Dictionary mapping UIDs to TestResult objects
    """
    # Load test cases
    try:
        description, test_cases = load_test_cases(test_cases_json_path)
        print(f"OJ System - {description}")
        print(f"Found {len(test_cases)} test cases")
    except ValueError as e:
        print(f"Error loading test cases: {str(e)}")
        return {}
    
    results = {}
    
    # Filter test cases if specific UID is requested
    if specific_uid:
        test_cases = [tc for tc in test_cases if tc.uid == specific_uid]
        if not test_cases:
            print(f"No test case found with UID: {specific_uid}")
            return {}
    
    # Run each test case
    for test_case in test_cases:
        print(f"\nRunning test case {test_case.uid}...")
        result = run_test_case(user_script_path, test_case)
        results[test_case.uid] = result
        
        if result.passed:
            print(f"Test case {test_case.uid}: {color.GREEN}PASSED{color.END}")
        else:
            print(f"Test case {test_case.uid}: {color.RED}FAILED{color.END}")
            print("User output:")
            print(result.user_output)
            print("\nExpected output:")
            print(result.expected_output)
    
    # Print summary
    passed_count = sum(1 for r in results.values() if r.passed)
    print(f"\nSummary: {passed_count}/{len(test_cases)} test cases passed")
    
    return results

def main():
    # Command line usage
    if len(sys.argv) < 3:
        print("Usage: python oj_system.py <user_script> <test_cases_json> [specific_uid]")
        print("Example: python oj_system.py solution.py test_cases.json")
        print("Example (single test case): python oj_system.py solution.py test_cases.json 46102865483261")
        sys.exit(1)
    
    user_script = sys.argv[1]
    test_cases_json = sys.argv[2]
    specific_uid = sys.argv[3] if len(sys.argv) > 3 else None
    
    # Check files exist
    for file_path in [user_script, test_cases_json]:
        if not os.path.exists(file_path):
            print(f"Error: File not found - {file_path}")
            sys.exit(1)
    
    # Run OJ
    run_oj(user_script, test_cases_json, specific_uid)

if __name__ == "__main__":
    main()