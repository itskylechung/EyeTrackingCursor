from screeninfo import get_monitors

monitors = get_monitors()
print(f"Detected {len(monitors)} screen(s):")
for i, m in enumerate(monitors):
    print(f"Screen {i}: x={m.x}, y={m.y}, width={m.width}, height={m.height}")
