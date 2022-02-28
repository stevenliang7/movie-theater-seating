class theatre:
    def __init__(self):
        self.grid = []
        for i in range(10):
            row = []
            seats = []
            for j in range(20):
                seats.append('s')
            row.append(seats)
            row.append(20)
            self.grid.append(row)
        self.total = 200
        self.key = 'ABCDEFGHIJ'
    def __str__(self):
        ret = ''
        for row in self.grid:
            for seat in row[0]:
                ret += seat
            ret += '\n'
        return ret
            
    def reserve(self, seats: int):
        reserved = []
        # check if there are enough available seats to fit the party
        if self.total < seats:
            return []
        for i in range(len(self.grid)-1, -1, -1):
            # row has enough seats available to fit reservation
            if (self.grid[i][1] >= seats):
                row = ''.join(self.grid[i][0])
                start = row.find('s'*seats)
                # check if there are enough sequential seats in the row
                if(start != -1):
                    for j in range(seats):
                        # change seat to reserved
                        self.grid[i][0][start+j] = 'r'
                        self.grid[i][1] -= 1
                        self.total -= 1
                        reserved.append(self.key[i] + str(start+j+1))
                    self.buffer(i, start, start+seats-1)
                    return reserved
        return []
    # adjust buffer seats around reservation for customer safety
    def buffer(self, row: int, start: int, end: int):
        for i in range(start, end+1):
            # block out up to 3 seats to the left if possible
            for j in range(1,4):
                if start-j >= 0 and self.grid[row][0][start-j] != 'x':
                    # change value in grid to x to represent blocked seat
                    self.grid[row][0][start-j] = 'x'
                    self.grid[row][1] -= 1
                    self.total -= 1
                # out of bounds or seats are already blocked
                else:
                    break
            # block out up to 3 seats to the right if possible
            for j in range(1,4):
                if end+j < len(self.grid[row][0]) and self.grid[row][0][end+j] != 'x':
                    # change value in grid to x to represent blocked seat
                    self.grid[row][0][end+j] = 'x'
                    self.grid[row][1] -= 1
                    self.total -= 1
                # out of bounds or seats are already blocked
                else:
                    break
            # not the first row
            if row > 0:
                # seat in front isn't already blocked
                if self.grid[row-1][0][i] != 'x':
                    self.grid[row-1][0][i] = 'x'
                    self.grid[row-1][1] -= 1
                    self.total -= 1
            # not the last row
            if row < len(self.grid) - 1:
                if self.grid[row+1][0][i] != 'x':
                    self.grid[row+1][0][i] = 'x'
                    self.grid[row+1][1] -= 1
                    self.total -= 1