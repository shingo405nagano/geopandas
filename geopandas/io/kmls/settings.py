from dataclasses import asdict
from dataclasses import dataclass
from typing import Dict

SIMPLE_XMLNS = "http://www.opengis.net/kml/2.2"


# Tag names used in KML.
@dataclass
class Tags:
    alpha: str = "alpha"
    altitude_mode: str = "altitudeMode"
    balloon_style: str = "BalloonStyle"
    color: str = "color"
    coordinates: str = "coordinates"
    data: str = "Data"
    display_name: str = "displayName"
    document: str = "Document"
    extended_data: str = "ExtendedData"
    extrude: str = "extrude"
    fill: str = "fill"
    highlight_style: str = "highlight"
    href: str = "href"
    icon: str = "Icon"
    icon_style: str = "IconStyle"
    id: str = "id"
    inner_boundary_is: str = "innerBoundaryIs"
    key: str = "key"
    label_style: str = "LabelStyle"
    linestring: str = "LineString"
    line_style: str = "LineStyle"
    linearring: str = "LinearRing"
    multi_geometry: str = "MultiGeometry"
    name: str = "name"
    normal_style: str = "normal"
    outer_boundary_is: str = "outerBoundaryIs"
    outline: str = "outline"
    pair: str = "Pair"
    placemark: str = "Placemark"
    point: str = "Point"
    polygon: str = "Polygon"
    poly_style: str = "PolyStyle"
    scale: str = "scale"
    style: str = "Style"
    style_map: str = "StyleMap"
    style_url: str = "styleUrl"
    tessellate: str = "tessellate"
    value: str = "value"
    width: str = "width"


# AltitudeMode tag names used in KML.
@dataclass
class AltitudeMode:
    # Indicates to ignore an altitude specification.
    clamp_to_ground: str = "clampToGround"
    # Sets the altitude of the element relative to the actual ground elevation of a particular location.
    relative_to_ground: str = "relativeToGround"
    # Sets the altitude of the coordinate relative to sea level, regardless of the actual elevation of the terrain beneath the element.
    absolute: str = "absolute"

    @property
    def asdict(self) -> Dict[str, str]:
        return asdict(self)


# URL of Icon that can be displayed in Google Earth.
# Google Earth Icons -> https://kml4earth.appspot.com/icons.html#google_vignette
@dataclass
class Icons:
    airports: str = "http://maps.google.com/mapfiles/kml/shapes/airports.png"
    arrows: str = "http://maps.google.com/mapfiles/kml/shapes/arrow.png"
    bus: str = "http://maps.google.com/mapfiles/kml/shapes/bus.png"
    cabs: str = "http://maps.google.com/mapfiles/kml/shapes/cabs.png"
    camera: str = "http://maps.google.com/mapfiles/kml/shapes/camera.png"
    caution: str = "http://maps.google.com/mapfiles/kml/shapes/caution.png"
    coffee: str = "http://maps.google.com/mapfiles/kml/shapes/coffee.png"
    cycling: str = "http://maps.google.com/mapfiles/kml/shapes/cycling.png"
    dining: str = "http://maps.google.com/mapfiles/kml/shapes/dining.png"
    dollar: str = "http://maps.google.com/mapfiles/kml/shapes/dollar.png"
    firedept: str = "http://maps.google.com/mapfiles/kml/shapes/firedept.png"
    forbidden: str = "http://maps.google.com/mapfiles/kml/shapes/forbidden.png"
    gas_station: str = "http://maps.google.com/mapfiles/kml/shapes/gas_stations.png"
    homegardenbusiness: str = (
        "http://maps.google.com/mapfiles/kml/shapes/homegardenbusiness.png"
    )
    hospitals: str = "http://maps.google.com/mapfiles/kml/shapes/hospitals.png"
    info: str = "http://maps.google.com/mapfiles/kml/shapes/info-i.png"
    lodging: str = "http://maps.google.com/mapfiles/kml/shapes/lodging.png"
    man: str = "http://maps.google.com/mapfiles/kml/shapes/man.png"
    parking: str = "http://maps.google.com/mapfiles/kml/shapes/parking_lot.png"
    parks: str = "http://maps.google.com/mapfiles/kml/shapes/parks.png"
    phone: str = "http://maps.google.com/mapfiles/kml/shapes/phone.png"
    circle: str = "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png"
    square: str = "http://maps.google.com/mapfiles/kml/shapes/placemark_square.png"
    rail: str = "http://maps.google.com/mapfiles/kml/shapes/rail.png"
    shopping: str = "http://maps.google.com/mapfiles/kml/shapes/shopping.png"
    snack_bar: str = "http://maps.google.com/mapfiles/kml/shapes/snack_bar.png"
    toilets: str = "http://maps.google.com/mapfiles/kml/shapes/toilets.png"
    truck: str = "http://maps.google.com/mapfiles/kml/shapes/truck.png"
    yen: str = "http://maps.google.com/mapfiles/kml/shapes/yen.png"
    blue_pushpin: str = "http://maps.google.com/mapfiles/kml/pushpin/blue-pushpin.png"
    green_pushpin: str = "http://maps.google.com/mapfiles/kml/pushpin/grn-pushpin.png"
    lightblue_pushpin: str = (
        "http://maps.google.com/mapfiles/kml/pushpin/ltblu-pushpin.png"
    )
    pink_pushpin: str = "http://maps.google.com/mapfiles/kml/pushpin/pink-pushpin.png"
    purple_pushpin: str = (
        "http://maps.google.com/mapfiles/kml/pushpin/purple-pushpin.png"
    )
    red_pushpin: str = "http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png"
    white_pushpin: str = "http://maps.google.com/mapfiles/kml/pushpin/wht-pushpin.png"
    yellow_pushpin: str = "http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png"
    church: str = "http://maps.google.com/mapfiles/kml/pal2/icon11.png"
    tree: str = "http://maps.google.com/mapfiles/kml/pal2/icon12.png"
    buillding: str = "http://maps.google.com/mapfiles/kml/pal3/icon21.png"
    red_cross: str = "http://maps.google.com/mapfiles/kml/pal3/icon46.png"
    hazard: str = "http://maps.google.com/mapfiles/kml/pal3/icon47.png"
    home: str = "http://maps.google.com/mapfiles/kml/pal3/icon56.png"
    camera_color: str = "http://maps.google.com/mapfiles/kml/pal4/icon46.png"
    search: str = "http://maps.google.com/mapfiles/kml/pal4/icon0.png"
    signal: str = "http://www.google.com/mapfiles/traffic.png"


# If matplotlib is not installed, select colors here.
NAMED_COLORS = {
    "tomato": "#ff6347",
    "teal": "#008b8b",
    "royalblue": "#4169e1",
    "firebrick": "#b22222",
    "seagreen": "#2e8b57",
    "dodgerblue": "#1e90ff",
    "red": "#ff0000",
    "green": "#00ff00",
    "blue": "#0000ff",
    "gold": "#ffa500",
    "lime": "#00ff00",
    "cyan": "#00ffff",
    "maroon": "#800000",
    "olive": "#808000",
    "indigo": "#4b0082",
    "crimson": "#dc143c",
    "yellowgreen": "#9acd32",
    "navy": "#000080",
    "pink": "#ffc0cb",
    "skyblue": "#87ceeb",
    "springgreen": "#00ff7f",
    "magenta": "#ff00ff",
    "yellow": "#ffff00",
    "brown": "#a52a2a",
    "steelblue": "#4682b4",
    "violet": "#ee82ee",
    "white": "#ffffff",
    "gray": "#808080",
    "black": "#000000",
}
