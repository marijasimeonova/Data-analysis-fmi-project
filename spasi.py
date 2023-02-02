import json
import matplotlib.pyplot as plt

def read_from_file(filename, year):
    with open(filename, 'r', encoding="utf8") as f:
        data = json.load(f)
        
    data.pop(0)
    if year == 2021:
        data.pop(0)
    bel_mp = {}
    bel_cities = {}

    math_mp = {}
    math_cities = {}
    for i in data:
        city = i[0]

        bel_num = int(i[5])
        if bel_num == 0:
            continue
        bel_avg = float(i[6].replace(',','.'))

        oldval = bel_mp.get(city, 0)
        newval = oldval + bel_num * bel_avg

        bel_mp[city] = newval

        oldcityval = bel_cities.get(city, 0)
        bel_cities[city] = oldcityval + bel_num

        oldmath = math_mp.get(city, 0)
        math_num = int(i[7])
        if  math_num == 0:
            continue
        math_avg = float(i[8].replace(',','.'))
        newmath = oldmath + math_num * math_avg
        math_mp[city] = newmath
        oldcityval = math_cities.get(city, 0)
        math_cities[city] = oldcityval + math_num

    final_bels = {}
    final_maths = {}
   
    for city in bel_cities:
        city_avg = bel_mp[city] / bel_cities[city]
        final_bels[city] = city_avg
    for city in math_cities:
        city_avg = math_mp[city] / math_cities[city]
        final_maths[city] = city_avg
        
    print ("BEL:")
    for city, avg in final_bels.items():
        print (city, avg)

    print("MATH")
    for city, avg in final_maths.items():
        print (city, avg)

    return (final_bels, final_maths)

final_bels_2019, final_maths_2019 = read_from_file('spasi/rezultati-2019.json', 2019)
final_bels_2021, final_maths_2021 = read_from_file('spasi/rezultati-2021.json', 2021)

fb1_2019 = list(final_bels_2019.keys())[:10]
fbv1_2019 = list(final_bels_2019.values())[:10]
fb1_2021 = list(final_bels_2021.keys())[:10]
fbv1_2021 = list(final_bels_2021.values())[:10]
fb2_2019 = list(final_bels_2019.keys())[10:20]
fbv2_2019 = list(final_bels_2019.values())[10:20]
fb2_2021 = list(final_bels_2021.keys())[10:20]
fbv2_2021 = list(final_bels_2021.values())[10:20]
fb3_2019 = list(final_bels_2019.keys())[20:]
fbv3_2019 = list(final_bels_2019.values())[20:]
fb3_2021 = list(final_bels_2021.keys())[20:]
fbv3_2021 = list(final_bels_2021.values())[20:]


#final bels
plt.plot(fb1_2019,fbv1_2019, label="2019")
plt.plot(fb1_2021, fbv1_2021, label="2021")

# plt.plot(fb2_2019, fbv2_2019, label="2019")
# plt.plot(fb2_2021, fbv2_2021, label="2021")

# plt.plot(fb3_2019, fbv3_2019, label="2019")
# plt.plot(fb3_2021, fbv3_2021, label="2021")


fm1_2019 = list(final_maths_2019.keys())[:10]
fmv1_2019 = list(final_maths_2019.values())[:10]
fm1_2021 = list(final_maths_2021.keys())[:10]
fmv1_2021 = list(final_maths_2021.values())[:10]
fm2_2019 = list(final_maths_2019.keys())[10:20]
fmv2_2019 = list(final_maths_2019.values())[10:20]
fm2_2021 = list(final_maths_2021.keys())[10:20]
fmv2_2021 = list(final_maths_2021.values())[10:20]
fm3_2019 = list(final_maths_2019.keys())[20:]
fmv3_2019 = list(final_maths_2019.values())[20:]
fm3_2021 = list(final_maths_2021.keys())[20:]
fmv3_2021 = list(final_maths_2021.values())[20:]

#final maths
# plt.plot(fm1_2019,fmv1_2019, label="2019")
# plt.plot(fm1_2021, fmv1_2021, label="2021")

# plt.plot(fm2_2019, fmv2_2019, label="2019")
# plt.plot(fm2_2021, fmv2_2021, label="2021")


# plt.plot(fm3_2019, fmv3_2019, label="2019")
# plt.plot(fm3_2021, fmv3_2021, label="2021")

plt.legend(loc='upper left')
plt.title('Среден успех БЕЛ')
# plt.title('Среден успех МАТЕМАТИКА')
plt.show()
