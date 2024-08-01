import knowledgebase 

class Agent:
    def __init__(self, program):
        self.program = program
        self.position = (0, 0)
        self.direction = 'E'
        self.health = 100
        self.has_gold = False
        self.knowledge_base = KnowledgeBase()

    def perceive(self):
        x, y = self.position
        cell_info = self.program.get_cell_info(x, y)
        if cell_info:
            self.knowledge_base.add_fact(f"Agent at {self.position}: {cell_info}")
        return cell_info

    def decide_action(self, percept):
        self.knowledge_base.infer_new_facts()
        # Logic to decide the next action
        if percept == 'G':
            self.has_gold = True
            return 'Grab'
        elif percept == 'S':
            return 'Shoot'
        elif percept == 'B':
            # More complex logic could be used here
            return 'Move to Safe Cell'
        else:
            return 'Move Forward'

    def move_forward(self):
        x, y = self.position
        if self.direction == 'E':
            self.position = (x, y + 1)
        elif self.direction == 'W':
            self.position = (x, y - 1)
        elif self.direction == 'N':
            self.position = (x - 1, y)
        elif self.direction == 'S':
            self.position = (x + 1, y)

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def perform_action(self, action):
        if action == 'Move Forward':
            self.move_forward()
        elif action == 'Turn Left':
            self.turn_left()
        elif action == 'Turn Right':
            self.turn_right()
        elif action == 'Grab':
            self.has_gold = True
        elif action == 'Shoot':
            pass  # Implement shooting logic

    def run(self):
        while True:
            percept = self.perceive()
            action = self.decide_action(percept)
            self.perform_action(action)
            if self.has_gold:
                break
        self.knowledge_base.print_knowledge_base()

# Example usage
program = Program('map1.txt')
agent = Agent(program)
agent.run()
