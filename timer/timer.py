import tkinter as tk

class StopwatchApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Stopwatch Timer")
        self.running = False
        self.time_elapsed = 0  # in seconds
        self.timer_id = None

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_stop_button = tk.Button(root, text="Start", font=("Helvetica", 14), width=10, command=self.toggle)
        self.start_stop_button.pack(side="left", padx=20, pady=10)

        self.reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), width=10, command=self.reset)
        self.reset_button.pack(side="right", padx=20, pady=10)

    def update_timer(self):
        if self.running:
            self.time_elapsed += 1
            self.time_label.config(text=self.format_time(self.time_elapsed))
            self.timer_id = self.root.after(1000, self.update_timer)

    def format_time(self, seconds: int) -> str:
        hrs = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hrs:02}:{mins:02}:{secs:02}"

    def toggle(self):
        if not self.running:
            self.running = True
            self.start_stop_button.config(text="Stop")
            self.update_timer()
        else:
            self.running = False
            self.start_stop_button.config(text="Start")
            if self.timer_id:
                self.root.after_cancel(self.timer_id)

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.time_label.config(text="00:00:00")
        self.start_stop_button.config(text="Start")
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
