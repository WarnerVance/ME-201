# Bro this doesn't work at all

def convert_g_to_kg(g):
    return g / 1000
def convert_in_to_cm(inch):
    return inch * 2.54
def convert_cm_to_m(cm):
    return cm / 100
def convert_in_to_m(inch):
    return convert_cm_to_m(convert_in_to_cm(inch))



mass_chassis = convert_g_to_kg(1251)
mass_boom = convert_g_to_kg(39)
mass_crane = mass_chassis + mass_boom
weight_crane = mass_crane * 9.81

x_boom = convert_in_to_m(8.4375)
x_shaft = convert_in_to_m(0.5)
x_out = x_boom + (x_shaft / 2)
x_wheels = convert_in_to_m(6.0625)
m_tip = convert_g_to_kg(345)
w_tip = m_tip * 9.81
t_tip = w_tip * (x_out-(x_wheels/2))

x_cm = t_tip/weight_crane

x_cw_boom = convert_in_to_m(float(input("Distance of the counter weight")))
x_cw = x_cw_boom - x_wheels/2
m_lift = 2.1
w_lift = m_lift * 9.81

x_pulleys = convert_in_to_m(3.55)

t_lift = ((w_lift/2)*(x_out-(x_wheels/2))) + ((w_lift)*(x_out-x_pulleys)-x_wheels/2)

w_cw = (t_lift - (x_cm*weight_crane))/(x_wheels/2+x_cw)
m_cw = w_cw / 9.81


print(m_cw)
