RM = rm -f
HTML_FILES = sk.html sk2.html
CLEAN_FILES = $(HTML_FILES)

nothing:
	@echo 'The default target for this Makefile does nothing.'

clean:
	$(RM) -- $(CLEAN_FILES)

check:
	@python3 scripts/check_rendering.py

all: $(HTML_FILES)

%.html: %.tx2as
	python3 sub.py --format=html --output="$@" $^

