import simplegui

current_section = "Home"


def start_rescue():
    global current_section
    current_section = "Rescue Operations"
    print("Leader is now focused on Rescue Operations: Provide immediate aid to survivors.")

def start_rebuilding():
    global current_section
    current_section = "Rebuilding Infrastructure"
    print("Leader is now focused on Rebuilding Infrastructure: Restore vital systems like shelter and power.")

def start_resources():
    global current_section
    current_section = "Resource Management"
    print("Leader is now focused on Resource Management: Distribute food, water, and medical supplies.")

def draw(canvas):
    canvas.draw_text("Current Focus: " + current_section, (100, 100), 24, "White")

frame = simplegui.create_frame("Myrina Rescue Mission", 400, 300)

frame.add_button("Start Rescue Operations", start_rescue, 200)
frame.add_button("Start Rebuilding Infrastructure", start_rebuilding, 200)
frame.add_button("Start Resource Management", start_resources, 200)

frame.set_draw_handler(draw)

frame.start()
