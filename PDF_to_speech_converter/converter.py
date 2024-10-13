import pypdf
import pyttsx3
import threading
import tkinter as tk
from tkinter import filedialog, messagebox


class PDFConverter:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("PDF to Speech Converter")
        self.main_window.geometry("500x500")

        self.pdf_file = None
        self.text = ""
        self.engine = pyttsx3.init()

        # GUI Elements
        self.file_label = tk.Label(self.main_window, text="Select PDF File:")
        self.file_button = tk.Button(self.main_window, text="Browse", command=self.browse_file)
        self.rate_label = tk.Label(self.main_window, text="Speech Rate:")
        self.rate_slider = tk.Scale(self.main_window, from_=100, to=300, orient=tk.HORIZONTAL)
        self.volume_label = tk.Label(self.main_window, text="Volume:")
        self.volume_slider = tk.Scale(self.main_window, from_=0.5, to=1.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.convert_button = tk.Button(self.main_window, text="Convert to Speech", command=self.start_speech_thread)
        self.stop_button = tk.Button(self.main_window, text="Stop Speech", command=self.stop_speech)
        self.create_widgets()

    def create_widgets(self):
        # File selection button
        self.file_label.pack(pady=10)
        self.file_button.pack(pady=10)

        # Speech settings (rate)
        self.rate_label.pack(pady=10)
        self.rate_slider.set(200)  # Default rate
        self.rate_slider.pack(pady=10)

        # Speech settings (volume)
        self.volume_label.pack(pady=10)
        self.volume_slider.set(1.0)  # Default volume
        self.volume_slider.pack(pady=10)

        # Convert and stop buttons
        self.convert_button.pack(pady=20)
        self.stop_button.pack(pady=10)

    def browse_file(self):
        try:
            self.pdf_file = filedialog.askopenfilename(
                filetypes=[("PDF files", "*.pdf")],
                title="Choose a PDF file"
            )
            if self.pdf_file:
                self.file_label.config(text=f"Selected File: {self.pdf_file}")

        except Exception as e:
            messagebox.showerror("Error", f"Error selecting file: {e}")

    def extract_text(self):
        try:
            if not self.pdf_file:
                return

            with open(self.pdf_file, "rb") as file:
                pdf_reader = pypdf.PdfReader(file)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    page_text = page.extract_text()
                    if page_text:
                        self.text += page_text

        except Exception as e:
            messagebox.showerror("Error", f"Error reading PDF file: {e}")
            self.text = ""

    def set_speech_properties(self):
        rate = self.rate_slider.get()
        volume = self.volume_slider.get()

        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def start_speech_thread(self):
        """
        Start the speech conversion in a separate thread.
        """
        if not self.pdf_file:
            messagebox.showerror("Error", "No PDF file selected!")
            return

        self.extract_text()
        if not self.text:
            messagebox.showerror("Error", "No text found in the PDF!")
            return

        self.convert_button.config(state=tk.DISABLED)
        try:
            # Runs the speech conversion in another thread to avoid blocking the GUI
            speech_thread = threading.Thread(target=self.convert_to_speech)
            speech_thread.start()

        except Exception as e:
            messagebox.showerror("Error", f"Error starting speech thread: {e}")
            self.convert_button.config(state=tk.NORMAL)

    def convert_to_speech(self):
        """
        Convert the extracted text to speech (runs in a separate thread).
        """
        self.set_speech_properties()

        try:
            self.engine.say(self.text)
            self.engine.runAndWait()

        except Exception as e:
            messagebox.showerror("Error", f"Error during speech conversion: {e}")

        finally:
            self.convert_button.config(state=tk.NORMAL)

    def stop_speech(self):
        self.engine.stop()
        self.convert_button.config(state=tk.NORMAL)
