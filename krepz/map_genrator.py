import folium


def create_map():
    m = folium.Map(location=[59.829810, 10.239877], zoom_start=16, min_zoom=6, max_zoom=22)
    # tile = folium.TileLayer( tiles="Stamen Toner", max_native_zoom=22, max_zoom=22)
    thunder = folium.TileLayer(
        tiles="https://tile.thunderforest.com/spinal-map/{z}/{x}/{y}.png?apikey=f2ff80f6355c4d80a34d958224b1b454",
        attr="spinal", max_native_zoom=22, max_zoom=22, min_zoom=6)
    # tile.add_to(m)
    thunder.add_to(m)
    m = quests(m)
    m = easter_egg(m)
    m = m._repr_html_()
    return m


def quests(map):

    quest_titles = ["Test of Strength", "Test of Endurance", "Test of Faith", "Test of Time"]
    quest_locations = [[59.829342, 10.241066], [59.829169, 10.239305], [59.829896, 10.240092], [59.828633, 10.237008]]
    icon_image = "https://wowchallenges.com/images/questionmark.png"

    for title, location in zip(quest_titles, quest_locations):
        i = folium.features.CustomIcon(icon_image, icon_size=(20,20))
        mk = folium.Marker(location=location, icon=i, popup=title)
        mk.add_to(map)

    return map

def easter_egg(map):
    icon_image = "https://static.vecteezy.com/system/resources/previews/016/398/117/original/easter-eggs-cartoon-style-easter-eggs-paschal-eggs-image-as-cartoon-colorful-style-for-the-christian-feast-of-easter-which-celebrates-the-resurrection-of-jesus-free-png.png"
    popup_text = "6-1-3"
    location = [-27.120656, -109.363000]
    i = folium.features.CustomIcon(icon_image, icon_size=(30, 30))
    mk = folium.Marker(location=location, icon=i, popup=popup_text)
    mk.add_to(map)
    return map


