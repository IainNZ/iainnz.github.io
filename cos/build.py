import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json

DATA = json.load(open("data.json", "rb"))

output = ""

for chapter_name, chapter in DATA:

    output += "<h4>" + chapter_name + "</h4>\n"
    output += "<ul>\n"

    for location in chapter:
        varname = location["name"].replace("-", "_")
        output += "  <script>\n"
        output += "    var %s = L.marker([%s]).addTo(mymap).bindPopup(\"%s <a href='#%s'>[more]</a>\");\n"%(
            varname, location["latlon"], location["short"], location["name"])
        output += "  </script>\n"
        output += "  <li>\n"
        output += "    <a name='%s'></a>\n"%location["name"]
        output += "    <a href=\"#map\" onclick=\"%s.fire('click')\">[Map]</a>\n"%varname
        output += "    " + location["short"] + "\n"
        output += "    <ul>\n"
        if "long" in location:
            txt = location["long"]
            if "Wikipedia" in txt:
                txt = txt.replace("Wikipedia", "<a href='https://en.wikipedia.org/wiki/%s'>Wikipedia</a>"%location["wiki"])
            output += "      <li>" + txt + "</li>\n"
        output += "    </ul>\n"
        output += "  </li>\n"
        
    
    output += "</ul>\n"

template = open("index.template.html", "rb").read()
open("index.html", "wb").write(template.replace("___CONTENT___", output))
