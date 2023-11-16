color_names=raw_input('enter comma-seperated color names:')
colors=color_names.split(',')
colors=[color.strip() for color in colors]
if len(colors) >= 2:
    print('First color:',colors[0])
    print('Last color:',colors[-1])
else:
    print('Please enter atleast two color names')
