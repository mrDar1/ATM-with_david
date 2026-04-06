# dar UI
# import ui_dar
# ui_dar.ATMApp().run()

# David's UI
from models import Bank
import ui

bank = Bank()
ui.ATMApp(bank).mainloop()
