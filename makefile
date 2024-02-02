CC = gcc
CFLAGS = -Wall -Wextra -pedantic -std=c11
LDFLAGS = -lcs50

all: my_program

my_program: test.c
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f my_program

.PHONY: all clean
