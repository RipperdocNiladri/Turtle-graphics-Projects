import cv2
import turtle

IMAGE = "YOUR_IMAGE.png"  # Replace with your image file path

SCALE = 0.65
SIMPLIFY = 2.0
MIN_LENGTH = 30
DRAW_SPEED = 0


img = cv2.imread(IMAGE, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("ERROR: Could not find", IMAGE)
    exit()

original_height, original_width = img.shape


width = int(original_width * SCALE)
height = int(original_height * SCALE)

img = cv2.resize(img, (width, height))


_, binary = cv2.threshold(
    img,
    180,
    255,
    cv2.THRESH_BINARY_INV
)

contours, _ = cv2.findContours(
    binary,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_NONE
)

print("Contours detected:", len(contours))


screen = turtle.Screen()

screen.setup(
    width=width + 100,
    height=height + 100
)

screen.bgcolor("white")
screen.title("🐢 Turtle Drawing")

t = turtle.Turtle()

t.speed(DRAW_SPEED)
t.hideturtle()
t.pensize(2)
t.color("black")


def convert_point(x, y):
    turtle_x = x - width / 2
    turtle_y = height / 2 - y

    return turtle_x, turtle_y


contours = sorted(
    contours,
    key=cv2.contourArea,
    reverse=True
)

drawn = 0

for contour in contours:

    perimeter = cv2.arcLength(
        contour,
        True
    )

    if perimeter < MIN_LENGTH:
        continue

    epsilon = SIMPLIFY

    simplified = cv2.approxPolyDP(
        contour,
        epsilon,
        True
    )

    if len(simplified) < 2:
        continue

    points = simplified.reshape(-1, 2)

    x, y = convert_point(
        points[0][0],
        points[0][1]
    )

    t.penup()
    t.goto(x, y)
    t.pendown()

    for point in points[1:]:

        x, y = convert_point(
            point[0],
            point[1]
        )

        t.goto(x, y)

    x, y = convert_point(
        points[0][0],
        points[0][1]
    )

    t.goto(x, y)

    t.penup()

    drawn += 1

    if drawn % 10 == 0:
        print("Contours drawn:", drawn)


print()
print("================================")
print("🐢 DRAWING COMPLETE!")
print("Contours drawn:", drawn)
print("================================")

turtle.done()