import pygame
from pygame.camera import Camera

from pygame.locals import *

class Camera():
    def __init__(self, sizeY, sizeX):
        self.size = (sizeY, sizeX)
        self.device = '/dev/video0'
        self.filename = 'capture.png'

    def capture(self):
        pygame.camera.init()
        pygame.camera.list_cameras()
        camera = pygame.camera.Camera(self.device, self.size)
        camera.start()
        image = camera.get_image()
        pygame.image.save(image, self.filename)
        camera.stop() 

