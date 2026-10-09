import time

import pyautogui


def read_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Ingresa un número entero válido.")
            continue

        if value > 0:
            return value
        print("El valor debe ser mayor que cero.")


def read_delay() -> float:
    while True:
        try:
            value = float(input("Pausa entre repeticiones en segundos (mínimo 0.2): "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if value >= 0.2:
            return value
        print("La pausa mínima es de 0.2 segundos.")


def main() -> None:
    repetitions = read_positive_int("¿Cuántas veces hago clic y presiono Enter? ")
    delay = read_delay()

    print(
        "\nColoca el puntero sobre el lugar que quieres pulsar. "
        "La acción comenzará en 3 segundos."
    )
    for remaining in range(3, 0, -1):
        print(f"{remaining}...")
        time.sleep(1)

    click_position = pyautogui.position()
    print(
        f"Usando la posición ({click_position.x}, {click_position.y}). "
        "Puedes mover el mouse a la esquina superior izquierda para detener el bot."
    )

    try:
        for current in range(1, repetitions + 1):
            pyautogui.click(click_position.x, click_position.y)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
            print(f"Acción {current}/{repetitions}")

            if current < repetitions:
                time.sleep(delay)
    except pyautogui.FailSafeException:
        print("\nDetenido por el mecanismo de seguridad de PyAutoGUI.")
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")


if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    main()
