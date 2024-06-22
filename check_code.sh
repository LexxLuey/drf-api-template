#!/bin/bash

# Set exit on errors
set -e
trap 'set +e; echo "Error encountered during linting!" >&2; exit 1' ERR

# Define directory for linting (default: current directory)
LINT_DIR="${1:-.}"

# Tools used for linting (adjust as needed) pycodestyle flake8 pylint
LINTERS=(flake8)

# Find all Python files recursively
PYTHON_FILES=$(find "$LINT_DIR" -name "*.py" -type f)

# Run all linters on each file
has_errors=0 # Flag to track if any linter encountered errors

# Function to run a linter on a file
run_linter() {
    local linter="$1"
    local file="$2"
    echo "Running $linter on $file..."
    if ! command -v "$linter" &>/dev/null; then
        echo "Error: Linter '$linter' not found. Please install."
        exit 1
    fi
    # Call the linter on the file
    "$linter" "$file" || has_errors=1

}

# Run all linters on each file
for file in $PYTHON_FILES; do
    for linter in "${LINTERS[@]}"; do
        run_linter "$linter" "$file"
    done
done

# Print final message based on error flag
if [ $has_errors == 1 ]; then
    echo -e "\033[31m Code linting failed ✋. Please fix the identified issues 👆 then try again. \033[0m "
else
    echo -e "\033[32m Code linting successful! 🎉 \n Go ahead and make that PR.\033[0m 🚀"
fi
