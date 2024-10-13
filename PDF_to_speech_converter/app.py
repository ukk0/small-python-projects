import tkinter as tk
from converter import PDFConverter


if __name__ == "__main__":
    main_window = tk.Tk()
    app = PDFConverter(main_window)
    main_window.mainloop()
