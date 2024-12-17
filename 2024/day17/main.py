class Computer:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    self.outs = []
    self.pointer = 0
  
  def run(self, program):
    self.program = ','.join([str(p) for p in program])
    while self.pointer < len(program):
      opcode, operand = program[self.pointer], program[self.pointer + 1]
      if opcode == 0:
        self.adv(operand)
      elif opcode == 1:
        self.bxl(operand)
      elif opcode == 2:
        self.bst(operand)
      elif opcode == 3:
        self.jnz(operand)
      elif opcode == 4:
        self.bxc(operand)
      elif opcode == 5:
        self.out(operand)
      elif opcode == 6:
        self.bdv(operand)
      elif opcode == 7:
        self.cdv(operand)
   
   
  def adv(self, operand): #0
    n = self.a // (2 ** self.get_combo_operand_value(operand))
    self.a = n
    self.pointer += 2

  def bxl(self, operand): #1
    self.b = self.b ^ operand
    self.pointer += 2
  
  def bst(self, operand): #2
    t = self.get_combo_operand_value(operand) % 8
    self.b = t
    self.pointer += 2
        
  def jnz(self, operand): #3
    if self.a == 0:
      self.pointer += 2
      return
    self.pointer = operand
  
  def bxc(self, _operand): #4
    self.b = self.b ^ self.c
    self.pointer += 2
  
  def out(self, operand): #5
    value = self.get_combo_operand_value(operand) % 8
    self.outs.append(value)
    self.pointer += 2
    # print('out', value)
  
  def bdv(self, operand): #6
    self.b = self.a // (2 ** self.get_combo_operand_value(operand))
    self.pointer += 2
  
  def cdv(self, operand): #7
    self.c = self.a // (2 ** self.get_combo_operand_value(operand))
    self.pointer += 2
  
  def get_combo_operand_value(self, operand):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return self.a
    if operand == 5:
        return self.b
    if operand == 6:
        return self.c
    return 7

  
  def print(self):
    return ','.join([str(x) for x in self.outs])

a =  729
b = 0
c = 0

program = [int(instruction) for instruction in "0,1,5,4,3,0".split(",")]




# Here are some examples of instruction operation:

# If register C contains 9, the program 2,6 would set register B to 1.
computer = Computer(0, 0, 9)
computer.run([2, 6])
print("If register C contains 9, the program 2,6 would set register B to 1.", computer.b == 1)

# If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
computer = Computer(10, 0, 0)

print("If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.")
computer.run([5, 0, 5, 1, 5, 4])
computer.print()
print('')

# If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
computer = Computer(2024, 0, 0)
computer.run([0, 1, 5, 4, 3, 0 ])
print("If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A. Register =", computer.a, computer.a == 0)
computer.print()
print('')

# # If register B contains 29, the program 1,7 would set register B to 26.
computer = Computer(0, 29, 0)
computer.run([1, 7])
print("If register B contains 29, the program 1,7 would set register B to 26. B =", computer.b, computer.b == 26)
print('')

# # If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354.
computer = Computer(0, 2024, 43690)
computer.run([4, 0])
print("If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354.", computer.b == 44354)
print('')


print("\n\n Test example: Expected output: 4,6,3,5,6,3,5,2,1,0")
computer = Computer(729, 0, 0)
computer.run([0,1,5,4,3,0])
computer.print()
print('')


part_one = Computer(25358015, 0, 0)
part_one.run([2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0])
print("\n\n Registers part 1:", part_one.a, part_one.b, part_one.c)

print('Solution 1:')
part_one.print()

#attempt 1: 2,7,2,5,1,2,7,3,7

part_two_test = Computer(2024, 0, 0)
part_two_test.run([0,3,5,4,3,0])
print('')
print('Part two test: \n')
part_two_test.print()

# for A in range(0, 1000000):
#   program = [0,3,5,4,3,0]
#   p2 = Computer(A, 0, 0)
#   p2.run(program)
#   if p2.print().endswith('4,3,0'):
#     print('endswith', A)
#   if p2.print() == '0,3,5,4,3,0':
#     print('Solution 2',A)
#     exit(0)
    

def find_A(program, stack, n=1):
    if n > len(program):
        return min(stack)
   
    next_stack = []
    for num in stack:
        for i in range(8):
            A = 8 * num + i
            p2 = Computer(A, 0, 0)
            p2.run(program)
            if p2.outs == program[-n:]: # if last digits match is a good candidate
                next_stack.append(A)
        print(next_stack)

    return find_A(program, next_stack, n + 1)

print('Solution 2. Test', find_A([0,3,5,4,3,0], [0])) # 117400
print('Solution 2. ', find_A([2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0], [0]))
  


# while left <= right:
#   mid = (left + right) // 2
#   part_two_test = Computer(mid, 0, 0)
#   # part_two_test.run([2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0])
#   part_two_test.run([0,3,5,4,3,0])

#   target = part_two_test.program.replace(',', '')
#   p = part_two_test.print().replace(',', '')
#   if len(p) == len(target):
#     print('Solution 2.', mid)
#     print('Search range', left, right)
#     # exit(0)
#     right = mid - 1
#   if len(p) < len(target):
#     left = mid + 1
#   else:
#     right = mid -1
  