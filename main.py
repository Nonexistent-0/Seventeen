import pygame
import random

swidth = 400
sheight = 600

fps = 30
clock = pygame.time.Clock()

GREEN = (0, 75, 0)
DARK_GREEN = (0, 50, 0)
LIGHT_GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (170, 124, 30)
BROWN = (140, 84, 0)
DARK_BROWN = (100, 44, 0)

cards = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13",
         "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13",
         "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13",
         "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13"]

p1, p2 = [], []
for i in range(26):
    rand = random.choice(cards)
    p1.append(rand)
    cards.remove(rand)
    rand = random.choice(cards)
    p2.append(rand)
    cards.remove(rand)

p1side = ["", "", ""]
p2side = ["", "", ""]
p1hand = ["", "", ""]

for i in range(3):
    temp = random.choice(p1)
    p1.remove(temp)
    p1side[i] = temp

for i in range(3):
    temp = random.choice(p2)
    p2.remove(temp)
    p2side[i] = temp

for i in range(3):
    temp = random.choice(p1)
    p1.remove(temp)
    p1hand[i] = temp    

class Card():
    def __init__(self, symbol, number):
        self.symbol = symbol
        self.number = number

pygame.init()

window = pygame.display.set_mode((swidth, sheight))

p1sc = 0
p2sc = 0

winner = ""

running = True
title = True

font = pygame.font.SysFont("Arial", 30)

play_text = font.render("Play!", True, BLACK)
go_text = font.render("Game End", True, BLACK)
p1st = font.render(f"Player Total: {p1sc}", True, BLACK)
p2st = font.render(f"Computer Total: {p2sc}", True, BLACK)
win_text = font.render(f"{winner} Wins!", True, BLACK)

font = pygame.font.SysFont("Arial", 20)

i1 = font.render("Welcome to Seventeen! This game is played in turns", True, BLACK)
i2 = font.render("between two players. On the first turn, Player 2", True, BLACK)
i3 = font.render("will remove one of Player 1's cards. Then it", True, BLACK)
i4 = font.render("becomes Player 1's turn. Player 1 will place 1 card", True, BLACK)
i5 = font.render("down from their hand and pull a card from the deck.", True, BLACK)
i6 = font.render("They then get to remove 1 of Player 2's cards. Then", True, BLACK)
i7 = font.render("it becomes player 2's turn. This loop repeats until", True, BLACK)
i8 = font.render("the deck runs out of cards. The goal of the game is", True, BLACK)
i9 = font.render("to have the final three cards on your side of the", True, BLACK)
i10 = font.render("table be closer to 17 than your opponent.", True, BLACK)

cl = font.render(f"Cards Left: {len(p1)}", True, BLACK)

turn = "p2-2"

gtext = ""

p1e = -1
p2e = -1

game_over = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if title:
                if swidth/2-70 <= mouse[0] <= swidth/2+70 and sheight/2+100 <= mouse[1] <= sheight/2+140:
                    title = False
            if turn == "p1-1":
                if 25 <= mouse[0] <= 125 and 350 <= mouse[1] <= 486:
                    tempi = 0
                    p1side[p1e] = p1hand[tempi]
                    p1hand[tempi] = random.choice(p1)
                    p1.remove(p1hand[tempi])
                    p1e = -1
                    turn = "p1-2"
                elif 150 <= mouse[0] <= 250 and 350 <= mouse[1] <= 486:
                    tempi = 1
                    p1side[p1e] = p1hand[tempi]
                    p1hand[tempi] = random.choice(p1)
                    p1.remove(p1hand[tempi])
                    p1e = -1
                    turn = "p1-2"
                elif 275 <= mouse[0] <= 375 and 350 <= mouse[1] <= 486:
                    tempi = 2
                    p1side[p1e] = p1hand[tempi]
                    p1hand[tempi] = random.choice(p1)
                    p1.remove(p1hand[tempi])
                    p1e = -1
                    turn = "p1-2"
            elif turn == "p1-2":
                if 25 <= mouse[0] <= 125 and 23 <= mouse[1] <= 159:
                    tempi = 0
                    p2side[tempi] = ""
                    p2e = tempi
                    turn = "p2-1"
                elif 150 <= mouse[0] <= 250 and 23 <= mouse[1] <= 159:
                    tempi = 1
                    p2side[tempi] = ""
                    p2e = tempi
                    turn = "p2-1"
                elif 275 <= mouse[0] <= 375 and 23 <= mouse[1] <= 159 <= 159:
                    tempi = 2
                    p2side[tempi] = ""
                    p2e = tempi
                    turn = "p2-1"
                    
    pygame.draw.rect(window, GREEN, [0, 0, swidth, sheight])
    mouse = pygame.mouse.get_pos()

    if (title):
        if swidth/2-70 <= mouse[0] <= swidth/2+70 and sheight/2+100 <= mouse[1] <= sheight/2+140: 
            pygame.draw.rect(window, LIGHT_GRAY, [swidth/2-70, sheight/2+100, 140, 40])  
        else: 
            pygame.draw.rect(window, WHITE, [swidth/2-70, sheight/2+100, 140, 40])
        window.blit(play_text, (swidth/2-25,sheight/2+100))
        window.blit(i1, (0, 0))
        window.blit(i2, (0, 20))
        window.blit(i3, (0, 40))
        window.blit(i4, (0, 60))
        window.blit(i5, (0, 80))
        window.blit(i6, (0, 100))
        window.blit(i7, (0, 120))
        window.blit(i8, (0, 140))
        window.blit(i9, (0, 160))
        window.blit(i10, (0, 180))
    elif game_over:
        window.blit(go_text, (0, 0))
        p1sc, p2sc = 0, 0
        p1sc += int(p1side[0][1:])
        p1sc += int(p1side[1][1:])
        p1sc += int(p1side[2][1:])
        p2sc += int(p2side[0][1:])
        p2sc += int(p2side[1][1:])
        p2sc += int(p2side[2][1:])
        p1st = font.render(f"Player Total: {p1sc}", True, BLACK)
        p2st = font.render(f"Computer Total: {p2sc}", True, BLACK)
        p1w = abs(17-p1sc)
        p2w = abs(17-p2sc)
        if p1w < p2w:
            winner = "Player"
        elif p2w < p1w:
            winner = "Computer"
        elif p1w == p2w:
            winner = "No One"
        win_text = font.render(f"{winner} Wins!", True, BLACK)
        window.blit(p1st, (0, 200))
        window.blit(p2st, (0, 350))
        window.blit(win_text, (0, 500))
    else:
        pygame.draw.rect(window, BROWN, [0, 329, 400, 171])
        pygame.draw.rect(window, DARK_BROWN, [0, 500, 400, 100])
        pygame.draw.rect(window, DARK_GREEN, [25, 23, 100, 136])
        if 25 <= mouse[0] <= 125 and 23 <= mouse[1] <= 159 and turn == "p1-2": 
            pygame.draw.rect(window, LIGHT_GRAY, [25, 23, 100, 136]) 
        pygame.draw.rect(window, DARK_GREEN, [150, 23, 100, 136])
        if 150 <= mouse[0] <= 250 and 23 <= mouse[1] <= 159 and turn == "p1-2": 
            pygame.draw.rect(window, LIGHT_GRAY, [150, 23, 100, 136]) 
        pygame.draw.rect(window, DARK_GREEN, [275, 23, 100, 136])
        if 275 <= mouse[0] <= 375 and 23 <= mouse[1] <= 159 and turn == "p1-2": 
            pygame.draw.rect(window, LIGHT_GRAY, [275, 23, 100, 136]) 
        pygame.draw.rect(window, DARK_GREEN, [25, 172, 100, 136])
        pygame.draw.rect(window, DARK_GREEN, [150, 172, 100, 136])
        pygame.draw.rect(window, DARK_GREEN, [275, 172, 100, 136])
        pygame.draw.rect(window, LIGHT_BROWN, [25, 350, 100, 136])
        if 25 <= mouse[0] <= 125 and 350 <= mouse[1] <= 486 and turn == "p1-1": 
            pygame.draw.rect(window, LIGHT_GRAY, [25, 350, 100, 136]) 
        pygame.draw.rect(window, LIGHT_BROWN, [150, 350, 100, 136])
        if 150 <= mouse[0] <= 250 and 350 <= mouse[1] <= 486 and turn == "p1-1": 
            pygame.draw.rect(window, LIGHT_GRAY, [150, 350, 100, 136]) 
        pygame.draw.rect(window, LIGHT_BROWN, [275, 350, 100, 136])
        if 275 <= mouse[0] <= 375 and 350 <= mouse[1] <= 486 and turn == "p1-1": 
            pygame.draw.rect(window, LIGHT_GRAY, [275, 350, 100, 136]) 

        cl = font.render(f"Cards Left: {len(p1)}", True, BLACK)
        window.blit(cl, (0, 500))

        for i in range(3):
            if i != p1e:
                img = pygame.image.load(f'Playing Cards\\{p1side[i]}.png')
                img = pygame.transform.scale(img, (128, 128))
                window.blit(img, (9 + 125 * i, 176))

        for i in range(3):
            if i != p2e:
                img = pygame.image.load(f'Playing Cards\\{p2side[i]}.png')
                img = pygame.transform.scale(img, (128, 128))
                window.blit(img, (9 + 125 * i, 27))

        for i in range(3):
            img = pygame.image.load(f'Playing Cards\\{p1hand[i]}.png')
            img = pygame.transform.scale(img, (128, 128))
            window.blit(img, (9 + 125 * i, 354))

        if turn == "p1-1":
            gtext = "Select a card to play."
            gf = font.render(gtext, True, BLACK)
            window.blit(gf, (0, 550))

        elif turn == "p1-2":
            gtext = "Select one of the opponent's cards to remove."
            gf = font.render(gtext, True, BLACK)
            window.blit(gf, (0, 550))

        elif turn == "p2-1":
            gtext = "Other player's turn."
            gf = font.render(gtext, True, BLACK)
            window.blit(gf, (0, 550))
            p2side[p2e] = random.choice(p2)
            p2.remove(p2side[p2e])
            p2e = -1
            turn = "p2-2"
            
        elif turn == "p2-2":
            gtext = "Other player's turn."
            gf = font.render(gtext, True, BLACK)
            window.blit(gf, (0, 550))
            p1e = random.randint(0,2)
            p1side[p1e] = ""
            turn = "p1-1"

    if len(p1) == 0:
        game_over = True
    clock.tick(fps)
    pygame.display.update()
    pygame.draw.rect(window, BLACK, [0, 0, swidth, sheight])