import pygame
import pgzrun

WIDTH = 300
HEIGHT = 400
TITLE = "Calculator"

BUTTON_WIDTH = 60
BUTTON_HEIGHT = 60
BUTTON_PADDING = 10

BACKGROUND_COLOR = (30, 30, 30)
BUTTON_COLOR = (60, 60, 60)
BUTTON_HOVER_COLOR = (80, 80, 80)
DISPLAY_COLOR = (40, 40, 40)
TEXT_COLOR = (255, 255, 255)
OPERATION_BUTTON_COLOR = (80, 80, 160)
OPERATION_HOVER_COLOR = (100, 100, 180)
EQUALS_BUTTON_COLOR = (80, 160, 80)
EQUALS_HOVER_COLOR = (100, 180, 100)
CLEAR_BUTTON_COLOR = (160, 80, 80)
CLEAR_HOVER_COLOR = (180, 100, 100)

display_value = "0"
stored_value = 0
current_operation = None
clear_on_next_input = False

buttons = [
    {"text": "7", "x": 0, "y": 0, "action": "number", "value": 7},
    {"text": "8", "x": 1, "y": 0, "action": "number", "value": 8},
    {"text": "9", "x": 2, "y": 0, "action": "number", "value": 9},
    {"text": "/", "x": 3, "y": 0, "action": "operation", "value": "divide"},
    
    {"text": "4", "x": 0, "y": 1, "action": "number", "value": 4},
    {"text": "5", "x": 1, "y": 1, "action": "number", "value": 5},
    {"text": "6", "x": 2, "y": 1, "action": "number", "value": 6},
    {"text": "x", "x": 3, "y": 1, "action": "operation", "value": "multiply"},
    
    {"text": "1", "x": 0, "y": 2, "action": "number", "value": 1},
    {"text": "2", "x": 1, "y": 2, "action": "number", "value": 2},
    {"text": "3", "x": 2, "y": 2, "action": "number", "value": 3},
    {"text": "-", "x": 3, "y": 2, "action": "operation", "value": "subtract"},
    
    {"text": "0", "x": 0, "y": 3, "action": "number", "value": 0},
    {"text": "C", "x": 1, "y": 3, "action": "clear", "value": "clear"},
    {"text": "=", "x": 2, "y": 3, "action": "equals", "value": "equals"},
    {"text": "+", "x": 3, "y": 3, "action": "operation", "value": "add"},
]

def calculate_button_rect(button):
    x = button["x"] * (BUTTON_WIDTH + BUTTON_PADDING) + BUTTON_PADDING
    y = button["y"] * (BUTTON_HEIGHT + BUTTON_PADDING) + 100
    return Rect((x, y), (BUTTON_WIDTH, BUTTON_HEIGHT))

def get_button_color(button, hovering):
    action = button["action"]

    if action == "operation":
        # if hovering:
        #     return OPERATION_HOVER_COLOR
        # else:
        #     return OPERATION_BUTTON_COLOR
        return OPERATION_HOVER_COLOR if hovering else OPERATION_BUTTON_COLOR
    elif action == "equals":
        return EQUALS_HOVER_COLOR if hovering else EQUALS_BUTTON_COLOR
    elif action == "clear":
        return CLEAR_HOVER_COLOR if hovering else CLEAR_BUTTON_COLOR
    else:
        return BUTTON_HOVER_COLOR if hovering else BUTTON_COLOR

def get_hovered_button():
    pass

def perform_operation():
    pass

def on_mouse_down(pos, button):
    pass

def draw():
    pass

pgzrun.go()
