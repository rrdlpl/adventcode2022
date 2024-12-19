from dataclasses import dataclass
import re
from PIL import Image
from typing import Tuple


WIDE = 101
TALL = 103
@dataclass
class Robot:
  position: Tuple[int, int]
  velocity: Tuple[int, int]

def parse_input():
   file = open('2024/day14/input.txt', 'r')
   lines = file.readlines()
   robots = []
   for line in lines:
     line = line.strip()
     match = re.search("p=(\\d+,\\d+) v=(-?\\d+,-?\\d+)", line)
     if match:
       position = tuple(map(int, match.group(1).split(',')))
       velocity = tuple(map(int, match.group(2).split(',')))
        
       robots.append(Robot(position, velocity))

   return robots
def move_robot(robots, seconds):
    for robot in robots:
      position = robot.position
      vx = robot.velocity[0]
      vy = robot.velocity[1]
      new_velocity = (vx * seconds, vy * seconds)
      new_position = ((position[0] +  new_velocity[0]) % WIDE , (position[1] + new_velocity[1]) % TALL)
      robot.position = new_position
      



  

def draw_robots_image(width, height, robots, output_filename):
    # Create a new image with white background
    image = Image.new("RGB", (width, height), "black")
    pixels = image.load()

    # Draw green pixels at robot positions
    for robot in robots:
        x, y = robot.position
        if 0 <= x < width and 0 <= y < height:
            pixels[x, y] = (0, 255, 0)  # RGB for green

    # Save the image to a file
    image.save(output_filename)

robots = parse_input()

for i in range(0, 6493):
   move_robot(robots,  1)
   if i >= 6000:
     draw_robots_image(WIDE, TALL, robots, f"visualization/frame{i}.png")
   
    
     