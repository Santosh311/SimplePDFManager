from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog, Button
from pdf_info import getPDFInfo
from merge_pdf import merge_pdfs
from split_pdf import split_pdf
from extract_pdf import extract_page
from rotate_pdf import rotate_pages
from encrypt_pdf import encrypt_pdf

def gui():
    root = Tk()
    root.title("Simple PDF Manager")
    root.state('zoomed')
    root.geometry("300x300")
    root['bg'] = "green"

    bg = Image.open("D:\Python_Course\PDFConverter\img.jpeg")
    resized_image = bg.resize((1920, 1080), Image.ANTIALIAS)
    canvas1 = Canvas(root, width=300, height=300)
    new_image = ImageTk.PhotoImage(resized_image)

    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=new_image, anchor="nw")

    def about():
        pdf = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                         filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        info = getPDFInfo(pdf)
        top = Toplevel(root)
        top.geometry("900x300")
        root.eval(f'tk::PlaceWindow {str(top)} center')
        label1 = Label(top, text=info, padx=10, pady=10, font=("Times New Roman", 12, "bold"))
        label1.pack(pady=10)

        def exit_popup():
            messagebox.showinfo(title="Success Message", message="File Info Displayed Succesfully")
            top.destroy()
            top.update()

        btn = Button(top, text="Exit", padx=5, pady=5, command=exit_popup)
        btn.pack()

    def merge():
        pdfs_open = filedialog.askopenfilenames(initialdir="/", title="Select A File",
                                                filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        merge_list = list(pdfs_open)
        pdfs_save = filedialog.asksaveasfilename(initialdir="/", title="Select A File",
                                                 filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        merge_pdfs(merge_list, pdfs_save)
        messagebox.showinfo(title="Success Message", message="PDFs Merged Succesfully")

    def split():
        pdf_split = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                               filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        pdfs_save = pdf_split.split(".")[0]
        n = IntVar()
        top = Toplevel(root)
        top.geometry("300x100")
        root.eval(f'tk::PlaceWindow {str(top)} center')
        label1 = Label(top, text="Enter page to split at", padx=10, pady=10)
        label1.pack()
        e1 = Entry(top, width=15, textvariable=n)
        e1.pack()

        def call_split_fun(pdf_path, pdf_save_path):
            num = int(n.get())
            split_pdf(pdf_path, num, pdf_save_path)
            messagebox.showinfo(title="Success Message", message="PDF Split Succesfully")
            top.destroy()
            top.update()

        btn = Button(top, text="OK", padx=7, pady=7, command=lambda: call_split_fun(pdf_split, pdfs_save))
        btn.pack()

    def extract():
        pdf_extract = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                 filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        page_no = IntVar()
        top = Toplevel(root)
        top.geometry("300x100")
        root.eval(f'tk::PlaceWindow {str(top)} center')
        label1 = Label(top, text="Enter page no to extract", padx=10, pady=10)
        label1.pack()
        e1 = Entry(top, width=15, textvariable=page_no)
        e1.pack()

        def call_extract_fun(pdf_path):
            num = int(page_no.get())
            extract_page(pdf_path, num)
            messagebox.showinfo(title="Success Message", message="Page Extracted Succesfully")
            top.destroy()
            top.update()

        btn = Button(top, text="OK", padx=7, pady=7, command=lambda: call_extract_fun(pdf_extract))
        btn.pack()

    def rotate():
        pdf_rotate = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        direction = StringVar()
        top = Toplevel(root)
        top.geometry("500x200")
        root.eval(f'tk::PlaceWindow {str(top)} center')
        label1 = Label(top, text="Enter direction to specify", padx=10, pady=10)
        label1.pack()

        def onClick(*args):
            e1.delete(0, 'end')

        e1 = Entry(top, width=60, textvariable=direction)
        e1.insert(0, "Enter clockwise, counter clockwise or upside down only")
        e1.pack()
        e1.bind("<Button-1>", onClick)

        def call_rotate_fun(pdf_path):
            d = str(direction.get())
            rotate_pages(pdf_path, d)
            messagebox.showinfo(title="Success Message", message="PDF Rotated Succesfully")
            top.destroy()
            top.update()

        btn = Button(top, text="OK", padx=7, pady=7, command=lambda: call_rotate_fun(pdf_rotate))
        btn.pack(pady=20)

    def encrypt():
        pdf_encrypt = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                 filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        password = StringVar()
        top = Toplevel(root)
        top.geometry("300x100")
        root.eval(f'tk::PlaceWindow {str(top)} center')
        label1 = Label(top, text="Enter password", padx=10, pady=10)
        label1.pack()

        e1 = Entry(top, width=10, textvariable=password)
        e1.pack()

        def call_encrypt_fun(pdf_path):
            p = str(password.get())
            encrypt_pdf(pdf_path, p)
            messagebox.showinfo(title="Success Message", message="PDF Encrypted Succesfully")
            top.destroy()
            top.update()

        btn = Button(top, text="OK", padx=7, pady=7, command=lambda: call_encrypt_fun(pdf_encrypt))
        btn.pack()

    b1 = Button(root, text="About PDF", command=about, width=50, height=2, borderwidth=3, bg="#51ECCA",
                font=("Consolas", 15, "bold"))
    b2 = Button(root, text="Merge PDFs", command=merge, width=50, height=2, borderwidth=3, bg="#51ECCA",
                font=("Consolas", 15, "bold"))
    b3 = Button(root, text="Split PDF", command=split, width=50, height=2, borderwidth=3, bg="#51ECCA",
                font=("Consolas", 15, "bold"))
    b4 = Button(root, text="Extract Single Page from PDF", command=extract, width=50, height=2, bg="#51ECCA",
                borderwidth=3, font=("Consolas", 15, "bold"))
    b5 = Button(root, text="Rotate PDF", command=rotate, width=50, height=2, borderwidth=3, bg="#51ECCA",
                font=("Consolas", 15, "bold"))
    b6 = Button(root, text="Encrypt PDF with password", command=encrypt, width=50, height=2, bg="#51ECCA",
                borderwidth=3, font=("Consolas", 15, "bold"))

    button1_canvas = canvas1.create_window(200, 20, anchor="nw", window=b1)
    button2_canvas = canvas1.create_window(200, 70, anchor="nw", window=b2)
    button3_canvas = canvas1.create_window(200, 120, anchor="nw", window=b3)
    button4_canvas = canvas1.create_window(200, 170, anchor="nw", window=b4)
    button5_canvas = canvas1.create_window(200, 220, anchor="nw", window=b5)
    button6_canvas = canvas1.create_window(200, 270, anchor="nw", window=b6)

    b1.place(relx=0.5, rely=0.15, anchor=CENTER)
    b2.place(relx=0.5, rely=0.30, anchor=CENTER)
    b3.place(relx=0.5, rely=0.45, anchor=CENTER)
    b4.place(relx=0.5, rely=0.60, anchor=CENTER)
    b5.place(relx=0.5, rely=0.75, anchor=CENTER)
    b6.place(relx=0.5, rely=0.90, anchor=CENTER)

    root.mainloop()

def main():
    gui()

if __name__ == '__main__':
    main()

