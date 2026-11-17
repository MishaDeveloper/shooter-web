import asyncio
import pygame
from game import Game


async def main():
    pygame.init()

    game = Game()
    await game.run()

    pygame.quit()


asyncio.run(main())