# Bot de clic, pegar y enviar

Este script hace clic en la posición actual del puntero, pega el contenido del
portapapeles con `Ctrl+V` y presiona Enter para enviar, una cantidad finita de
veces. Copia primero el texto que quieras pegar.

## Uso

1. Instala Python.
2. Instala la dependencia:

   ```powershell
   py -m pip install -r requirements.txt
   ```

3. Inicia el bot:

   ```powershell
   py main.py
   ```

4. Indica el número de repeticiones y la pausa entre ellas.
5. Coloca el puntero sobre el objetivo durante la cuenta regresiva de 3 segundos.

Para detenerlo antes, presiona `Ctrl+C` o mueve el puntero a la esquina superior
izquierda de la pantalla. Revisa que la ventana correcta esté activa antes de
iniciarlo: cada repetición hace clic, pega el contenido del portapapeles y
presiona Enter.
