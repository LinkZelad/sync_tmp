.PHONY: clean

CC = gcc
CFLAGS = -I include
CFILES = $(shell find src -name "*.c")
OBJS = $(CFILES:.c=.o)
TARGET = main
# DATA = src/data/*.txt

RM = -rm -f
# all: $(TARGET)
# 	echo "Clean"
	# git commit -a -m "> make"

$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

%o : %c
	$(CC) -c $(CFLAGS) $< -o $@

clean:
	$(RM) $(TARGET) $(OBJS) $(DATA)
	# git commit -a -m "> make clean"
