# Practice Automation Shortcuts# Add these lines to your ~/.zshrc file



# Quick access to your practice automation project# D2L Playwright Project Shortcuts

alias practice="cd ~/automation-practice && source .venv/bin/activate"alias d2l="cd ~/d2l/automation/playwright-ui-python && source venv/bin/activate"

alias practice-ref="open ~/automation-practice/PRACTICE_PLAYWRIGHT_DAILY_REFERENCE.md"alias d2l-ref="open ~/d2l/automation/playwright-ui-python/D2L_PLAYWRIGHT_DAILY_REFERENCE.md"

alias practice-quick="open ~/automation-practice/QUICK_REFERENCE_CARD.md"alias d2l-quick="open ~/d2l/automation/playwright-ui-python/QUICK_REFERENCE_CARD.md"

alias practice-test="cd ~/automation-practice && source .venv/bin/activate && pytest tests/test_practice_sites.py -v --headed"alias d2l-test="cd ~/d2l/automation/playwright-ui-python && source venv/bin/activate && pytest tests/test_login_pom.py -v --headed"



# Usage:# Usage after adding to ~/.zshrc and running 'source ~/.zshrc':

# practice      - Navigate to project and activate venv# d2l           - Navigate to project and activate venv

# practice-ref  - Open daily reference guide# d2l-ref       - Open full reference guide  

# practice-quick- Open quick reference card# d2l-quick     - Open quick reference card

# practice-test - Run practice tests with visual browser# d2l-test      - Quick test to verify everything works