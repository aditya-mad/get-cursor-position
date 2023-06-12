from pynput import mouse


def mouse_coordinates(xcoord, ycoord):
    print(f"({xcoord}, {ycoord})")


with mouse.Listener(on_move=mouse_coordinates) as getcoord:
    getcoord.join()
