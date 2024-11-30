from functools import reduce

class Packet:

    def __init__(self, bits):
        self.bits = bits
        #print('Initializing packet with bits:', self.bits)

    # Parses data and returns the number of bits in the packet
    def parse(self):
        self.version = int(self.bits[:3], 2)
        self.type = int(self.bits[3:6], 2)
        self.data = {}
        if self.type == 4:
            self.data['value'] = 0
            i = 6
            while True:
                self.data['value'] = self.data['value'] * 16 + int(self.bits[i+1:i+5], 2)
                i += 5
                if self.bits[i-5] == '0':
                    break
        else:
            self.data['length_type_id'] = int(self.bits[6], 2)
            if self.data['length_type_id'] == 0:
                i = 7 + 15
                self.data['length_bits'] = int(self.bits[7:i], 2)
            else:
                i = 7 + 11
                self.data['length_packets'] = int(self.bits[7:i], 2)
            self.data['packets'] = []
            header_length = i
            while True:
                packet = Packet(self.bits[i:])
                self.data['packets'].append(packet)
                i += packet.parse()
                if self.data['length_type_id'] == 0:
                    if self.data['length_bits'] == i - header_length:
                        break
                elif self.data['length_type_id'] == 1:
                    if self.data['length_packets'] == len(self.data['packets']):
                        break
        return i

class Problem:

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        data = f.read().strip()
        self.packet = Packet(''.join('{:04b}'.format(int(x, 16)) for x in data))

    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())
        print("Puzzle 2: ", self.solvePart2())

    def sumVersion(self, packet):
        version = packet.version
        if 'packets' in packet.data:
            for p in packet.data['packets']:
                version += self.sumVersion(p)
        return version

    def processPacket(self, packet):
        if packet.type == 4:
            return packet.data['value']
        elif packet.type == 0:
            return sum(self.processPacket(p) for p in packet.data['packets'])
        elif packet.type == 1:
            return reduce(lambda x, y: x * y, [self.processPacket(p) for p in packet.data['packets']])
        elif packet.type == 2:
            return min(self.processPacket(p) for p in packet.data['packets'])
        elif packet.type == 3:
            return max(self.processPacket(p) for p in packet.data['packets'])
        elif packet.type == 5:
            return 1 if self.processPacket(packet.data['packets'][0]) > self.processPacket(packet.data['packets'][1]) else 0
        elif packet.type == 6:
            return 1 if self.processPacket(packet.data['packets'][0]) < self.processPacket(packet.data['packets'][1]) else 0
        elif packet.type == 7:
            return 1 if self.processPacket(packet.data['packets'][0]) == self.processPacket(packet.data['packets'][1]) else 0
        else:
            raise Exception('Unknown packet type:', packet.type)

    def solvePart1(self):
        self.packet.parse()
        return self.sumVersion(self.packet)

    def solvePart2(self):
        self.packet.parse()
        return self.processPacket(self.packet)


problem = Problem()
problem.solve()
