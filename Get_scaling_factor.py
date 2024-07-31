import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import math
def get_even_or_lower_even(n):
    if n % 2 == 0:
        return n
    else:
        return n - 1

class ImagePixelPositionApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Image Pixel Position App")
        
        self.reference_path = filedialog.askopenfilename(title="Select a reference file")
        
        self.image_path = filedialog.askopenfilename(title="Select an image file")

        self.image = Image.open(self.image_path)
        self.reference = Image.open(self.reference_path)
        self.img_tk = ImageTk.PhotoImage(self.image)
        self.ref_tk = ImageTk.PhotoImage(self.reference)
        
        self.img_canvas = tk.Canvas(root, width=self.image.width, height=self.image.height)
        self.ref_canvas = tk.Canvas(root, width=self.reference.width, height=self.reference.height)
        self.ref_canvas.grid(row=0, column=0, padx=5, pady=5, sticky="nw")
        self.img_canvas.grid(row=0, column=1, padx=5, pady=5, sticky="nw")
        
        self.ref_canvas.create_image(0, 0, anchor=tk.NW, image=self.ref_tk)
        self.img_canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
        
        self.img_label = tk.Label(root, text="Mouse Position on image: ")
        self.img_label.grid(row=1, column=1, padx=5, pady=5, sticky="nw")
        
        self.ref_label = tk.Label(root, text="Mouse Position on reference: ")
        self.ref_label.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        
        self.img_positions = []
        self.img_pos_count = 0
        self.ref_positions = []
        self.ref_pos_count = 0
        
        self.img_canvas.bind("<Motion>", self.img_mouse_move)
        self.img_canvas.bind("<Double-1>", self.save_img_position)
        
        self.ref_canvas.bind("<Motion>", self.ref_mouse_move)
        self.ref_canvas.bind("<Double-1>", self.save_ref_position)
        
        self.calc_button = tk.Button(root, text="Calculate scaling factor", command=self.calc_fact)
        self.calc_button.grid(row=1, column=2, padx=5, pady=5, sticky="nw")
        
    def img_mouse_move(self, event):
        self.img_label.config(text=f"Mouse Position: {event.x}, {event.y}")
        
    def ref_mouse_move(self, event):
        self.ref_label.config(text=f"Mouse Position: {event.x}, {event.y}")    
    
    def save_img_position(self, event):
        x, y = event.x, event.y
        self.img_positions.append((x, y))
        self.img_pos_count = self.img_pos_count + 1
        print(f"Saved position (N°{self.img_pos_count}) in image: {x}, {y}")
        
        # Save to file
        k=1
        with open("Positions in image.txt", "w") as file:
            for pos in self.img_positions:
                file.write(f"N°{k}: {pos[0]}, {pos[1]}\n")
                k=k+1
                
    def save_ref_position(self, event):
        x, y = event.x, event.y
        self.ref_positions.append((x, y))
        self.ref_pos_count = self.ref_pos_count + 1
        print(f"Saved position (N°{self.ref_pos_count}) in reference: {x}, {y}")
        
        # Save to file
        k=1
        with open("Positions in reference.txt", "w") as file:
            for pos in self.ref_positions:
                file.write(f"N°{k}: {pos[0]}, {pos[1]}\n")
                k=k+1
                
    def calc_fact(self):
        if len(self.img_positions) < 2 or len(self.ref_positions) < 2:
            messagebox.showwarning("Warning", "Not enough positions saved to calculate distances.")
            return
        
        abc = min(len(self.img_positions),len(self.ref_positions))
        print(abc)
        
        bcd = get_even_or_lower_even(abc)
        print(bcd)
        
        mean_ratio = 0
        k=0
        # Euclidean distances between pairs of saved positions
        for i in range(bcd):
            
            if i % 2 == 0:
                
                x1, y1 = self.img_positions[i]
                x2, y2 = self.img_positions[i+1]
                
                img_dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                
                x1, y1 = self.ref_positions[i]
                x2, y2 = self.ref_positions[i+1]
                
                ref_dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                
                ratio = ref_dist/img_dist
                
                print(i,ref_dist,img_dist,ratio)
                
                k=k+1
                mean_ratio = mean_ratio + ratio
                
        mean_ratio = mean_ratio/k
        print("Mean ratio", mean_ratio)
        messagebox.showinfo("Mean ratio", mean_ratio)
        
        # # Euclidean distances between each consecutive pair of saved positions
        # img_distances = []
        # for i in range(1, len(self.img_positions)):
        #     x1, y1 = self.img_positions[i - 1]
        #     x2, y2 = self.img_positions[i]
        #     distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        #     img_distances.append(distance)
        # ref_distances = []
        # for i in range(1, len(self.ref_positions)):
        #     x1, y1 = self.ref_positions[i - 1]
        #     x2, y2 = self.ref_positions[i]
        #     distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        #     ref_distances.append(distance)
        
        # # Display the distances
        # distances_str = "\n".join([f"Distance {i} in image: {dist:.2f}" for i, dist in enumerate(img_distances, start=1)])
        # messagebox.showinfo("Distances", distances_str)
        # print("Distances calculated:")
        # print(distances_str)               
               
if __name__ == "__main__":
    root = tk.Tk()
    app = ImagePixelPositionApp(root)
    root.mainloop()
