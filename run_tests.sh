#!/bin/bash
# D2L Playwright Test Runner
# Convenience script to run tests with proper PYTHONPATH

# Set the project directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS_DIR="${PROJECT_DIR}/tests"

# Export PYTHONPATH to include tests directory
export PYTHONPATH="${TESTS_DIR}"

# Activate virtual environment if it exists
if [[ -f "${PROJECT_DIR}/venv/bin/activate" ]]; then
    source "${PROJECT_DIR}/venv/bin/activate"
    echo "✅ Virtual environment activated"
else
    echo "⚠️  Virtual environment not found. Run: python3 -m venv venv && source venv/bin/activate"
fi

# .env file is optional for practice sites (no sensitive credentials needed)
if [[ -f "${PROJECT_DIR}/.env" ]]; then
    echo "📋 Using custom .env configuration"
else
    echo "📋 Using default configuration (no .env needed for practice sites)"
fi

echo "🚀 Running Practice Playwright tests..."
echo "📂 Project directory: ${PROJECT_DIR}"
echo "🐍 Python path: ${PYTHONPATH}"

# Run the tests with provided arguments or default to all tests
if [[ $# -eq 0 ]]; then
    echo "🧪 Running all practice tests..."
    pytest "${TESTS_DIR}/test_practice_sites.py" -v --headed
else
    echo "🧪 Running: $@"
    pytest "$@"
fi