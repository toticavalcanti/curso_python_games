import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
canvas = tk.Canvas(frame, width=600, height=400, bg='#aaaaff')
item = canvas.create_rectangle(10,10,100,80, fill='green')
game_object = GameObject(canvas, item) #cria nova instância
print(game_object.get_position())
# [10, 10, 100, 80]
game_object.move(20, -10)
print(game_object.get_position())
# [30, 0, 120, 70]
game_object.delete()