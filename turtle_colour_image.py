import cv2
import numpy as np
import turtle

IMAGE = "905292.png"

SCALE = 0.65
SIMPLIFY = 1.8         
MIN_LENGTH = 20         
DRAW_SPEED = 0           
NUM_COLORS = 16          
FILL_SHAPES = True     
DRAW_BLACK_OUTLINES = True 


img_bgr = cv2.imread(IMAGE)

if img_bgr is None:
    print("ERROR: Could not find", IMAGE)
    exit()

original_height, original_width = img_bgr.shape[:2]
width = int(original_width * SCALE)
height = int(original_height * SCALE)
img_bgr = cv2.resize(img_bgr, (width, height))
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
blurred = cv2.bilateralFilter(img_rgb, d=7, sigmaColor=50, sigmaSpace=50)

pixel_data = np.float32(blurred.reshape((-1, 3)))
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 15, 1.0)
_, labels, centers = cv2.kmeans(
    pixel_data, 
    NUM_COLORS, 
    None, 
    criteria, 
    10, 
    cv2.KMEANS_RANDOM_CENTERS
)

centers = np.uint8(centers)
labels = labels.flatten()

screen = turtle.Screen()
screen.setup(width=width + 100, height=height + 100)
screen.bgcolor("#1a1a24")
screen.title("🐢 Turtle Color Contour Drawing")
screen.colormode(255)  
screen.tracer(10, 0)   

t = turtle.Turtle()
t.speed(DRAW_SPEED)
t.hideturtle()
t.pensize(2)

def convert_point(x, y):
    """Converts image coordinates (top-left 0,0) to Turtle coordinates (center 0,0)."""
    turtle_x = x - width / 2
    turtle_y = height / 2 - y
    return turtle_x, turtle_y

all_regions = []

for color_idx, color in enumerate(centers):
    r, g, b = int(color[0]), int(color[1]), int(color[2])
    
    mask = (labels == color_idx).astype(np.uint8).reshape((height, width)) * 255
  
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        area = cv2.contourArea(contour)
        if perimeter >= MIN_LENGTH and area > 20:
            all_regions.append((contour, (r, g, b), area))

all_regions.sort(key=lambda item: item[2], reverse=True)

print("Total colored regions detected:", len(all_regions))

drawn = 0

for contour, color, _ in all_regions:
    simplified = cv2.approxPolyDP(contour, SIMPLIFY, True)
    if len(simplified) < 3:
        continue

    points = simplified.reshape(-1, 2)
    r, g, b = color

    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)

    start_x, start_y = convert_point(points[0][0], points[0][1])
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    if FILL_SHAPES:
        t.begin_fill()

    for point in points[1:]:
        px, py = convert_point(point[0], point[1])
        t.goto(px, py)

    t.goto(start_x, start_y)

    if FILL_SHAPES:
        t.end_fill()

    t.penup()
    drawn += 1

    if drawn % 15 == 0:
        print(f"Colored regions drawn: {drawn}/{len(all_regions)}")
        screen.update()

if DRAW_BLACK_OUTLINES:
    print("Drawing crisp outlines...")
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 70, 180)
    edge_contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    t.pensize(1.5)
    t.pencolor("#1c1c24")

    for c in edge_contours:
        if cv2.arcLength(c, False) < MIN_LENGTH:
            continue
        pts = cv2.approxPolyDP(c, SIMPLIFY, False).reshape(-1, 2)
        if len(pts) < 2:
            continue

        sx, sy = convert_point(pts[0][0], pts[0][1])
        t.penup()
        t.goto(sx, sy)
        t.pendown()
        for pt in pts[1:]:
            t.goto(*convert_point(pt[0], pt[1]))
        t.penup()

screen.update()
print()
print("================================")
print("🐢 COLOR DRAWING COMPLETE!")
print("================================")

turtle.done()