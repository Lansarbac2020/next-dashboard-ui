import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(figsize=(10,10))

# Helper functions to draw geometric objects
def draw_line(p1, p2, label=None, color='black'):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color)
    if label:
        ax.text((p1[0]+p2[0])/2, (p1[1]+p2[1])/2, label, fontsize=12, ha='right')

def draw_point(p, label=None, color='black'):
    ax.plot(p[0], p[1], 'o', color=color)
    if label:
        ax.text(p[0], p[1], label, fontsize=12, ha='right')

def draw_circle(center, radius, label=None, color='black'):
    circle = plt.Circle(center, radius, fill=False, color=color)
    ax.add_patch(circle)
    if label:
        ax.text(center[0], center[1]-radius-0.1, label, fontsize=12, ha='center')

def draw_square_in_circle(center, radius):
    # Draw square inside the circle
    points = [(center[0]-radius, center[1]-radius),
              (center[0]+radius, center[1]-radius),
              (center[0]+radius, center[1]+radius),
              (center[0]-radius, center[1]+radius)]
    for i in range(4):
        draw_line(points[i], points[(i+1) % 4])

def draw_triangle_with_incircle():
    # Draw triangle
    points = [(2, 8), (5, 10), (7, 7)]
    for i in range(3):
        draw_line(points[i], points[(i+1) % 3])
    
    # Draw incircle
    center = (4.8, 8.2)
    draw_circle(center, 0.7)

# 1. Dividing a 6 cm segment into two parts
draw_line((0, 9), (6, 9), 'AB')
draw_point((3, 9), 'Midpoint')

# 2. Perpendicular from P outside the segment
draw_line((0, 8), (6, 8), 'AB')
draw_point((3, 9.5), 'P')
draw_line((3, 9.5), (3, 8), color='blue')

# 3. Perpendicular from P on the segment
draw_line((0, 7), (6, 7), 'AB')
draw_point((3, 7), 'P')
draw_line((3, 7), (3, 6), color='blue')

# 4. Dividing a segment into 7 equal parts
draw_line((0, 6), (6, 6), 'AB')
for i in range(1, 7):
    draw_point((i, 6), f'{i}')

# 5. Incircle of an acute triangle
draw_triangle_with_incircle()

# 6. Square inside a circle
draw_circle((8, 3), 2)
draw_square_in_circle((8, 3), 2)

# 7. Bisector of an obtuse angle
draw_line((2, 1), (5, 1), 'Line 1')
draw_line((2, 1), (3, 3), 'Line 2')
draw_line((2, 1), (3, 2), color='blue')  # Bisector

# 8. Dividing a 90° angle into three equal parts
draw_line((0, 0), (4, 0), 'Base Line')
draw_line((0, 0), (0, 4), 'Perpendicular')
draw_line((0, 0), (3.46, 2), color='blue')  # 30°
draw_line((0, 0), (2, 3.46), color='blue')  # 60°

# Set plot limits and display
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 11)
ax.set_aspect('equal', 'box')
plt.gca().set_axis_off()
plt.show()
