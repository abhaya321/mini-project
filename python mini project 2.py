import tkinter as tk

# Conversion functions
def convert_length(value, from_unit, to_unit):
    units = {
        "Kilometer": 1,
        "meter": 1000,
        "Centimeter": 100000,
        "Millimeter": 1000000,
        "Micrometer": 1000000000,
        "Nanometer": 1000000000000,
        "Mile": 0.621371,
        "Yard": 1093.61,
        "Foot": 3280.84,
        "Inch": 39370.1,
        "Nautical Mile": 0.539957,

    }
    result = value * units[to_unit] / units[from_unit]
    return result

def convert_mass(value, from_unit, to_unit):
    units = {
        "Ton": 1,
        "Kilogram": 1000,
        "Gram": 1e+6,
        "Milligram": 1e+9,
        "Microgram": 1e+12,
        "Imperial Ton": 0.984207,
        "US Ton": 1.10231,
        "Stone": 157.473,
        "Pound": 2204.62,
        "Ounce": 35274,

    }
    result = value * units[to_unit] / units[from_unit]
    return result
def convert_speed(value, from_unit, to_unit):
    units = {
        "Miles per hour": 1,
        "Foot per second": 1.46667,
        "Meter per second": 0.44704,
        "Kilometer per hour": 1.60934,
        "Knot": 0.868976,
    }
    result = value * units[to_unit] / units[from_unit]
    return result

# Conversion functions for time
def convert_time(value, from_unit, to_unit):
    units = {
        "Nanosecond": 1,
        "Microsecond": 1e-3,
        "Millisecond": 1e-6,
        "Second": 1e-9,
        "Minute": 1.66667e-11,
        "Hour": 2.77778e-13,
        "Day": 1.15741e-14,
        "Week": 1.65344e-15,
        "Month": 3.80518e-16,
        "Year": 3.171e-17,
        "Decade": 3.171e-18,
        "Century": 3.171e-19,
    }
    result = value * units[to_unit] / units[from_unit]
    return result
# Conversion functions for volume
def convert_volume(value, from_unit, to_unit):
    units = {
        "US liquid gallon": 1,
        "US liquid quart": 4,
        "US liquid pint": 8,
        "US legal cup": 16,
        "fluid ounce": 128,
        "US tablespoon": 256,
        "US teaspoon": 768,
        "cubic meter": 3.78541,
        "liter": 3.78541,
        "milliliter": 3785.41,
        "imperial gallon": 0.832674,
        "imperial quart": 3.33061,
        "imperial pint": 6.66124,
        "imperial cup": 13.3225,
        "imperial tablespoon": 40,
        "imperial teaspoon": 120,
        "cubic foot": 0.133681,
        "cubic inch": 231,
    }
    result = value * units[to_unit] / units[from_unit]
    return result

# Conversion functions for energy
def convert_energy(value, from_unit, to_unit):
    units = {
        "joule": 1,
        "kilojoule": 0.001,
        "gram calorie": 0.239006,
        "kilo calorie": 0.000239006,
        "watt hour": 0.000277778,
        "electron volt": 6.242e+18,
        "british thermal unit": 0.000947817,
        "US therm": 9.478e-9,
        "foot-pound": 0.737562,
    }
    result = value * units[to_unit] / units[from_unit]
    return result
# Conversion functions for area
def convert_area(value, from_unit, to_unit):
    units = {
        "Square kilometer": 1,
        "Square meter": 1e+6,
        "Square centimeter": 1e+10,
        "Square millimeter": 1e+12,
        "Square mile": 0.239006,
        "Square yard": 1195990.05,
        "Square foot": 10763910.4,
        "Square inch": 1.55e+9,
        "Acre": 247.105,
        "Hectare": 100,
    }
    result = value * units[to_unit] / units[from_unit]
    return result

# Update Options Function
def update_options():
    category = clicked_category.get()

    from_menu['menu'].delete(0, 'end')
    to_menu['menu'].delete(0, 'end')

    if category == "Length":
        for option in length_options:
            from_menu['menu'].add_command(label=option, command=tk._setit(clicked_from, option))
            to_menu['menu'].add_command(label=option, command=tk._setit(clicked_to, option))
    elif category == "Mass":
        for option in mass_options:
            from_menu['menu'].add_command(label=option, command=tk._setit(clicked_from, option))
            to_menu['menu'].add_command(label=option, command=tk._setit(clicked_to, option))
    elif category == "speed":
        for option in speed_options:
            from_menu['menu'].add_command(label=option, command=tk._setit(clicked_from, option))
            to_menu['menu'].add_command(label=option, command=tk._setit(clicked_to, option))
    elif category == "time":
        for option in time_options:
            from_menu['menu'].add_command(label=option, command=tk._setit(clicked_from, option))
            to_menu['menu'].add_command(label=option, command=tk._setit(clicked_to, option))
    elif category == "volume":
        for option in volume_options:
            from_menu['menu'].add_command(label=option, command=tk._setit(clicked_from, option))
            to_menu['menu'].add_command(label=option, command=tk._setit(clicked_to, option))
    elif category == "energy":
        for option in energy_options:
            from_menu['menu'].add_command(label=option, command=tk._setit(clicked_from, option))
            to_menu['menu'].add_command(label=option, command=tk._setit(clicked_to, option))
    elif category == "Area":
        for option in area_options:
            from_menu['menu'].add_command(label=option,command=tk._setit(clicked_from, option))
            to_menu['menu'].add_command(label=option, command=tk._setit(clicked_to, option))




    # Add similar conditions for other categories

# Conversion Trigger Function
def perform_conversion():
    try:
        value = float(entry.get())
        from_unit = clicked_from.get()
        to_unit = clicked_to.get()
        category = clicked_category.get()

        result = 0.0  # Placeholder for result
        
        if category == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif category == "Mass":
            result = convert_mass(value, from_unit, to_unit)
        elif category == "speed":
            result = convert_speed(value, from_unit, to_unit)
        elif category == "time":
            result = convert_time(value, from_unit, to_unit)
        elif category == "volume":
            result = convert_volume(value, from_unit, to_unit)
        elif category == "energy":
            result = convert_energy(value, from_unit, to_unit)
        elif category == "Area":
            result = convert_area(value, from_unit, to_unit)


        # Add similar conditions for other categories

        result_label.config(text=f"Result: {result:.4f} {to_unit}")

    except ValueError:
        result_label.config(text="Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Unit Converter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

category_options = ["Length", "Mass" , "speed" , "time" , "volume" , "energy" , "Area"]  # Add other categories here
clicked_category = tk.StringVar()
clicked_category.set(category_options[0])

category_label = tk.Label(frame, text="Category:")
category_label.grid(row=0, column=0)
category_menu = tk.OptionMenu(frame, clicked_category, *category_options)
category_menu.grid(row=0, column=1)

clicked_from = tk.StringVar()
from_label = tk.Label(frame, text="From:")
from_label.grid(row=1, column=0)
from_menu = tk.OptionMenu(frame, clicked_from, "")
from_menu.grid(row=1, column=1)

clicked_to = tk.StringVar()
to_label = tk.Label(frame, text="To:")
to_label.grid(row=2, column=0)
to_menu = tk.OptionMenu(frame, clicked_to, "")
to_menu.grid(row=2, column=1)

entry_label = tk.Label(frame, text="Enter value:")
entry_label.grid(row=3, column=0)
entry = tk.Entry(frame)
entry.grid(row=3, column=1)

convert_button = tk.Button(frame, text="Convert", command=perform_conversion)
convert_button.grid(row=4, columnspan=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=5, columnspan=2)

# Define your lists of units for each category
length_options = ["Kilometer", "meter" , "Centimeter", "Millimeter", "Micrometer", "Nanometer", "Mile", "Yard", "Foot", "Inch", "Nautical Mile"]
mass_options = ["Ton", "Kilogram", "Gram", "Milligram", "Microgram", "Imperial Ton", "US Ton", "Stone", "Pound", "Ounce"]
speed_options = ["Miles per hour", "Foot per second", "Meter per second", "Kilometer per hour", "knot"]
time_options = ["Nanosecond" , "Microsecond" , "Millisecond" , "Second" , "Minute" , "Hour" , "Day" , "Week" , "Month" , "Year" , "Decade" , "Century"]
volume_options = ["US liquid gallon" , "US liquid quart" , "US liquid pint" , "US legal cup" , "fluid ounce" , "US tablespoon" , "US teaspoon" , "cubic meter" , "liter" , "milliliter" , "imperial gallon" , "imperial quart" , "imperial pint" , "imperial cup" , "imperial tablespoon" , "imperial teaspoon" , "cubic foot" , "cubic inch "]
energy_options = ["joule" , "kilojoule" , "gram calorie" , "kilo calorie" , "watt hour" , "electron volt" , "british thermal unit" , "US therm" , "foot-pound"]
area_options = ["Square kilometer", "Square meter", "Square centimeter", "Square millimeter", "Square mile", "Square yard", "Square foot", "Square inch", "Acre", "Hectare"]


# Add options for other categories

clicked_category.trace('w', lambda *args: update_options())

update_options()  # Initial update of options based on the default category

root.mainloop()
