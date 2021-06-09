# help         Show this information.
.PHONY: help
help:
	cat makefile | grep -oP "^# \K(.*)"

# clean        Remove (!) all untracked and ignored files.
.PHONY: clean
clean:
	git clean -xdff
	
# ‎‎
# ---------------------------------------------------------------------------
# The following commands must be run in the deploy environment.
# ---------------------------------------------------------------------------
# ‎‎

.PHONY: docs-deploy
docs-deploy:
	python3 -m illiterate --inline easy_tbot docs/api
	cp README.md docs/index.md

# docs         Compile and publish the documentation to Github.
.PHONY: docs
docs: docs-deploy
	mkdocs build

# gh-deploy    Deploy docs to Github Pages
.PHONY: gh-deploy
gh-deploy: docs-deploy
	git remote add pages git@github.com:easy_tbot/easy_tbot.github.io || echo "remote exists"
	mkdocs gh-deploy -r pages -b master --force

# format       Format all source code inplace using `black`.
.PHONY: format
format:
	(git status | grep -E "nothing to commit|nada para hacer commit") && black easy_tbot/ || echo "(!) REFUSING TO REFORMAT WITH UNCOMMITED CHANGES" && exit
	git status
# 