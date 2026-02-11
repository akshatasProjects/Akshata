import turtle
import pandas

# Creating a screen
screen = turtle.Screen()
screen.title("U S State Guessing Game")
image = "../US-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# getting the CSV data
data = pandas.read_csv("../US-states-game-start/50_states.csv")
# Converting the data to list
all_states = data.state.to_list()
user_guessed_state = []

while len(user_guessed_state) < 50:
    # creating a prompt box getting state name from user
    ans_state = screen.textinput(f"{len(user_guessed_state)/50}",  prompt="What's the state name?").title()

    # checking for user wants to exit and Saving data to CSV
    if ans_state == "Exit":
        missing_state_list = [eachState for eachState in all_states if eachState not in user_guessed_state]
        # for eachState in all_states:
        #     if eachState not in user_guessed_state:
        #         missing_state_list.append(state) 
        
        new_data = pandas.DataFrame(missing_state_list)
        new_data.to_csv("Missed_States.csv")
        break    

    if ans_state in all_states:
        t =turtle.Turtle()
        t.hideturtle()
        t.penup()
        # extracting the whole row if data matches
        state_data = data[data.state == ans_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

screen.exitonclick()