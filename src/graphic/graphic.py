import pygame
class Graphic:
    def __init__(self, file_path):
        # Initialize grid as a 2D array of lists
        self.N, self.grid = self.read_input(file_path)
        self.cell_size = 64
        self.window_size = self.N * self.cell_size
        self.screen = None
        self.elements = {}

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_size, self.window_size))
        pygame.display.set_caption('Wumpus World')

        # Load assets
        self.load_assets()

        # Update percepts
        self.update_percepts()

    def load_assets(self):
        self.elements['A'] = pygame.image.load('../../asset/agent.png')
        self.elements['W'] = pygame.image.load('../../asset/wumpus.png')
        self.elements['G'] = pygame.image.load('../../asset/gold.png')
        self.elements['P'] = pygame.image.load('../../asset/pit.png')
        self.elements['P_G'] = pygame.image.load('../../asset/gas.png')
        self.elements['H_P'] = pygame.image.load('../../asset/potion.png')

        for key in self.elements:
            self.elements[key] = pygame.transform.scale(self.elements[key], (self.cell_size, self.cell_size))

    def update_percepts(self):
        for x in range(self.N):
            for y in range(self.N):
                cell_content = self.grid[x][y]
                if 'W' in cell_content:  # Wumpus
                    self.apply_stench(x, y)
                if 'P' in cell_content:  # Pit
                    self.apply_breeze(x, y)
                if 'P_G' in cell_content:  # Poisonous Gas
                    self.apply_whiff(x, y)
                if 'H_P' in cell_content:  # Healing Potion
                    self.apply_glow(x, y)

    def apply_stench(self, x, y):
        self.apply_percept(x, y, 'S')

    def apply_breeze(self, x, y):
        self.apply_percept(x, y, 'B')

    def apply_whiff(self, x, y):
        self.apply_percept(x, y, 'W_H')

    def apply_glow(self, x, y):
        self.apply_percept(x, y, 'G_L')

    def apply_percept(self, x, y, percept):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.N and 0 <= ny < self.N:
                if percept not in self.grid[nx][ny]:
                    self.grid[nx][ny].append(percept)

    def draw_grid(self):
        for x in range(self.N):
            for y in range(self.N):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
                cell_content = self.grid[x][y]
                for element in cell_content:
                    if element in self.elements:
                        self.screen.blit(self.elements[element], (y * self.cell_size, x * self.cell_size))

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))
            self.draw_grid()
            pygame.display.flip()

        pygame.quit()

    def read_input(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()

        N = int(lines[0].strip())  # First line is the grid size
        grid = [[cell.split(',') if cell != '-' else [] for cell in line.strip().split('.')] for line in lines[1:]]
        return N, grid

wumpus_world = Graphic("../../asset/input/level1.txt")
wumpus_world.run_game()