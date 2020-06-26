from Sensing.Wireless.Bluetooth import Bluetooth

path = r"R:\3-2\datasets\Student_life_dataset\dataset\sensing\bluetooth\bt_u00.csv"
bt = Bluetooth(path)

print(bt.get_no_ppl())

x = bt.get_no_ppl()
sum = 0
for key in x:
    sum+= x[key]

print(sum)



