from MVC.controller import MinesweeperController
from MVC.model import MinesweeperModel
from MVC.view import MinesweeperView

model = MinesweeperModel()
controller = MinesweeperController(model)
view = MinesweeperView(model, controller)
view.pack()
view.mainloop()