# Add these lines to your ~/.zshrc file

# D2L Playwright Project Shortcuts
alias d2l="cd ~/d2l/automation/playwright-ui-python && source venv/bin/activate"
alias d2l-ref="open ~/d2l/automation/playwright-ui-python/D2L_PLAYWRIGHT_DAILY_REFERENCE.md"
alias d2l-quick="open ~/d2l/automation/playwright-ui-python/QUICK_REFERENCE_CARD.md"
alias d2l-test="cd ~/d2l/automation/playwright-ui-python && source venv/bin/activate && pytest tests/test_login_pom.py -v --headed"

# Usage after adding to ~/.zshrc and running 'source ~/.zshrc':
# d2l           - Navigate to project and activate venv
# d2l-ref       - Open full reference guide  
# d2l-quick     - Open quick reference card
# d2l-test      - Quick test to verify everything works