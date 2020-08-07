.PHONY: all say_hello generate clean

CC := gcc

CC := ${CC}

all: 
	@echo ${CC}

# .DEFAULT_GOAL := clean
# normally only first command is run when using make, default goal allows us to specify with func to run

say_hello:
# @hides the command that is used
	@echo "Hello World"


generate:
	@echo "Creating empty text files..."
	touch file={1..10}.text

clean:
	@echo "removing txt files"
	rm *.text