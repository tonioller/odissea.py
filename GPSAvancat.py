import json

def toDecimal(g, m, s):
    r = g + m/60 + s/3600
    return r


dataIn = """[
              {"g":41,"m":16, "s":31.386},
              {"g":1, "m":59, "s":13.955},
              {"g":41,"m":16, "s":32.016},
              {"g":1, "m":59, "s":22.999}
          ]
"""          

data = json.loads(dataIn)

for latLong in data:
    print (toDecimal(latLong["g"], latLong["m"],latLong["s"]))
