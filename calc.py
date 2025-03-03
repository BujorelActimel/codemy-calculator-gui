import pygame
# import pgzrun

WIDTH = 300
HEIGHT = 450
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

    {"text": "x^2", "x": 0, "y": 4, "action": "operation", "value": "square"},
    {"text": "sqrt", "x": 1, "y": 4, "action": "operation", "value": "sqrt"}
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
    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        rect = calculate_button_rect(button)
        if rect.collidepoint(mouse_pos):
            return button
    return None

def perform_operation():
    global stored_value, display_value, current_operation

    if current_operation is None:
        return display_value
    
    current_value = float(display_value)

    if current_operation == "add":
        result = stored_value + current_value
    elif current_operation == "subtract":
        result = stored_value - current_value
    elif current_operation == "multiply":
        result = stored_value * current_value
    elif current_operation == "divide":
        if current_value == 0:
            return "cannot divide by zero"
        result = stored_value / current_value

    if len(str(result)) > 20:
        return "result is too large"

    if result == int(result):
        return str(int(result))
    else:
        return str(result)


def on_mouse_down(pos, button):
    global display_value, stored_value, current_operation, clear_on_next_input

    if button != mouse.LEFT:
        return
    
    hovered_button = get_hovered_button()
    if not hovered_button:
        return
    
    action = hovered_button["action"]
    value = hovered_button["value"]

    if action == "number":
        if display_value == "0" or clear_on_next_input:
            display_value = str(value)
            clear_on_next_input = False
        else:
            display_value += str(value)
    
    elif action == "operation":
        if current_operation is not None:
            display_value = perform_operation()
        
        stored_value = float(display_value)
        current_operation = value
        clear_on_next_input = True

    elif action == "equals":
        if current_operation is not None:
            display_value = perform_operation()
            stored_value = 0
            current_operation = None
            clear_on_next_input = True
    
    elif action == "clear":
        display_value = "0"
        stored_value = 0
        current_operation = None
        clear_on_next_input = True


def draw():
    screen.fill(BACKGROUND_COLOR)

    screen.draw.filled_rect(
        Rect((BUTTON_PADDING, BUTTON_PADDING), (WIDTH - 2 * BUTTON_PADDING, 80)),
        DISPLAY_COLOR
    )

    screen.draw.text(
        display_value,
        centerx=WIDTH//2,
        centery=45,
        fontsize=36,
        color=TEXT_COLOR
    )

    hovered_button = get_hovered_button()

    for button in buttons:
        rect = calculate_button_rect(button)
        is_hovering = (hovered_button == button)
        color = get_button_color(button, is_hovering)

        screen.draw.filled_rect(rect, color)
        screen.draw.text(
            button["text"],
            center=rect.center,
            fontsize=24,
            color=TEXT_COLOR
        )

# pgzrun.go()
