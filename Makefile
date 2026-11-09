nothing:
	@echo 'The default target for this Makefile does nothing.'

check:
	@python3 scripts/check_rendering.py

all: sk.html sk2.html

%.html: %.tx2as
	python3 sub.py --format=html --output="$@" $^

