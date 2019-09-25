import math
r_capsule=float(raw_input('Radius of capsule (m) ==> '))
print r_capsule
h_capsule=float(raw_input('Height of capsule (m) ==> '))
print h_capsule
r_reservoir=float(raw_input('Radius of oxygen reservoir (m) ==> '))
print r_reservoir
h_reservoir=float(raw_input('Height of oxygen reservoir (m) ==> '))
print h_reservoir
def volume_cone(radius, height):
    volume_cone=math.pi*radius**2*height/3
    return volume_cone
v_cone=volume_cone(r_capsule, h_capsule)
total_oxygen=v_cone*0.21*0.41*300
print 'Oxygen needed for the trip is %.3fm^3'%total_oxygen
def volume_cylinder(radius, height):
    volume_cylinder=math.pi*radius**2*height
    return volume_cylinder
oxygen_cylinder=volume_cylinder(r_reservoir, h_reservoir)*210
print 'Each cylinder holds %.3fm^3 at 3000 psi'%oxygen_cylinder
number_tanks=math.ceil(total_oxygen/oxygen_cylinder)
print 'The trip will require %d reservoir tanks.'%number_tanks