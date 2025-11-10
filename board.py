import pygame
import sys
import random

pygame.init()

# -------- WINDOW + BOARD SETUP --------
WIDTH, HEIGHT = 720, 720
TILE = WIDTH // 8
screen = pygame.display.set_mode((WIDTH + 250, HEIGHT))
pygame.display.set_caption("Rook Survival Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 26)
bigfont = pygame.font.SysFont("Arial", 32)

LIGHT = (235, 235, 208)
DARK  = (119, 148, 85)
FILES = "abcdefgh"

# -------- LOAD PIECES --------
bishop_img = pygame.image.load("white_bishop.png").convert_alpha()
rook_img   = pygame.image.load("black_rook.png").convert_alpha()
scale = int(TILE * 0.8)
bishop_img = pygame.transform.smoothscale(bishop_img, (scale, scale))
rook_img   = pygame.transform.smoothscale(rook_img, (scale, scale))

PLAYING = 1
GAME_OVER = 2
state = PLAYING  

def to_xy(square):
    file = square[0]
    rank = int(square[1])
    return FILES.index(file), rank - 1

def xy_to_square(x, y):
    file = FILES[x]
    rank = y + 1
    return f"{file}{rank}"

def draw_piece(img, x, y):
    visual_y = 7 - y
    px = x * TILE + TILE//2
    py = visual_y * TILE + TILE//2
    screen.blit(img, img.get_rect(center=(px, py)))

def draw_board():
    for r in range(8):
        for c in range(8):
            col = LIGHT if (r+c)%2==0 else DARK
            pygame.draw.rect(screen, col, (c*TILE, r*TILE, TILE, TILE))

def bishop_captures(bx, by, rx, ry):
    return abs(bx - rx) == abs(by - ry)

def draw_button(text, x, y, w, h):
    mx, my = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]

    hover = (x < mx < x+w and y < my < y+h)

    # colors
    base_color = (160, 160, 160)
    hover_color = (190, 190, 255)  # slight blue glow
    shadow_color = (90, 90, 90)

    # draw shadow
    pygame.draw.rect(screen, shadow_color, (x+3, y+3, w, h), border_radius=12)

    # draw button with rounded corners + hover color
    pygame.draw.rect(
        screen,
        hover_color if hover else base_color,
        (x, y, w, h),
        border_radius=12
    )

    # draw outline
    pygame.draw.rect(
        screen,
        (50,50,50),
        (x, y, w, h),
        width=2,
        border_radius=12
    )

    # render centered text
    t = bigfont.render(text, True, (0,0,0))
    screen.blit(t, (x + w//2 - t.get_width()//2,
                    y + h//2 - t.get_height()//2))

    # click handler
    if click and hover:
        pygame.time.wait(200)
        return True
    return False

def draw_roll_button():
    return draw_button("ROLL", WIDTH + 45, 260, 170, 60)

# -------- HUD --------
def draw_hud(coin, steps, rounds):
    pygame.draw.rect(screen, (220,220,220), (WIDTH, 0, 250, HEIGHT))

    title = bigfont.render("Game Info", True, (0,0,0))
    screen.blit(title, (WIDTH+50, 20))

    screen.blit(font.render(f"Round: {rounds}", True, (0,0,0)), (WIDTH+20, 80))
    screen.blit(font.render(f"Coin: {coin}", True, (0,0,0)), (WIDTH+20, 120))
    screen.blit(font.render(f"Steps: {steps}", True, (0,0,0)), (WIDTH+20, 160))
    screen.blit(font.render(f"Rook: {rook_square}", True, (0,0,0)), (WIDTH+20, 220))

# -------- ROOK CLASS --------
class Rook:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.queue = []
        self.timer = 0

    def plan_move_right(self, steps):
        for _ in range(steps):
            self.queue.append((1, 0))

    def plan_move_up(self, steps):
        for _ in range(steps):
            self.queue.append((0, 1))

    def update(self, dt):
        MOVE_DELAY = 200
        self.timer += dt

        while self.queue and self.timer >= MOVE_DELAY:
            self.timer -= MOVE_DELAY
            dx, dy = self.queue.pop(0)
            self.x = (self.x + dx) % 8
            self.y = (self.y + dy) % 8

# -------- RESET GAME --------
def reset_game():
    global rook, bishop_x, bishop_y, rounds
    global current_coin, current_steps, rook_square
    global waiting_for_roll, result_text

    bishop_x, bishop_y = to_xy("c3")
    rook = Rook(*to_xy("h1"))

    rounds = 0
    current_coin = ""
    current_steps = 0
    rook_square = "h1"
    waiting_for_roll = True
    result_text = ""

reset_game()

# -------- MAIN LOOP --------
while True:
    dt = clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if state == PLAYING:

        if not rook.queue:
            waiting_for_roll = True

            rook_square = xy_to_square(rook.x, rook.y)

            if bishop_captures(bishop_x, bishop_y, rook.x, rook.y):
                result_text = "BISHOP WINS!"
                state = GAME_OVER

            elif rounds >= 15:
                result_text = "ROOK SURVIVES!"
                state = GAME_OVER

            draw_board()
            draw_piece(bishop_img, bishop_x, bishop_y)
            draw_piece(rook_img, rook.x, rook.y)
            draw_hud(current_coin, current_steps, rounds)

            # ROLL button
            if draw_roll_button():
                waiting_for_roll = False

                current_coin = random.choice(["head","tail"])
                d1 = random.randint(1,6)
                d2 = random.randint(1,6)
                steps = d1 + d2

                current_steps = steps
                rounds += 1

                if current_coin == "head":
                    rook.plan_move_up(steps)
                else:
                    rook.plan_move_right(steps)

            pygame.display.update()
            continue

        # rook animating
        rook.update(dt)

        draw_board()
        draw_piece(bishop_img, bishop_x, bishop_y)
        draw_piece(rook_img, rook.x, rook.y)
        draw_hud(current_coin, current_steps, rounds)

        pygame.display.update()
        continue

    # ---------------- GAME OVER ----------------
    if state == GAME_OVER:

        draw_board()
        draw_piece(bishop_img, bishop_x, bishop_y)
        draw_piece(rook_img, rook.x, rook.y)
        draw_hud(current_coin, current_steps, rounds)

        msg = bigfont.render(result_text, True, (200,20,20))
        screen.blit(msg, (WIDTH//2 - 100, HEIGHT//2 - 100))

        if draw_button("RESTART", WIDTH//2 - 80, HEIGHT//2, 180, 60):
            reset_game()
            state = PLAYING

        pygame.display.update()
