import tkinter as tk
from tkinter import ttk
import time
from Constraint_enviroments.backtracking import backtracking
from helper import apply_action, get_actions

class BacktrackingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Backtracking Algorithm Visualization")
        self.root.geometry("800x600")
        
        # Frame chính
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Khởi tạo trạng thái ban đầu và mục tiêu
        self.initial_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        
        # Canvas cho trạng thái hiện tại
        self.state_canvas = tk.Canvas(self.main_frame, width=300, height=300, bg='white')
        self.state_canvas.grid(row=0, column=0, padx=10, pady=10)
        
        # Frame cho thông tin
        self.info_frame = ttk.Frame(self.main_frame)
        self.info_frame.grid(row=0, column=1, padx=10, pady=10)
        
        # Label hiển thị thông tin
        self.info_label = ttk.Label(self.info_frame, text="", wraplength=300)
        self.info_label.grid(row=0, column=0, pady=5)
        
        # Nút điều khiển
        self.control_frame = ttk.Frame(self.main_frame)
        self.control_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.start_button = ttk.Button(self.control_frame, text="Start", command=self.start_visualization)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.reset_button = ttk.Button(self.control_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=1, padx=5)
        
        # Biến theo dõi
        self.current_state = self.initial_state.copy()
        self.solution = None
        self.current_step = 0
        self.is_running = False
        self.used_numbers = set()
        self.states_history = []  # Lưu lịch sử các trạng thái
        
        # Vẽ trạng thái ban đầu
        self.draw_state(self.current_state)
        
    def draw_state(self, state):
        self.state_canvas.delete("all")
        cell_size = 100
        for i in range(3):
            for j in range(3):
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                # Vẽ ô với màu khác nhau cho ô đang điền
                if state[i][j] == 0:
                    fill_color = 'lightgray'
                else:
                    fill_color = 'white'
                self.state_canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=fill_color)
                if state[i][j] != 0:
                    self.state_canvas.create_text(
                        x1 + cell_size/2,
                        y1 + cell_size/2,
                        text=str(state[i][j]),
                        font=("Arial", 24)
                    )
    
    def start_visualization(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state="disabled")
            self.states_history = []  # Reset lịch sử
            self.solution, steps, nodes = backtracking(self.initial_state, self.goal_state, self.update_state)
            if self.solution:
                self.current_step = 0
                self.animate_solution()
            else:
                self.info_label.config(text="Không tìm thấy giải pháp!")
                self.is_running = False
                self.start_button.config(state="normal")
    
    def update_state(self, state, action=None):
        """Callback function để cập nhật trạng thái từ thuật toán"""
        self.states_history.append([row[:] for row in state])
        self.current_state = state
        self.draw_state(state)
        self.info_label.config(
            text=f"Đang điền số...\n"
                 f"Trạng thái hiện tại: {state}\n"
                 f"Số đã điền: {len([x for row in state for x in row if x != 0])}/9"
        )
        self.root.update()
        time.sleep(0.5)  # Delay để người dùng có thể theo dõi
    
    def animate_solution(self):
        if self.current_step < len(self.solution):
            action = self.solution[self.current_step]
            self.current_state = apply_action(self.current_state, action)
            self.draw_state(self.current_state)
            self.info_label.config(
                text=f"Bước {self.current_step + 1}/{len(self.solution)}\n"
                     f"Hành động: {action}\n"
                     f"Trạng thái hiện tại: {self.current_state}"
            )
            self.current_step += 1
            self.root.after(1000, self.animate_solution)
        else:
            self.info_label.config(text="Đã hoàn thành!")
            self.is_running = False
            self.start_button.config(state="normal")
    
    def reset(self):
        self.current_state = self.initial_state.copy()
        self.draw_state(self.current_state)
        self.info_label.config(text="")
        self.current_step = 0
        self.is_running = False
        self.start_button.config(state="normal")
        self.used_numbers = set()
        self.states_history = []

def show_backtracking_gui():
    root = tk.Tk()
    app = BacktrackingGUI(root)
    root.mainloop() 