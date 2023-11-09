from pynput import mouse

def on_click(x, y, button, pressed):
    if not pressed:
        # Stop the listener and return the mouse coordinates
        listener.stop()
        print(f"Coordinates: x={x}, y={y}")

print("Move the mouse cursor to the desired position...")

# Create a mouse listener
listener = mouse.Listener(on_click=on_click)
listener.start()

try:
    # Keep the script running until the mouse position is obtained
    while listener.running:
        pass
except KeyboardInterrupt:
    pass

