import time

def print_figure(position, direction):
    figure = ' o\n/|\\\n/\\'
    if direction == 'right':
        print(' ' * position + figure)
    else:
        print(' ' * (position - 3) + figure)

def main():
    position = 0
    for i in range(5):
        print_figure(position, 'right')
        time.sleep(0.5)
        print_figure(position, 'left')
        time.sleep(0.5)
        position += 3

if __name__ == "__main__":
    main()
