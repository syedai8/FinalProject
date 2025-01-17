import simplegui

current_section = "Home"
description = "Select a task on the left to begin the mission."

score = 0 

def start_rescue():
    global current_section, description, priorityRescue, score 
    current_section = "Rescue Operations"
    description = "Provide immediate aid to survivors"
    print(description)
    print("Choose wisely, you only get one choice for Myrina!")
    priorityRescue = input("Will you ike prioritize rescuing doctors, engineers, scientists or normal civillians? ")
    if priorityRescue == "doctors":
        print("You have gained experienced healthcare practitioners that can help the health of Myrina!")
        score = score + 500
    elif priorityRescue == "engineers":
        print("You have gained experienced builders that can help with infrastructure of Myrina!")
        score = score + 700
    elif priorityRescue == "scientists":
        print("You have gained protectos that can get the shield of Myrina back!")
        score = score + 1000
    else: 
        print("You have gained no special powers..!")
        score = score + 100

def start_rebuilding():
    global current_section, description, priorityRescue, score 
    current_section = "Rebuilding Infrastructure"
    description = "Restore vital systems like shelter and power"
    print(description)
    print("Choose wisely, you only get one choice for Myrina!")
    priorityBuild = input("What will you prioritize building first? Power facilities, Hospitals, Labs")
    if priorityBuild == "power facilities":
        if priorityRescue == "engineers":
            print("You rescued enough engineers to be able to build power facilities for Myrina!")
            score = score + 1000
        else:
            print("You did not prioritized rescuing engineers, so power facilities will have to wait..!")
            score = score 
    elif priorityBuild == "hospitals":
        if priorityRescue == "doctors":
            print("You rescued enough doctors to be able to provide healtcare to Myrina!")
            score = score + 700
        else:
            print("You did  not prioritize rescuing doctors, so hospitals will have to wait..!")
            score = score 
    elif priorityBuild == "labs":
        if priorityRescue == "scientists":
            print("You rescued enough scientists for labs and can provide defense for Myrina!")
            score = score + 600
        else: 
            print("You did not prioritize rescuing scientists, so labs will have to wait..!")
            score = score 
    else:
        print("Answer unclear, type again.")

def start_resources():
    global current_section, description, priorityRescue, score 
    current_section = "Resource Management"
    description = "Distribute food, water, and medical supplies"
    print(description)
    print("Now that you have made your choices, lead your team and civillians to distribute food and water!")
    score = score + 500

    
    
def draw(canvas):
    canvas.draw_text("Current Focus: " + current_section, (10, 100), 24, "White")
    canvas.draw_text(description, (10, 150), 18, "White")
    canvas.draw_polygon([(0, 200), (400,200), (400,400), (0, 400)], 2, "#F6FB8E", "#F6FB8E")
    canvas.draw_text("Score: " + str(score), (300, 20), 20, "White")

frame = simplegui.create_frame("Myrina Rescue Mission", 400, 400)

frame.add_button("Start Rescue Operations", start_rescue, 200)
frame.add_button("Start Rebuilding Infrastructure", start_rebuilding, 200)
frame.add_button("Start Resource Management", start_resources, 200)
frame.set_canvas_background("#67C5FF")

frame.set_draw_handler(draw)

frame.start()
