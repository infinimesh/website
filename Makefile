.PHONY: commit-check lint htmlhint links site-urls actionlint yamllint gitleaks

commit-check: lint
	@echo "commit-check passed."

lint: htmlhint links site-urls actionlint yamllint gitleaks
	@echo "lint passed."

htmlhint:
	htmlhint index.html api/index.html

links:
	sh scripts/lychee.sh --root-dir "$(CURDIR)" index.html api/index.html llms.txt llms-full.txt README.md

site-urls:
	python3 scripts/check_site_urls.py

actionlint:
	actionlint

yamllint:
	yamllint --strict .

gitleaks:
	gitleaks dir . --no-banner --redact
