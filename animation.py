# Gravitational constant
G = 6.67e-11

# Initial positions
initial_pos_star1 = vector(-4e11, 0, 0)
initial_pos_star2 = vector(4e11, 0, 0)
initial_pos_planet = vector(7e11, 0, 0)

# Initial velocities
initial_vel_planet = vector(0, 0, 1e2)

# Create stars and planet
star1 = sphere(pos=initial_pos_star1, radius=8e10, color=color.yellow, make_trail=True, interval=10, retain=50)
star1.mass = 6e30
star1.p = vector(0, 0, 1e4) * star1.mass

star2 = sphere(pos=initial_pos_star2, radius=4e10, color=color.blue, make_trail=True)
star2.mass = 3e30
star2.p = -star1.p

planet = sphere(pos=initial_pos_planet, radius=2e10, color=color.green, make_trail=True, trail_type="points", interval=10, retain=50)
planet.mass = 1e24
planet.p = initial_vel_planet * planet.mass

#Time step
dt = 1e5


while True:
    rate(150)
  
    # Calculate distance and gravitational force between stars
    distance = star2.pos - star1.pos
    force_stars = G * star1.mass * star2.mass * distance.hat / mag(distance)**2

    # Update momenta of stars
    star1.p = star1.p + force_stars * dt
    star2.p = star2.p - force_stars * dt
    
    # Calculate distances and gravitational forces between star1, star2, and planet
    dist_star1_planet = star1.pos - planet.pos
    dist_star2_planet = star2.pos - planet.pos

    force_star1_planet = G * star1.mass * planet.mass * dist_star1_planet.hat / mag(dist_star1_planet)**2
    force_star2_planet = G * star2.mass * planet.mass * dist_star2_planet.hat / mag(dist_star2_planet)**2

    total_force_planet = force_star1_planet + force_star2_planet

    # Update momentum of planet
    planet.p = planet.p + total_force_planet * dt
    
    # Update positions of stars and planet
    star1.pos = star1.pos + (star1.p / star1.mass) * dt
    star2.pos = star2.pos + (star2.p / star2.mass) * dt
    planet.pos = planet.pos + (planet.p / planet.mass) * dt
