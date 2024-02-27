import tkinter as tk
import pyqrcode

root = tk.Tk()
root.title("QR Gen")  # Provide Title
root.geometry("300x400")  # Increase the size for better display

# Color Schemes
bg_color = "#f0f0f0"  # Light gray background
text_color = "#333333"  # Dark gray text
button_color = "#4caf50"  # Green button color

root.configure(bg=bg_color)

url_label = tk.Label(root, text="Enter your URL:", bg=bg_color, fg=text_color)  # Provide URL
url_entry = tk.Entry(root, width=30)

def generateQR():
    url = url_entry.get()  # Get URL from entry box
    qr = pyqrcode.create(url, error='H')  # Create a QR code for the given URL with higher error correction
    qr.png("QR.png", scale=8)  # Save the QR code

    qr_image = tk.PhotoImage(file="QR.png")  # Load QR code image into tkinter PhotoImage object

    qr_label = tk.Label(root, image=qr_image, bg=bg_color)  # Display QR code image
    qr_label.image = qr_image  # Keep reference of image to prevent garbage
    qr_label.pack(pady=10)

generate = tk.Button(root, text="Generate", command=generateQR, bg=button_color, fg="white")  # Create a button

# Place widgets in the window
url_label.pack(pady=5)
url_entry.pack(pady=5)
generate.pack(pady=10)

root.mainloop()
