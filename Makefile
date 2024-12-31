help:
	@echo
	@echo "======================================================================"
	@echo
	@echo "🚀  MAIN"
	@echo
	@echo "run:       run app"
	@echo
	@echo "📦 DEPENDENCIES"
	@echo
	@echo "env:        show environment info"
	@echo "deps:       list prod dependencies"o
	@echo
	@echo "======================================================================"
	@echo

#
# 🚀  MAIN
#

run:
	poetry run python app.py

#
# 📦 DEPENDENCIES
#

env:
	poetry run poetry env info

deps:
	poetry run poetry show --tree --only main
