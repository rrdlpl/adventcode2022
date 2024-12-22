
class SecretNumberGenerator:
  def __init__(self, secret_number):
    self.secret_number = secret_number
  
  def mix(self, value):
    self.secret_number = self.secret_number ^ value
  def prune(self):
    if self.secret_number == 100000000:
      self.secret_number = 16113920
      return
    mod = self.secret_number % 16777216
    self.secret_number = mod
  
  def next(self):
    mult = self.secret_number * 64
    self.mix(mult)
    self.prune()
    div = self.secret_number // 32
    self.mix(div)
    self.prune()
    mult = self.secret_number * 2048
    self.mix(mult)
    self.prune()
    
def parse_input():
  file = open('2024/day22/input.txt', 'r')
  secret_numbers = [int(line.strip()) for line in file.readlines()]
  return secret_numbers

def calculate_secret_number(secret_number, iterations):
  secret_number_gen = SecretNumberGenerator(secret_number)
  for _ in  range(iterations):
    secret_number_gen.next()
    # print('secret number' , secret_number_gen.secret_number)
    
  return secret_number_gen.secret_number

def part_one():
  
  secret_numbers = parse_input()
  result = 0
  for secret_number in secret_numbers:
    result += calculate_secret_number(secret_number, 2000)
  
  return result


print('Solution 1.', part_one())