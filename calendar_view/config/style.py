from PIL import ImageFont
try:
    from importlib.resources import files, as_file  # stdlib (Py≥3.9)
except ImportError:
    # noinspection PyUnresolvedReferences
    from importlib_resources import files, as_file  # backport


font_path: str = 'Roboto-Regular.ttf'
helvetica_path: str = 'HelveticaNeue.ttc'


def image_font(size: int):
    # Try to use bundled Helvetica Neue, fallback to Roboto
    try:
        res = files('calendar_view.resources.fonts') / helvetica_path
        with as_file(res) as tmp_path:
            return ImageFont.truetype(str(tmp_path), size)
    except (OSError, IOError):
        res = files('calendar_view.resources.fonts') / font_path
        with as_file(res) as tmp_path:
            return ImageFont.truetype(str(tmp_path), size)


# Shadcn dark theme colors - pure black background
image_bg = (0, 0, 0, 255)  # Pure black

hour_height = 50
day_width = 400
padding_horizontal = 60
padding_vertical = 30

title_font = image_font(50)
title_color = (255, 255, 255, 255)  # Pure white
title_padding_left = 30
title_padding_right = 30
title_padding_top = 30
title_padding_bottom = 20

hour_number_font = image_font(22)
hour_number_color = (255, 255, 255, 255)  # Pure white

day_of_week_font = image_font(28)
day_of_week_color = (255, 255, 255, 255)  # Pure white

# Subtle borders - light gray for visibility on black
line_day_color = (100, 100, 100, 180)  # Light gray with transparency
line_day_width = 2
line_hour_color = (80, 80, 80, 120)  # Darker gray, more transparent
line_hour_width = 1

# Event styling with rounded corners like shadcn
event_border_width = 2
event_radius = 8  # Shadcn uses subtle rounded corners (rounded-md)
event_border_default = (71, 85, 105, 255)  # Slate-600
event_fill_default = (30, 41, 59, 240)  # Slate-800 with slight transparency

# Smaller font sizes for event text, all white
event_title_font = image_font(21)  # Increased by 1
event_title_color = (255, 255, 255, 255)  # Pure white
event_notes_font = image_font(17)  # Increased by 1
event_notes_color = (255, 255, 255, 255)  # Pure white
event_padding: int = 12  # Tighter padding for compact look
event_title_margin: int = 8  # Reduced margin

legend_spacing = 20
legend_padding_top = 40
legend_padding_bottom = 70
legend_padding_left = 70
legend_padding_right = 40
legend_name_font = image_font(28)
legend_name_color = (255, 255, 255, 255)  # Pure white

# https://stackoverflow.com/questions/7510313/transparent-png-in-pil-turns-out-not-to-be-transparent
