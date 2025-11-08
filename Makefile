# -------- VARIABLES --------
ENV_NAME = stat159-hw3

# -------- TARGETS --------
env:
	@echo "Creating or updating conda environment: $(ENV_NAME)"
	@conda env update -f environment.yml --name $(ENV_NAME) --prune || conda env create -f environment.yml -n $(ENV_NAME)
	@echo "Environment ready, activate with: conda activate $(ENV_NAME)"

# Build the local HTML site
html:
	@echo "Building local HTML site with MyST"
	myst build --html
	@echo "HTML build complete, open with: myst start"

# Clean up generated artifacts
clean:
	@echo "Cleaning up build and generated files"
	rm -rf figures/ audio/ _build/
	@echo "Clean complete"
