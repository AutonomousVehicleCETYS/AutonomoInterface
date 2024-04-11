import pygame


class XboxController:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def read_joystick_axes(self):
        pygame.event.pump()
        # Capturar los valores de las palancas
        left_x_axis = self.joystick.get_axis(0)
        left_y_axis = self.joystick.get_axis(1)
        right_x_axis = self.joystick.get_axis(3)  # El índice puede variar según el control
        right_y_axis = self.joystick.get_axis(4)  # El índice puede variar según el control
        return left_x_axis, left_y_axis, right_x_axis, right_y_axis
