import pygame
import os
import math

currentCwd = os.getcwd()
os.chdir(os.path.join(currentCwd, 'data'))

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.isRunning = True

        # Load car images
        self.carNoWheels = pygame.image.load('carNoWheels.png')
        self.carNoWheels = pygame.transform.scale(self.carNoWheels, [225, 100])
        self.carTurningLeft = pygame.image.load('carTurningLeft.png')
        self.carTurningLeft = pygame.transform.scale(self.carTurningLeft, [225, 100])
        self.carTurningRight = pygame.image.load('carTurningRight.png')
        self.carTurningRight = pygame.transform.scale(self.carTurningRight, [225, 100])


        # Initial car position and state
        self.carImage = self.carNoWheels
        self.carRect = self.carImage.get_rect()
        self.carRect.center = (400, 300)
        self.carSpeed = 3
        self.carAngle = 0  # Initialize angle to 0
        self.turnAngle = 0.01
        self.carX = 400.0
        self.carY = 300.0

    def updateCarImage(self, leftKey, rightKey, forwardKey, backwardKey):
        if forwardKey:
            if leftKey:
                self.carAngle += self.turnAngle
            elif rightKey:
                self.carAngle -= self.turnAngle
            self.carX += self.carSpeed * math.cos(self.carAngle)
            self.carY += self.carSpeed * math.sin(self.carAngle)
            self.carRect.center = (int(self.carX), int(self.carY))

        if leftKey:
            self.carImage = pygame.transform.rotate(self.carTurningLeft, math.degrees(self.carAngle))
        elif rightKey:
            self.carImage = pygame.transform.rotate(self.carTurningRight, math.degrees(self.carAngle))
        else:
            self.carImage = pygame.transform.rotate(self.carNoWheels, math.degrees(self.carAngle))

    def makeBarrier(self, x, y, angle):
        rotatedBarrier = pygame.transform.rotate(self.trafficBarrier, angle)
        rect = rotatedBarrier.get_rect(center=(x, y))
        self.screen.blit(rotatedBarrier, rect.topleft)

    def levelOne(self):
        # Add your logic here
        pass

    def mainLoop(self):
        leftKey = False
        rightKey = False
        forwardKey = False
        backwardKey = False

        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftKey = True
                    elif event.key == pygame.K_RIGHT:
                        rightKey = True
                    elif event.key == pygame.K_UP:
                        forwardKey = True
                    elif event.key == pygame.K_DOWN:
                        backwardKey = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftKey = False
                    elif event.key == pygame.K_RIGHT:
                        rightKey = False
                    elif event.key == pygame.K_UP:
                        forwardKey = False
                    elif event.key == pygame.K_DOWN:
                        backwardKey = False
            self.screen.fill((40, 40, 40))

            # MAIN GAME LOGIC:
            self.updateCarImage(leftKey, rightKey, forwardKey, backwardKey)

            self.screen.blit(self.carImage, self.carRect)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Main()
    game.mainLoop()
