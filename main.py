from xbox_controller_handler import XboxController
import time


def main():
    controller = XboxController()

    try:
        while True:
            left_x, left_y, right_x, right_y = controller.read_joystick_axes()
            print(
                f"Palanca izquierda: X={left_x:.2f}, Y={left_y:.2f} | Palanca derecha: X={right_x:.2f}, Y={right_y:.2f}")
            # Esperar un poco antes de la próxima lectura para no saturar la consola
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Programa terminado.")
        pygame.quit()


if __name__ == "__main__":
    main()
