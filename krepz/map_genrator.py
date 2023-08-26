import folium
import folium.plugins.fullscreen


def create_map():
    m = folium.Map(location=[59.735870, 10.230375], zoom_start=4, min_zoom=3, max_zoom=22)
    # tile = folium.TileLayer( tiles="Stamen Toner", max_native_zoom=22, max_zoom=22)
    thunder = folium.TileLayer(
        tiles="https://tile.thunderforest.com/spinal-map/{z}/{x}/{y}.png?apikey=f2ff80f6355c4d80a34d958224b1b454",
        attr="spinal", max_native_zoom=22, max_zoom=22, min_zoom=3)
    # tile.add_to(m)
    thunder.add_to(m)
    m = quests(m)
    m = artifacts(m)
    m = points_interest(m)
    fs = folium.plugins.Fullscreen(position='topleft', title='Full Screen', title_cancel='Exit Full Screen',
                                   force_separate_button=False)
    m.add_child(fs)
    m = m._repr_html_()
    return m




def quests(map):
    quest_titles = ["Trial of Companionship", "Trial of Fire", "Trial of Accuracy", "Trial of Strength",
                    "Trial of Endurance"]
    quest_locations = [[59.829475, 10.240137], [59.829083, 10.239603], [59.829306, 10.241166], [59.829132, 10.239455],
                       [59.827051, 10.234826]]
    icon_image = "https://wowchallenges.com/images/questionmark.png"

    for title, location in zip(quest_titles, quest_locations):
        i = folium.features.CustomIcon(icon_image, icon_size=(20, 20))
        popup = folium.Popup(f'<p style="color:black;">{title} </p>')
        mk = folium.Marker(location=location, icon=i, popup=popup)
        mk.add_to(map)

    return map


def artifacts(map):
    location = [[59.828392, 10.237148], [59.830808, 10.242754], [59.830229, 10.245778], [59.829411, 10.240839]]
    icon_image = 'https://cdn-icons-png.flaticon.com/512/4230/4230567.png'
    for location in location:
        i = folium.features.CustomIcon(icon_image, icon_size=(20, 20))
        mk = folium.Marker(location=location, icon=i)
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


def points_interest(map):
    icon_image = "https://cdn-icons-png.flaticon.com/512/4261/4261211.png"
    popup_text = "<div> <p>The residence of Lord Frank, father of the infamous Duke Mørgen Jortensne</p></div>"
    location = [59.781611, 10.225372]
    i = folium.features.CustomIcon(icon_image, icon_size=(20, 20))
    mk = folium.Marker(location=location, icon=i, popup=popup_text)
    mk.add_to(map)
    return map
