import tkinter
import turtle
import time

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("For Hidayah 💕")
screen.setup(width=800, height=700)
# Mematikan tracer agar animasi perpindahan frame terlihat mulus tanpa delay drawing
screen.tracer(0)

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Colors for the flower petals
petal_colors = ["#FF69B4", "#FF1493", "#FF6B6B", "#FFB6C1", "#FFC0CB"]

def draw_petal(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)
    t.end_fill()

def draw_flower(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw petals
    for i in range(6):
        t.color(petal_colors[i % len(petal_colors)])
        draw_petal(t, size, petal_colors[i % len(petal_colors)])
        t.left(60)
    
    # Draw center
    t.penup()
    t.goto(x, y - size//3)
    t.pendown()
    t.color("#FFD700")
    t.fillcolor("#FFD700")
    t.begin_fill()
    t.circle(size//3)
    t.end_fill()

def draw_stem(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#228B22")
    t.pensize(8)
    t.setheading(270)
    t.forward(200)
    
    # Draw leaves and add "Love You" text
    t.pensize(3)
    # Daun kiri (angle 45) dan daun kanan (angle -45)
    for angle, txt_x, txt_y in [(45, x - 70, y - 90), (-45, x + 35, y - 90)]:
        t.penup()
        t.goto(x, y - 80)
        t.pendown()
        t.setheading(270 + angle)
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.circle(40, 60)
        t.left(120)
        t.circle(40, 60)
        t.end_fill()
        
        # Menulis teks "Love You" di masing-masing daun
        t.penup()
        t.goto(txt_x, txt_y)
        t.color("white")
        t.write("Love You", font=("Arial", 10, "bold"))

def draw_hearts(t, offset=0):
    # Ditambahkan efek offset dinamis untuk membuat jantung terlihat "berdetak/bergerak"
    positions = [(-200, 150 + offset), (200, 150 - offset), (-180, -180 + offset), (180, -180 - offset)]
    for px, py in positions:
        t.penup()
        t.goto(px, py)
        t.pendown()
        t.color("#FF1493")
        t.fillcolor("#FF1493")
        t.begin_fill()
        t.left(50)
        t.forward(20)
        t.circle(10, 200)
        t.right(140)
        t.circle(10, 200)
        t.forward(20)
        t.setheading(0)
        t.end_fill()

def write_message(t, phrase_index):
    # Pesan utama dipindahkan ke ATAS bunga (Y: 200 dan 150)
    # Teks berganti secara berkala berdasarkan phrase_index
    if phrase_index == 0:
        main_text = "I Love You, Hidayah"
        sub_text = "You Make The Best Of Everything ❤️"
    else:
        main_text = "I Love You Veril"
        sub_text = "Forever and Always 💕"

    # Main message (Atas)
    t.penup()
    t.goto(0, 220)
    t.color("#FF69B4")
    t.write(main_text, align="center", font=("Georgia", 28, "bold"))
    
    # Sub message (Atas)
    t.goto(0, 180)
    t.color("#FFB6C1")
    t.write(sub_text, align="center", font=("Georgia", 18, "italic"))
    
    # Sparkle decoration (Sekarang ditaruh di bawah sebagai penyeimbang)
    t.goto(0, -300)
    t.color("#FFD700")
    t.write("✨ 🌸 ✨", align="center", font=("Arial", 24, "normal"))

# --- LOOP ANIMASI UTAMA ---
frame = 0
phrase_index = 0
running = True

# Fungsi untuk menghentikan loop saat jendela ditutup
def close_window():
    global running
    running = False
    try:
        screen.bye()
    except turtle.Terminated:
        pass

# Daftarkan fungsi close pada tombol close bawaan Windows/Mac
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_window)

# Bisa juga ditutup dengan klik layar kiri/kanan bebas
screen.onclick(lambda x, y: close_window())

try:
    while running:
        pen.clear() # Bersihkan frame sebelumnya
        
        # Hitung gerakan naik turun untuk efek animasi bergerak
        offset = round(10 * (frame % 10 if frame % 20 < 10 else 10 - (frame % 10))) / 5
        
        # Berganti teks setiap 30 frame (~ 3 detik)
        if frame % 30 == 0:
            phrase_index = 1 - phrase_index 
            
        # Gambar ulang objek dengan koordinat yang dinamis/diperbarui
        draw_stem(pen, 0, -50)
        draw_flower(pen, 0, 0, 80)
        draw_hearts(pen, offset)
        write_message(pen, phrase_index)
        
        if not running:
            break
            
        screen.update() # Render frame yang baru
        time.sleep(0.1) # Mengatur kecepatan animasi
        frame += 1

except (turtle.Terminated, tkinter.TclError):
    # Menangkap error saat jendela ditutup paksa di tengah jalan agar terminal tetap bersih
    pass