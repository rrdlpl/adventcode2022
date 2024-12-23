
from collections import defaultdict


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
    print('secret number' , secret_number_gen.secret_number)
    
  return secret_number_gen.secret_number


def calculate_prices(secret_number, iterations):
  secret_number_gen = SecretNumberGenerator(secret_number)
  prices = [secret_number % 10]

  for _ in  range(iterations):
    secret_number_gen.next()
    prices.append(secret_number_gen.secret_number % 10)
  
  prices_diff = []
  for i  in range(len(prices) - 1):
    prices_diff.append(prices[i + 1] - prices[i])
  return prices, prices_diff
def part_one():
  
  secret_numbers = parse_input()
  result = 0
  for secret_number in secret_numbers:
    result += calculate_secret_number(secret_number, 2000)
  
  return result


def get_all_sequences(prices, prices_diff):
    bananas_map = {}
    for i in range(len(prices_diff) - 3):
        sequence = (prices_diff[i], prices_diff[i + 1], prices_diff[i + 2], prices_diff[i + 3])
        if sequence not in bananas_map:
            bananas_map[sequence] = prices[i + 4]
    
    if len(prices) <= 11:
      for key in bananas_map:
        print(key, '= ',  bananas_map[key])
    return bananas_map  
  
def part_two():
  bananas = defaultdict(lambda: 0)
  secret_numbers = parse_input()
  for secret_number in secret_numbers:
    prices, prices_diff = calculate_prices(secret_number, 10)
    b = get_all_sequences(prices, prices_diff)
    for key, value in b.items():
      bananas[key] += value
  
  return max(bananas.values())

# print('Solution 1.', part_one())
print('Solution 2', part_two())