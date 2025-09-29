#!/usr/bin/env python3
"""
Custom Playwright Python linting rules
Similar to eslint-plugin-playwright but for Python
"""

import ast
import sys
import re
from pathlib import Path

class PlaywrightLinter(ast.NodeVisitor):
    """Custom linter for Playwright Python best practices"""
    
    def __init__(self):
        self.errors = []
        self.line_number = 0
    
    def visit_Call(self, node):
        """Check function calls for Playwright anti-patterns"""
        
        # Check for time.sleep() usage (should use Playwright waits)
        if (hasattr(node.func, 'attr') and 
            node.func.attr == 'sleep' and
            hasattr(node.func.value, 'id') and 
            node.func.value.id == 'time'):
            self.errors.append(
                f"Line {node.lineno}: Avoid time.sleep(). Use page.wait_for_*() methods instead"
            )
        
        # Check for hardcoded selectors (should be in page objects)
        if (hasattr(node.func, 'attr') and 
            node.func.attr in ['click', 'fill', 'locator'] and
            node.args):
            first_arg = node.args[0]
            if (hasattr(first_arg, 's') and 
                isinstance(first_arg.s, str) and
                ('#' in first_arg.s or '.' in first_arg.s)):
                self.errors.append(
                    f"Line {node.lineno}: Consider moving selector '{first_arg.s[:20]}...' to page object"
                )
        
        self.generic_visit(node)
    
    def visit_Await(self, node):
        """Check await patterns"""
        # Could add checks for missing awaits on async Playwright methods
        self.generic_visit(node)

def check_file(file_path):
    """Check a Python file for Playwright best practices"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Parse the AST
        tree = ast.parse(content)
        linter = PlaywrightLinter()
        linter.visit(tree)
        
        if linter.errors:
            print(f"\n❌ Playwright issues in {file_path}:")
            for error in linter.errors:
                print(f"  {error}")
            return False
        else:
            print(f"✅ {file_path} - No Playwright issues found")
            return True
            
    except Exception as e:
        print(f"Error checking {file_path}: {e}")
        return False

def main():
    """Main linter function"""
    if len(sys.argv) < 2:
        print("Usage: python playwright_linter.py <file_or_directory>")
        sys.exit(1)
    
    target = Path(sys.argv[1])
    all_good = True
    
    if target.is_file():
        if target.suffix == '.py':
            all_good = check_file(target)
    elif target.is_dir():
        for py_file in target.rglob("*.py"):
            if not check_file(py_file):
                all_good = False
    
    if all_good:
        print("\n🎉 All files pass Playwright best practices!")
        sys.exit(0)
    else:
        print("\n💡 Fix the issues above for better Playwright code!")
        sys.exit(1)

if __name__ == "__main__":
    main()