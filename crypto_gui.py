import tkinter as tk
from tkinter import messagebox
from utils.crypto_api import fetch_crypto_price
from utils.export_csv import export_to_csv


class CryptoTrackerApp:
    def __init__(self):
        self.root = tk.TK()
        self.root.title("Cryptocurrency Price Tracker")

        tk.Label(self.root, text="Enter Cryptocurrency (eg: Bitcoin, DOGE, ETH):", font=("Helvetica", 12)).pack(pady=10)
        self.crypto_entry = tk.Entry(self.root, width=30, font=("Helvetica", 12))
        self.crypto_entry.pack(pady=5)

        self.fetch_button = tk.Button(self.root, text="Fetch Price", command=self.fetch_price)
        self.fetch_button.pack(pady=10)

        self.result_text = tk.Text(self.root, height=15, width=60, wrap=tk.WORD)
        self.result_text.pack(pady=10)

        self.export_button = tk.Button(self.root, text="Export to CSV", command=self.export_data, state=tk.DISABLED)
        self.export_button.pack(pady=10)

        self.crypto_data = []

        def fetch_price(self):
            crypto_id = self.crypto_entry.get()
            if not crypto_id:
                messagebox.showerror("Error", "Please enter a cryptocurrency name.")
                return
            data = fetch_crypto_price(crypto_id)

            if data:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Cryptocurrency: {data['Cryptocurrency']}\n")
                self.result_text.insert(tk.END, f"Price (USD): {data['Price (USD)']}\n")
                self.result_text.insert(tk.END, f"Market Cap: {data['Market Cap (USD)']}\n")
                self.result_text.insert(tk.END, f"24h Volume (USD) : {data['24h Volume (USD']}\n")
                self.crypto_data.append(data)
                self.export_button.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Error", "Failed to fetch data . Please check the cryptocurrency name.")

        def export_data(self):
            if self.crypto_data:
                export_to_csv(self.crypto_data)
                messagebox.showinfo("Success", "Cryptocurrency data exported to crypto_data.csv")

        def run(self):
            self.root.mainloop()
