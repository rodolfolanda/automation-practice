# Practice Automation Shortcuts
# Add these lines to your ~/.zshrc file

# Quick access to your practice automation project
alias practice="cd ~/automation-practice && source .venv/bin/activate"
alias practice-ref="open ~/automation-practice/PRACTICE_PLAYWRIGHT_DAILY_REFERENCE.md"
alias practice-quick="open ~/automation-practice/QUICK_REFERENCE_CARD.md"
alias practice-test="cd ~/automation-practice && source .venv/bin/activate && pytest tests/test_practice_sites.py -v --headed"

# Usage after adding to ~/.zshrc and running 'source ~/.zshrc':
# practice      - Navigate to project and activate venv
# practice-ref  - Open daily reference guide
# practice-quick- Open quick reference card
# practice-test - Run practice tests with visual browser
