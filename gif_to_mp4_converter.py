import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
import threading
from pathlib import Path
import mimetypes

class ModernGIFToMP4Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF to MP4 Converter")
        self.root.geometry("480x750")
        self.root.resizable(True, True)
        self.root.minsize(480, 750)
        
        self.colors = {
            'primary': '#2563eb',
            'secondary': '#64748b',
            'success': '#10b981',
            'danger': '#ef4444',
            'warning': '#f59e0b',
            'background': '#f8fafc',
            'surface': '#ffffff',
            'text': '#1e293b',
            'text_secondary': '#64748b'
        }
        
        self.root.configure(bg=self.colors['background'])
        
        self.selected_folder = tk.StringVar()
        self.output_folder = tk.StringVar()
        self.conversion_progress = tk.DoubleVar()
        self.status_text = tk.StringVar(value="Select a folder and start the batch conversion")
        
        self.setup_ui()
        
    def setup_ui(self):
        main_container = tk.Frame(self.root, bg=self.colors['background'])
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.create_header(main_container)
        
        content_frame = tk.Frame(main_container, bg=self.colors['surface'], 
                                relief="flat", bd=0)
        content_frame.pack(fill="both", expand=True, pady=(20, 0))
        
        content_padding = tk.Frame(content_frame, bg=self.colors['surface'])
        content_padding.pack(fill="both", expand=True, padx=30, pady=30)
        
        self.create_folder_section(content_padding)
        self.create_output_section(content_padding)
        self.create_progress_section(content_padding)
        self.create_button_section(content_padding)
        self.create_watermark_section(content_padding)
        
    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg=self.colors['background'])
        header_frame.pack(fill="x", pady=(0, 10))
        
        title_frame = tk.Frame(header_frame, bg=self.colors['background'])
        title_frame.pack()
        
        icon_label = tk.Label(title_frame, text="🎬", font=("Arial", 32), 
                             bg=self.colors['background'], fg=self.colors['primary'])
        icon_label.pack()
        
        title_label = tk.Label(title_frame, text="GIF to MP4 Converter", 
                              font=("Segoe UI", 24, "bold"), 
                              bg=self.colors['background'], fg=self.colors['text'])
        title_label.pack(pady=(10, 5))
        
        subtitle_label = tk.Label(title_frame, text="Convert GIFs to MP4 format easily", 
                                 font=("Segoe UI", 12), 
                                 bg=self.colors['background'], fg=self.colors['text_secondary'])
        subtitle_label.pack()
        
    def create_folder_section(self, parent):
        section_frame = tk.Frame(parent, bg=self.colors['surface'])
        section_frame.pack(fill="x", pady=(0, 20))
        
        section_title = tk.Label(section_frame, text="📁 Source Folder", 
                                font=("Segoe UI", 14, "bold"), 
                                bg=self.colors['surface'], fg=self.colors['text'])
        section_title.pack(anchor="w", pady=(0, 10))
        
        folder_frame = tk.Frame(section_frame, bg=self.colors['surface'])
        folder_frame.pack(fill="x")
        
        self.folder_entry = tk.Entry(folder_frame, textvariable=self.selected_folder, 
                                    state="readonly", font=("Segoe UI", 10),
                                    relief="flat", bd=1, highlightthickness=1,
                                    highlightcolor=self.colors['primary'],
                                    highlightbackground="#e2e8f0")
        self.folder_entry.pack(side="left", fill="x", expand=True, ipady=8)
        
        select_button = tk.Button(folder_frame, text="📂 Select Folder", 
                                 command=self.select_folder,
                                 font=("Segoe UI", 10, "bold"),
                                 bg=self.colors['primary'], fg="white",
                                 relief="flat", bd=0, padx=20, pady=8,
                                 cursor="hand2")
        select_button.pack(side="right", padx=(10, 0))
        
    def create_output_section(self, parent):
        section_frame = tk.Frame(parent, bg=self.colors['surface'])
        section_frame.pack(fill="x", pady=(0, 20))
        
        section_title = tk.Label(section_frame, text="📤 Output Folder", 
                                font=("Segoe UI", 14, "bold"), 
                                bg=self.colors['surface'], fg=self.colors['text'])
        section_title.pack(anchor="w", pady=(0, 10))
        
        output_frame = tk.Frame(section_frame, bg=self.colors['surface'])
        output_frame.pack(fill="x")
        
        self.output_entry = tk.Entry(output_frame, textvariable=self.output_folder, 
                                   state="readonly", font=("Segoe UI", 10),
                                   relief="flat", bd=1, highlightthickness=1,
                                   highlightcolor=self.colors['primary'],
                                   highlightbackground="#e2e8f0")
        self.output_entry.pack(fill="x", ipady=8)
        
    def create_progress_section(self, parent):
        section_frame = tk.Frame(parent, bg=self.colors['surface'])
        section_frame.pack(fill="x", pady=(0, 20))
        
        section_title = tk.Label(section_frame, text="📊 Progress", 
                                font=("Segoe UI", 14, "bold"), 
                                bg=self.colors['surface'], fg=self.colors['text'])
        section_title.pack(anchor="w", pady=(0, 10))
        
        progress_container = tk.Frame(section_frame, bg=self.colors['surface'])
        progress_container.pack(fill="x")
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Modern.Horizontal.TProgressbar",
                       troughcolor=self.colors['background'],
                       background=self.colors['success'],
                       bordercolor=self.colors['background'],
                       lightcolor=self.colors['success'],
                       darkcolor=self.colors['success'])
        
        self.progress_bar = ttk.Progressbar(progress_container, 
                                          variable=self.conversion_progress,
                                          maximum=100, length=400,
                                          style="Modern.Horizontal.TProgressbar")
        self.progress_bar.pack(fill="x", pady=(0, 10))
        
        self.status_label = tk.Label(progress_container, textvariable=self.status_text, 
                                   wraplength=500, justify="left",
                                   font=("Segoe UI", 10),
                                   bg=self.colors['surface'], fg=self.colors['text_secondary'])
        self.status_label.pack(anchor="w")
        
    def create_button_section(self, parent):
        button_frame = tk.Frame(parent, bg=self.colors['surface'])
        button_frame.pack(fill="x", pady=(30, 0))
        
        center_frame = tk.Frame(button_frame, bg=self.colors['surface'])
        center_frame.pack(expand=True)
        
        left_frame = tk.Frame(center_frame, bg=self.colors['surface'])
        left_frame.pack(side="left", padx=(0, 20))
        
        self.convert_button = tk.Button(left_frame, text="🚀 Start Conversion", 
                                       command=self.start_conversion,
                                       font=("Segoe UI", 12, "bold"),
                                       bg=self.colors['success'], fg="white",
                                       relief="flat", bd=0, padx=30, pady=12,
                                       cursor="hand2")
        self.convert_button.pack()
        
        right_frame = tk.Frame(center_frame, bg=self.colors['surface'])
        right_frame.pack(side="left", padx=(20, 0))
        
        exit_button = tk.Button(right_frame, text="❌ Exit", 
                               command=self.root.quit,
                               font=("Segoe UI", 12),
                               bg=self.colors['danger'], fg="white",
                               relief="flat", bd=0, padx=20, pady=12,
                               cursor="hand2")
        exit_button.pack()
        
    def create_watermark_section(self, parent):
        watermark_frame = tk.Frame(parent, bg=self.colors['surface'])
        watermark_frame.pack(fill="x", pady=(20, 0))
        
        watermark_label = tk.Label(watermark_frame, text="Made by ErgoSoft", 
                                  font=("Segoe UI", 10, "italic"), 
                                  bg=self.colors['surface'], fg=self.colors['text_secondary'])
        watermark_label.pack(anchor="w")
        
    def select_folder(self):
        folder = filedialog.askdirectory(title="Select the folder where the files are located")
        if folder:
            self.selected_folder.set(folder)
            output_path = os.path.join(folder, "Outputs")
            self.output_folder.set(output_path)
            self.status_text.set(f"✅ Selected folder: {folder}")
            
    def get_supported_files(self, folder):
        supported_files = []
        file_type = "all"
        
        print(f"\n🔍 Scanning folder: {folder}")
        print(f"📁 Selected file type: {file_type}")
        print("=" * 50)
        
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                file_ext = file.lower()
                
                if file_ext.endswith('.gif'):
                    print(f"✅ GIF file found: {file}")
                    supported_files.append(file)
        
        print("=" * 50)
        print(f"📊 Total supported files: {len(supported_files)}")
        print(f"🎬 GIF files: {sum(1 for f in supported_files if f.lower().endswith('.gif'))}")
        print()
        
        return supported_files
    
    def start_conversion(self):
        if not self.selected_folder.get():
            messagebox.showerror("Error", "Please select a folder first!")
            return
            
        conversion_thread = threading.Thread(target=self.convert_files)
        conversion_thread.daemon = True
        conversion_thread.start()
        
    def convert_files(self):
        try:
            input_folder = self.selected_folder.get()
            output_folder = self.output_folder.get()
            
            os.makedirs(output_folder, exist_ok=True)
            
            supported_files = self.get_supported_files(input_folder)
            
            if not supported_files:
                self.status_text.set("❌ No GIF files found in the selected folder!")
                return
                
            gif_count = sum(1 for f in supported_files if f.lower().endswith('.gif'))
            
            status_msg = f"🔍 Found {gif_count} GIF files. Starting conversion..."
            
            self.status_text.set(status_msg)
            self.convert_button.config(state="disabled", text="⏳ Converting...")
            
            for i, file in enumerate(supported_files):
                input_path = os.path.join(input_folder, file)
                output_filename = os.path.splitext(file)[0] + ".mp4"
                output_path = os.path.join(output_folder, output_filename)
                
                self.status_text.set(f"🔄 Converting GIF: {file} ({i+1}/{len(supported_files)})")
                cmd = [
                    "ffmpeg", "-i", input_path,
                    "-c:v", "libx264",
                    "-pix_fmt", "yuv420p",
                    "-preset", "medium",
                    "-crf", "23",
                    "-y",
                    output_path
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode != 0:
                    print(f"❌ FFmpeg error ({file}): {result.stderr}")
                    
                    print(f"🔄 Trying alternative command: {file}")
                    alt_cmd = [
                        "ffmpeg", "-i", input_path,
                        "-c:v", "libx264",
                        "-pix_fmt", "yuv420p",
                        "-vf", "scale=iw:ih:flags=lanczos",
                        "-y",
                        output_path
                    ]
                    
                    alt_result = subprocess.run(alt_cmd, capture_output=True, text=True)
                    
                    if alt_result.returncode != 0:
                        print(f"❌ Alternative command failed ({file}): {alt_result.stderr}")
                        self.status_text.set(f"❌ Error: {file} could not be converted!")
                        continue
                    else:
                        print(f"✅ Alternative command successful: {file}")
                
                if os.path.exists(output_path):
                    file_size = os.path.getsize(output_path)
                    if file_size == 0:
                        print(f"⚠️ 0 byte file created: {output_filename}")
                        
                        print(f"🔄 Last attempt - simple command: {file}")
                        simple_cmd = [
                            "ffmpeg", "-i", input_path,
                            "-c:v", "libx264",
                            "-y",
                            output_path
                        ]
                        
                        simple_result = subprocess.run(simple_cmd, capture_output=True, text=True)
                        
                        if simple_result.returncode == 0:
                            file_size = os.path.getsize(output_path)
                            if file_size > 0:
                                print(f"✅ Simple command successful: {file} → {output_filename} ({file_size} bytes)")
                            else:
                                print(f"❌ Simple command created a 0 byte file: {file}")
                                self.status_text.set(f"⚠️ Warning: {file} created a 0 byte file!")
                                try:
                                    os.remove(output_path)
                                    print(f"🗑️ 0 byte file deleted: {output_filename}")
                                except:
                                    pass
                                continue
                        else:
                            print(f"❌ Simple command failed: {file}")
                            self.status_text.set(f"⚠️ Warning: {file} created a 0 byte file!")
                            try:
                                os.remove(output_path)
                                print(f"🗑️ 0 byte file deleted: {output_filename}")
                            except:
                                pass
                            continue
                    else:
                        print(f"✅ Success: {file} → {output_filename} ({file_size} bytes)")
                else:
                    print(f"❌ Output file not created: {output_filename}")
                    self.status_text.set(f"❌ Error: {file} output file not created!")
                    continue
                
                progress = ((i + 1) / len(supported_files)) * 100
                self.conversion_progress.set(progress)
                
            success_msg = f"✅ GIF conversion completed! {gif_count} files successfully converted."
            
            self.status_text.set(success_msg)
            self.convert_button.config(state="normal", text="🚀 Start Conversion")
            
            messagebox.showinfo("🎉 Completed", 
                              f"{len(supported_files)} files successfully converted to MP4 format!\n"
                              f"📁 Output folder: {output_folder}")
                              
        except Exception as e:
            self.status_text.set(f"❌ Error occurred: {str(e)}")
            self.convert_button.config(state="normal", text="🚀 Start Conversion")
            messagebox.showerror("Error", f"An error occurred during conversion:\n{str(e)}")

def check_ffmpeg():
    try:
        result = subprocess.run(["ffmpeg", "-version"], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def main():
    if not check_ffmpeg():
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("FFmpeg required", 
                           "This program requires FFmpeg.\n\n"
                           "You can install FFmpeg using the following steps:\n"
                           "1. Go to https://ffmpeg.org/download.html\n"
                           "2. Download FFmpeg for Windows\n"
                           "3. Extract the downloaded file\n"
                           "4. Add the bin folder to your system PATH\n"
                           "5. Restart the program")
        return
    
    root = tk.Tk()
    app = ModernGIFToMP4Converter(root)
    root.mainloop()

if __name__ == "__main__":
    main() 