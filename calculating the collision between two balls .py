import math

def ball_collides(ball1, ball2):
    # Extract the positions and radii of the two balls
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2

    # Calculate the distance between the centers of the two balls
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Determine if the balls are colliding by comparing the distance to the sum of their radii
    if distance <= r1 + r2:
        return True
    else:
        return False

# Define two balls: (x, y, r)
ball1 = (0, 0, 1)
ball2 = (3, 4, 2)

# Check if the two balls are colliding
collision = ball_collides(ball1, ball2)

# Print the result
print(collision)  # Output: False