
def static_map_importer():
    staticmap = ""
    with open("static-ips.csv") as file_read:
        lines = file_read.readlines()
        for line in lines:
            line = line.strip()
            items = line.split(",")
            if len(items) > 1:
                if items[0] != "MAC" and items[1] != "IP":
                    mac = items[0].strip()
                    ip = items[1].strip()
                    description = items[2].strip()
                    hostname = items[3].strip()
                    staticmap_item = f"<staticmap><mac>{mac}</mac><ipaddr>{ip}</ipaddr><hostname>{hostname}</hostname><descr><![CDATA[{description}]]></descr></staticmap>"
                    staticmap += staticmap_item
    with open("static-map.xml", "w") as file_write:
        file_write.write(staticmap)
    return staticmap

print(static_map_importer())
