# Import statements
import geopandas as gpd
import geoplot as gplt


def init(width, height, edgeColor, faceColor):
    boston = (-71.2, 42.2, -70.9, 42.4)
    boston_neighborhoods = gpd.read_file('datasets/Boston_Neighborhoods.geojson')

    return gplt.polyplot(boston_neighborhoods, extent=boston, edgecolor=edgeColor, facecolor=faceColor,
                         figsize=(width, height))


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


def add_polling_locations(ax, color):
    polling_locations = gpd.read_file('datasets/Polling_Locations.geojson')
    ax = polling_locations.plot(ax=ax, color=color)
    return ax
