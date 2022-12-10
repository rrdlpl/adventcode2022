import time

def parse_cycles(lines):
    instructions = []
    instructions.append(0)
    for line in lines:
        line = line.strip()
        command = line.split()
        instructions.append(0)
        if command[0] == 'addx':
            instructions.append(int(command[1]))
    return instructions

def signal_strength(cycles):
    x = 1
    strength = 0
    for cycle in range(1, len(cycles)):
        if cycle % 40 == 20:
            strength += cycle * x
        x += cycles[cycle]
    return strength

def draw_sprites(cycles):
    x = 1
    screen_size = 40
    crt = list(' ' * screen_size)
    for cycle in range(1, len(cycles)):
        pixel_index = (cycle - 1) % screen_size
        if (cycle - 1) > 0 and pixel_index == 0:
            print(''.join(crt))

        sprite_pixels = [x - 1, x, x + 1]
        # If the sprite is positioned such that one of its three pixels 
        # is the pixel currently being drawn, the screen produces a lit pixel (#); 
        # otherwise, the screen leaves the pixel dark
        if pixel_index in sprite_pixels:
            crt[pixel_index] = '#'
        else:
            crt[pixel_index] = ' '
        x += cycles[cycle]
    print(''.join(crt))

file = open('day10/input.txt', 'r')
lines = file.readlines()

start_time = time.time()

cycles = parse_cycles(lines)
strength = signal_strength(cycles)
print('Solution 1. Signal strength', strength)
draw_sprites(cycles)
end_time = time.time()
print('Time ellapsed', (end_time - start_time) * 1000)

file.close()

