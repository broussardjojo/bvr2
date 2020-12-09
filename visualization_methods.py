# Import statements
import geopandas as gpd
import geoplot as gplt


def init(width, height, edgeColor, faceColor):
    boston = (-71.2, 42.2, -70.9, 42.4)
    boston_neighborhoods = gpd.read_file('datasets/Boston_Neighborhoods.geojson')
    return gplt.polyplot(boston_neighborhoods, extent=boston, edgecolor=edgeColor, facecolor=faceColor,
                         figsize=(width, height))


# Plots the subway on the provided subplot.
# Note that we didn't abstract this method - this is because jojo wanted it to be pretty in multiple colors.
def add_subway(ax):
    mbta_routes = gpd.read_file('datasets/routes.geojson')

    # Plotting Orange Line
    orange_line = mbta_routes.query("name=='Orange Line'")
    ax = orange_line.plot(ax=ax, color='orange')

    # Green Line
    green_line = mbta_routes.query(
        "name in ['Boston College (B)', 'Cleveland Circle (C)', 'Riverside (D)', 'Heath St. (E)']")
    ax = green_line.plot(ax=ax, color='green')

    # Red line
    # Note - there's a problem here in the Braintree line.
    # Fixing it requires... looking at the coordinates of
    # each individual stop on the braintree line :/
    red_line = mbta_routes.query("name in ['Braintree', 'Mattapan']")
    ax = red_line.plot(ax=ax, color='red')

    # Blue line
    blue_line = mbta_routes.query("name == 'Blue Line'")
    ax = blue_line.plot(ax=ax, color='blue')

    return ax


def add_visualization(ax, path, color):
    toDraw = gpd.read_file(path)
    ax = toDraw.plot(ax=ax, color= color)
    return ax


def add_polling_locations(ax, color):
    return add_visualization(ax, "datasets/Polling_Locations.geojson", color)


# Checking to see if the gpd.plot works for polygons...
def add_open_space(ax, color):
    return add_visualization(ax, "datasets/Open_Space.geojson", color)


# Save an AxesSubplot in the resultImages folder
def save_as(ax, name):
    fig = ax.get_figure()
    fig.savefig("resultImages/" + name + ".png")

# Parser to create a visualization based on an input string:
# More than anything, this is a proof of concept of a method that a front end could call based on a variety of
# Selections by the user.

# Current accepted parameters (ideally, these would be factored out into their own function):
# - -subway : plots the MBTA on the map, with each line in their respective color
# - -bikeNetwork [color]
# - -publicLibraries [color]
# - -openSpace [color]
# - -colleges [color]
# - -evStations [color]
# - -pollingLocations [color]
# - -trees [color]

def parser(vargs):
    argList = vargs.split()
    index = 0

    ax = init(10, 10, "white", "lightgray")
    while index < len(argList):
        carg = argList[index]
        # Yes i know this is bad design!
        # But it'll work and it's a proof of concept!
        # There are no switch statements in python
        # Nothing means anything to me anymore. I just want to be done with the semester
        # So that I can wallow in despair with marginally less stress on myself

        #this implementation is not particularly robust. Don't try too hard to break it!
        if carg == "-subway" :
            ax = add_subway(ax)
        else:
            index += 1
            color = argList[index]
            if carg == "-bikeNetwork":
                ax = add_visualization(ax, "datasets/Existing_Bike_Network.geojson", color)
            elif carg == "-publicLibraries":
                ax = add_visualization(ax, "datasets/Public_Libraries.geojson", color)
            elif carg == "-openSpace":
                ax = add_visualization(ax, "datasets/Open_Space.geojson", color)
            elif carg == "-colleges":
                ax = add_visualization(ax, "datasets/Colleges_and_Universities.geojson", color)
            elif carg == "-evStations":
                ax = add_visualization(ax, "datasets/Charging_Stations.geojson", color)
            elif carg == "-pollingLocations":
                ax = add_visualization(ax, "datasets/Polling_Locations.geojson", color)
            elif carg == "-trees":
                ax = add_visualization(ax, "datasets/trees.geojson", color)
            else:
                print("Invalid visualization argument: " + carg)
                return
        index += 1
    return ax

