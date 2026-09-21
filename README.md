# 🐢 Turtle Image Tracer

A simple computer-vision project that converts **images into drawable contours** and recreates them using Python's built-in **Turtle Graphics**.

The project combines **OpenCV image processing** with **Turtle Graphics** to turn an image into a sequence of paths that a Turtle can automatically draw on the screen.

> **Pixels → Contours → Coordinates → Turtle Drawing** 🎨🐢

---

## ✨ Demo

The program takes a black-and-white line-art image and reconstructs it using Turtle Graphics.

```text
        Original Image
              │
              ▼
      ┌───────────────┐
      │    OpenCV     │
      │ Image Process │
      └───────┬───────┘
              │
              ▼
        Detect Contours
              │
              ▼
       Simplify Points
              │
              ▼
      Convert Coordinates
              │
              ▼
       🐢 Python Turtle
              │
              ▼
       Reconstructed Art
```

The Turtle then follows the detected contours and automatically redraws the original artwork.

---

## 🚀 Features

* 🖼️ Converts line-art images into drawable paths
* 🔍 Detects outlines using OpenCV
* ✂️ Simplifies contours to reduce unnecessary points
* 🐢 Draws detected contours using Python Turtle
* ⚫ Produces black-line drawings on a white canvas
* ⚙️ Adjustable drawing quality and speed
* 📐 Automatically converts OpenCV coordinates to Turtle coordinates
* 🧠 Demonstrates fundamental computer-vision concepts

---

## 🛠️ Technologies Used

* **Python 3**
* **OpenCV**
* **Turtle Graphics**
* **NumPy** — used internally by OpenCV

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/RipperdocNiladri/Turtle-graphics-Projects.git
cd Turtle-graphics-Projects
```

### 2. Install OpenCV

```bash
pip install opencv-python
```

> **Note:** `turtle` is included with standard Python installations, so no separate installation is normally required.

---

## 📁 Project Structure

```text
Turtle-Image-Tracer/
│
├── turtle_image.py
├── turtle_colour_image.py
├── YOUR_IMAGE.png
├── mandala.py
└── README.md
```

---

## ▶️ Usage

Place your black-and-white line-art image inside the project directory.

For example:

```text
YOUR_IMAGE.png
```

Then run:

```bash
python turtle_image.py
```

The program will:

1. Load the image
2. Convert it to grayscale
3. Resize the image
4. Threshold the image
5. Detect contours
6. Remove very small contours
7. Simplify contour points
8. Convert image coordinates into Turtle coordinates
9. Draw the detected contours

---
# ⚙️ Turtle Colour Image Configuration

Python's **Turtle Graphics** provides multiple ways to control how fast your drawing is rendered.

There are two main methods:

1. 🚀 **Screen-level rendering control** using `screen.tracer()`
2. 🐢 **Turtle movement speed** using `t.speed()`

> 💡 **Recommendation:** If your project performs lots of drawing operations, `screen.tracer()` has a much greater effect on the overall rendering speed than `t.speed()`.

---

## 🚀 Method 1 — `screen.tracer()`

The recommended way to control the **overall drawing/rendering speed** is:

```python
screen.tracer(frames, delay_in_ms)
```

For example:

```python
screen.tracer(10, 0)
```

The two parameters control how frequently the Turtle screen updates and the delay between updates.

### ⚙️ Speed Presets

| Desired Speed                    | Configuration                                | Description                                                 |
| -------------------------------- | -------------------------------------------- | ----------------------------------------------------------- |
| 🚀 **Super Fast / Near Instant** | `screen.tracer(50, 0)` or `screen.tracer(0)` | Renders extremely quickly.                                  |
| ⚡ **Fast**                       | `screen.tracer(10, 0)`                       | Fast drawing while still allowing you to see progress.      |
| ☕ **Medium / Relaxed**           | `screen.tracer(2, 5)`                        | Updates every 2 strokes with a small delay.                 |
| 🐢 **Slow & Cinematic**          | `screen.tracer(1, 25)`                       | Updates frequently for a slower, deliberate drawing effect. |

### 🔍 Example

```python
screen = turtle.Screen()

screen.tracer(10, 0)

# Drawing code...
```

---

## 🐢 Method 2 — `t.speed()`

Python Turtle also provides a built-in movement speed control:

```python
t.speed(DRAW_SPEED)
```

For example:

```python
DRAW_SPEED = 0

t.speed(DRAW_SPEED)
```

### ⚙️ Turtle Speed Values

| Value | Speed                          |
| ----: | ------------------------------ |
|   `1` | 🐢 Slowest                     |
|   `3` | 🐌 Slow                        |
|   `6` | 🚶 Normal                      |
|  `10` | ⚡ Fast                         |
|   `0` | 🚀 Fastest — no turn animation |

Example:

```python
DRAW_SPEED = 6
t.speed(DRAW_SPEED)
```

---

## ⚠️ Which One Should You Use?

When your project uses a large number of drawing operations, `screen.tracer()` generally has a **much bigger impact** on the final rendering speed.

Think of it like this:

```text
t.speed()
     ↓
Controls Turtle movement animation

screen.tracer()
     ↓
Controls screen refresh / rendering
     ↓
Affects overall drawing performance
```

For complex drawings, you can combine both:

```python
DRAW_SPEED = 0

t.speed(DRAW_SPEED)
screen.tracer(10, 0)
```

---

# 📋 Quick Copy-Paste Examples

## 🐢 Slow Down the Drawing

If you want to clearly watch the Turtle sketch **stroke by stroke**, use:

```python
screen.tracer(1, 15)
```

This updates the screen after each drawing step with a small delay.

---

## ⚡ Fast Drawing

For a fast but still visible rendering:

```python
screen.tracer(10, 0)
```

---

## 🚀 Draw Almost Instantly

If you want the drawing to appear as quickly as possible:

```python
screen.tracer(0)
```

This disables automatic screen updates while the drawing is being generated.

If you use this approach, make sure the screen is updated after the drawing:

```python
screen.tracer(0)

# Drawing code...

screen.update()
```

---

## 🎯 Recommended Configurations

### 🎬 Cinematic Mode

Best when you want to record the Turtle drawing process:

```python
screen.tracer(1, 15)
t.speed(3)
```

### ⚡ Preview Mode

Good balance between speed and visibility:

```python
screen.tracer(10, 0)
t.speed(6)
```

### 🚀 Performance Mode

Best for generating complex drawings quickly:

```python
screen.tracer(0)
t.speed(0)

# Drawing code...

screen.update()
```

---

## 🧠 In Short

```text
             TURTLE DRAWING SPEED
                     │
          ┌──────────┴──────────┐
          │                     │
      t.speed()           screen.tracer()
          │                     │
   Turtle animation       Screen rendering
          │                     │
     0 → Fastest          0 → No automatic
                          screen updates
```

> 💡 **Tip:** For image-tracing or complex Turtle projects, experiment with `screen.tracer()` first. It usually makes the biggest difference in drawing performance.

---

### 🔧 Main Controls

```python
# Turtle movement speed
t.speed(0)

# Screen rendering speed
screen.tracer(10, 0)
```

Adjust these values depending on whether you want **performance**, **visibility**, or a **cinematic drawing effect**. 🐢🎨




## ⚙️ Turtle Image Configuration


You can adjust the following values inside `turtle_image.py`:

```python
SCALE = 0.65
SIMPLIFY = 2.0
MIN_LENGTH = 30
DRAW_SPEED = 0
```

### `SCALE`

Controls the size of the input image.

```python
SCALE = 0.65
```

Higher values produce a larger drawing.

---

### `SIMPLIFY`

Controls how aggressively contour points are simplified.

```python
SIMPLIFY = 2.0
```

#### Lower values

* More detail
* More points
* Slower drawing

#### Higher values

* Fewer points
* Faster drawing
* Less detail

---

### `MIN_LENGTH`

Controls which small contours are ignored.

```python
MIN_LENGTH = 30
```

Increasing this value removes more small details and noise.

---

### `DRAW_SPEED`

Controls Turtle's drawing speed.

```python
DRAW_SPEED = 0
```

For maximum drawing speed:

```python
DRAW_SPEED = 0
```

For a visible drawing animation:

```python
DRAW_SPEED = 3
```

You can experiment with different values to find the desired balance between speed and animation.

---

## 🧠 How It Works

The complete process can be summarized as:

```text
Image
  ↓
Grayscale Conversion
  ↓
Thresholding
  ↓
Contour Detection
  ↓
Contour Simplification
  ↓
Coordinate Conversion
  ↓
Turtle Drawing
```

### 1. Load the Image

OpenCV loads the image as a grayscale image.

```python
img = cv2.imread(
    IMAGE,
    cv2.IMREAD_GRAYSCALE
)
```

---

### 2. Resize the Image

The image is resized according to the selected scale.

```python
img = cv2.resize(
    img,
    (width, height)
)
```

This allows the size of the final Turtle drawing to be controlled.

---

### 3. Threshold the Image

The grayscale image is converted into a binary image.

```python
_, binary = cv2.threshold(
    img,
    180,
    255,
    cv2.THRESH_BINARY_INV
)
```

This separates the dark line-art from the white background, making the outlines easier for OpenCV to detect.

---

### 4. Find Contours

OpenCV searches for the boundaries of the detected shapes.

```python
contours, _ = cv2.findContours(
    binary,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_NONE
)
```

Each contour is essentially a sequence of points representing part of the image's geometry.

---

### 5. Simplify the Contours

Raw contours can contain thousands of points.

The program uses:

```python
cv2.approxPolyDP()
```

to reduce unnecessary points while preserving the overall shape.

This improves drawing performance without significantly changing the appearance of the artwork.

---

### 6. Convert Coordinates

OpenCV and Turtle use different coordinate systems.

**OpenCV:**

```text
(0,0)
  ───────────► X
  │
  │
  ▼
  Y
```

**Turtle:**

```text
          +Y
           ▲
           │
           │
-X ◄───────┼───────► +X
           │
           │
           ▼
          -Y
```

The program converts the detected OpenCV coordinates into Turtle coordinates before drawing.

---

### 7. Turtle Draws the Contours 🐢

Finally, Turtle moves through the detected points:

```python
t.goto(x, y)
```

By following each contour, Turtle reconstructs the original artwork as a collection of connected paths.

---

## 🎯 Example Use Cases

This project can be used to learn about:

* Computer Vision
* OpenCV
* Image Processing
* Contour Detection
* Coordinate Systems
* Computational Drawing
* Turtle Graphics
* Python Automation

It can also serve as a foundation for more advanced projects such as:

```text
Image
  ↓
Edge Detection
  ↓
Contour Extraction
  ↓
Path Optimization
  ↓
Drawing Algorithm
  ↓
Plotter / Pen Robot
```

---

## 🔮 Future Improvements

Possible upgrades include:

* 🔍 Automatic edge detection
* 🧭 Better contour ordering
* 🖼️ Support for outer borders and inner details
* 🖊️ Adjustable pen thickness
* 📊 Drawing progress indicator
* 🎞️ Improved real-time drawing animation
* 🌈 Color image support
* 🗂️ Multiple drawing layers
* ⚡ Path optimization
* 📄 Export detected paths as SVG
* 🖨️ Support for physical pen plotters
* 🤖 Arduino/robotic drawing integration

---

## 🧪 Learning Goal

The main purpose of this project is **learning and experimentation**.

Rather than simply displaying an image, the project explores how an image can be represented as **geometric paths** and then reconstructed using a programmable drawing system.

It demonstrates the connection between:

> **Computer Vision → Geometry → Coordinates → Graphics**


---

Engineering student exploring:

* 🐍 Python
* 👁️ Computer Vision
* 🤖 AI/ML
* 🔌 Embedded Systems
* 🦾 Robotics
* ⚙️ Automation

---

## ⭐ Project Status

**Active — Experimental / Learning Project**

The project is being developed gradually as new image-processing and drawing techniques are explored.

---

## 📜 License

No formal license is currently provided.

This is primarily a personal learning and experimentation project.

---

## 🏷️ GitHub Tagline

> **🐢 Image → Contours → Turtle Drawing | A Python + OpenCV experiment in computer vision and computational art.**

---

<p align="center">
  Made with Python 🐍, OpenCV 👁️ and Turtle 🐢
</p>

## Author 

**Niladri Pal**
