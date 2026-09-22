validate:
	python3 scripts/validate.py

test:
	python3 -m unittest discover -s tests -v

links:
	python3 scripts/check_links.py
