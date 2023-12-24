import turtle 
import pandas 

screen = turtle.Screen()
screen.title("Indian States Game 2023")
image = "Projects_Python\Indian_State_Quiz\India-states-new.gif"
screen.addshape(image)
turtle.shape(image)
states_csv = pandas.read_csv("Projects_Python\Indian_State_Quiz\/28_states.csv")
guesses=[]
missing_states=[]
Turr = turtle.Turtle()
Turr.hideturtle()
Turr.penup()
while len(guesses)<28:
    input_state = screen.textinput(title=f"{len(guesses)}/28 Guess the state",prompt="Enter state name: ").title()
    
    #End the Game
    if input_state=="Exit" or input_state == "End":
        break
    #already guessed
    if input_state not in guesses:
        input_state_corxy = states_csv[states_csv.state==input_state]
        
        #if state exists in the list
        if not (input_state_corxy.empty):
            Turr.goto(int(input_state_corxy.x.iloc[0]),int(input_state_corxy.y.iloc[0]))
            Turr.write(input_state)
            guesses.append(input_state)

states = states_csv.state
for state in states:
    if state not in guesses:
        missing_states.append(state)

dict_states_to_learn={
    "states":missing_states
}

states_to_learn = pandas.DataFrame(dict_states_to_learn)
states_to_learn.to_csv("Projects_Python\Indian_State_Quiz\To_learn_states.csv",index=False)
