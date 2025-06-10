class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x  # начальная позиция по x
        self.y = y  # начальная позиция по y
        self.s = s  # размер шага (количество клеточек за ход)
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):

        if self.s <= 1:
            raise ValueError("s не может быть меньше или равно 0")
        self.s -= 1
    
    def count_moves(self, x2, y2):

        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        

        steps_x = dx // self.s
        steps_y = dy // self.s
        
        rem_x = dx % self.s
        rem_y = dy % self.s
        
        total_steps = steps_x + steps_y
        if rem_x != 0:
            total_steps += 1
        if rem_y != 0:
            total_steps += 1
        
        return total_steps
    
    def __str__(self):
        return f"Черепашка в позиции ({self.x}, {self.y}), шаг: {self.s}"

Wise_Turtle = Turtle(0,0)

print(Wise_Turtle.count_moves(3,3))
