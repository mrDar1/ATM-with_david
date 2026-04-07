"""2 options for UI: Figma Design or basic, uncomment your choice and comment the other one"""
# Regular UI
# import ui
# ui.ATMApp().run()

# Figma Design UI
import storage
import figma_ui

bank = storage.load_data()
figma_ui.ATMApp(bank).mainloop()
