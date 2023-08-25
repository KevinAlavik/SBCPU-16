class SBUCPU:
    def __init__(self):
        self.registers = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'PC': 0
        }
        self.memory = [0] * 65536  # 64KB memory space

    def load_program(self, program):
        self.memory[:len(program)] = program
    
    def run(self):
        while True:
            opcode = self.memory[self.registers['PC']]
            
            if opcode == 0x00:
                # Halt the CPU
                break
            elif opcode == 0x01:
                # Load opcode
                reg_a = self.memory[self.registers['PC'] + 1]
                if reg_a in self.registers:
                    value = self.memory[self.registers['PC'] + 2]
                    self.registers[reg_a] = value
                else:
                    print("Invalid register")
                self.registers['PC'] += 3  # Move to the next instruction
            elif opcode == 0x02:
                # Add opcode
                reg_a = self.memory[self.registers['PC'] + 1]
                reg_b = self.memory[self.registers['PC'] + 2]
                if reg_a in self.registers and reg_b in self.registers:
                    self.registers[reg_a] += self.registers[reg_b]
                else:
                    print("Invalid registers")
                self.registers['PC'] += 3  # Move to the next instruction
            elif opcode == 0x03:
                # Sub opcode
                reg_a = self.memory[self.registers['PC'] + 1]
                reg_b = self.memory[self.registers['PC'] + 2]
                if reg_a in self.registers and reg_b in self.registers:
                    self.registers[reg_a] -= self.registers[reg_b]
                else:
                    print("Invalid registers")
                self.registers['PC'] += 3  # Move to the next instruction
            else:
                # Invalid opcode
                print("Invalid opcode")
                break  # Halt the CPU on unknown opcode


