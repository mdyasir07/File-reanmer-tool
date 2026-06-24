import tkinter as tk
from tkinter import filedialog, messagebox
from app_logic import update_suffix

APP_ICON_PATH="C:\Users\moyasir\Desktop\rename-tool\Suffix_Renamer.ico"
class SuffixRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" File Renamer Toolkit(Suffix)")
        self.root.geometry("500x400")

        if APP_ICON_PATH and os.path.exists(APP_ICON_PATH):
            try:
                self.iconbitmap(APP_ICON_PATH)
            except Exception:
                pass

        self.folder_path = tk.StringVar()
        self.old_suffix = tk.StringVar()
        self.new_suffix = tk.StringVar()
        self.case_sensitive = tk.BooleanVar(value=False)
        self.include_subfolders = tk.BooleanVar(value=True)

        self.preview_results = []

        self.create_ui()
        self.configure_grid()
        

    def create_ui(self):

        options_frame = tk.Frame(self.root)
        options_frame.grid(row=3, column=0, columnspan=3, sticky="w", padx=5, pady=5)


        #FR-P-01/02/03:BROWSE BUTTON AND ENTRY
        tk.Label(self.root, text="Folder:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.folder_path, width=40).grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        tk.Button (self.root, text="Browse", command=self.browse).grid(row=0, column=2, padx=5, pady=5)
        
        #FR-S-01:OLD SUFFIX
        tk.Label(self.root, text="Old Suffix:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.old_suffix).grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
        
        #FR-S-02:NEW SUFFIX
        tk.Label(self.root, text="New Suffix:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.new_suffix).grid(row=2, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
       
        #FR-S-04:CASE SENSITIVE 
        tk.Checkbutton(options_frame, text="Case Sensitive", variable=self.case_sensitive).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        #FR-P-08:INCLUDE SUBFOLDERS CHECKBOX
        tk.Checkbutton(options_frame, text="Include Subfolders", variable=self.include_subfolders).grid(row=0, column=1, sticky="w", padx=5, pady=5)
 
        
        #FR-P-11/15:PREVIEW AND EXECUTE BUTTONS
        tk.Button(self.root, text="Preview", command=self.preview).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Execute", command=self.execute).grid(row=4, column=1, padx=5, pady=5)
       
        #FR-P-20:LOG AREA
        tk.Label(self.root, text="Log Box:").grid(row=5, column=0, sticky="e", padx=5, pady=0)
        self.log_area=tk.Text(self.root, height=10)
        self.log_area.grid(row=6, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
        self.log_area.configure(state="disabled")
   
    def configure_grid(self):
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(6, weight=1)
    
    #FR-P-1:BROWSE FOLDER
    def browse(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)
    
    #FR-P-21:CLEAR LOG AREA
    def preview(self):
        self.log_area.config(state="normal")
        self.log_area.delete(1.0, tk.END)
        self.log_area.config(state="disabled")
        if not self.folder_path.get():
            messagebox.showerror("Error", "Please select a folder.")
            return
         
        #FR-S-03:ERROR CHECK FOR EMPTY OLD SUFFIX
        if not self.old_suffix.get():
            messagebox.showerror("Error", "the old suffix should not be empty.")
            return
        if not self.new_suffix.get():
            messagebox.showerror("Error","Enter the new suffix")
            return
       
       #FR-P-11:PREVIEW WITHOUT MODIYING FILES
        self.preview_results = update_suffix(
            folder=self.folder_path.get(),
            old_suffix=self.old_suffix.get(),
            new_suffix=self.new_suffix.get(),
            case_sensitive=self.case_sensitive.get(),
            include_subfolders=self.include_subfolders.get(),
    
            execute=False
        )

        #FR-P-14:MESSAGE IF NO FILES FOUND
        if not self.preview_results:
            self.log_area.insert(tk.END, "No files found with the specified old suffix.")
            return
        
        #FR-P-12:SHOW OLD TO NEW FILE NAME
        for old, new, _, _ in self.preview_results:
            self.log(f"{old} -> {new}")

        #FR-P-13:SHOW TOTAL FILES TO BE RENAMED    
        self.log(f"\nTotal files: {len(self.preview_results)}")
    
    def execute(self):
        self.log_area.config(state="normal")
        self.log_area.delete(1.0, tk.END)
        self.log_area.config(state="disabled")
        if not self.folder_path.get():
            messagebox.showerror("Error", "Please select a folder.")
            return
        if not self.old_suffix.get():
            messagebox.showerror("Error", "the old suffix should not be empty.")
            return
        if not self.new_suffix.get():
            messagebox.showerror("Error","Enter the new suffix")
            return
        
        results = update_suffix(
            folder=self.folder_path.get(), 
            old_suffix=self.old_suffix.get(),
            new_suffix=self.new_suffix.get(),
            case_sensitive=self.case_sensitive.get(),
            include_subfolders=self.include_subfolders.get(),
            execute=True
        )
        sucess=0
        failure=0
        for old,new,status,error in results:

            #FR-P-16:LOG SUCCESSFUL RENAME
            if status:
                self.log(f"{old} -> {new}")
                sucess+=1
           
                #FR-P-17:LOG FAILED RENAME WITH ERROR
            else:
                self.log(f"Failed to rename {old}: {error}")
                failure+=1
        
        #FR-P-18:SHOW SUMMARY OF RENAME OPERATION
        self.log(f"\nTotal files: {len(results)}, Success: {sucess}, Failure: {failure}")
    
    
    def log(self,message):
        #FR-P-20/22:APPEND LOG MESSAGE AND AUTO-SCROLL
        self.log_area.config(state="normal")
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
        self.log_area.config(state="disabled")
    
def run_suffix_app():
    root = tk.Tk()
    app = SuffixRenamerApp(root)
    root.mainloop()

