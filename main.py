"""2 options for UI: Figma Design or basic.
right now, beutiful Figma has 2 ready screens,
other than that will jump to basic UI (when press admin zone button)"""

# basic UI
# import ui
# ui.ATMApp().run()

# Figma Design UI
import storage
import figma_ui

bank = storage.load_data()
figma_ui.ATMApp(bank).mainloop()
