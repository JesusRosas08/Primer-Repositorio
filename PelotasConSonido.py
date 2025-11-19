import os
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading

try:
    from playsound import playsound
except ImportError:
    from playsound3 import playsound  # type: ignore

# Carpeta base del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class AnimatedGif(tk.Label):
    """Widget que muestra un GIF animado repitiéndose en bucle."""
    def __init__(self, master, gif_path: str, delay: int = 80):
        image = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(image)]
        self.delay = delay
        self.idx = 0
        super().__init__(master, image=self.frames[0], bg="white")
        self.after(self.delay, self._animate)

    def _animate(self):
        self.idx = (self.idx + 1) % len(self.frames)
        self.configure(image=self.frames[self.idx])
        self.after(self.delay, self._animate)

def play_sound(sound_path: str):
    """Reproduce sonido en un hilo para no bloquear la GUI."""
    threading.Thread(target=playsound, args=(sound_path,), daemon=True).start()

def main():
    root = tk.Tk()
    root.title('Animación con sonido – Tkinter')
    root.geometry('500x400')
    root.configure(bg="white")

    # Rutas de archivos
    gif1_path = os.path.join(BASE_DIR, 'animation.gif')
    gif2_path = os.path.join(BASE_DIR, 'animation2.gif')
    sound_path = os.path.join(BASE_DIR, 'boing.wav')

    # Primer GIF
    gif1 = AnimatedGif(root, gif1_path, delay=80)
    gif1.place(x=80, y=100)

    # Segundo GIF
    gif2 = AnimatedGif(root, gif2_path, delay=80)
    gif2.place(x=300, y=100)

    # Botón de sonido
    tk.Button(
        root,
        text='Reproducir sonido',
        command=lambda: play_sound(sound_path),
        font=('Arial', 12, 'bold'),
        padx=10,
        pady=5,
        bg="#4CAF50",
        fg="white"
    ).pack(pady=20, side="bottom")

    root.mainloop()

if __name__ == '__main__':
    main()
