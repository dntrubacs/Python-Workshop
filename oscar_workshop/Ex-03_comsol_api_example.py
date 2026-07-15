import numpy as np
import matplotlib.pyplot as plt

# IMPORTANT: You must install the `mph` library via pip: `pip install mph`
# MPh uses JPype to talk to COMSOL's native Java API, making it much more Pythonic.



import mph


client = mph.start()
model = client.load('scattering_nanosphere.mph')

print(client.names())

print(client.models())



# Inspecting models
print(model.parameters())

for (name, value) in model.parameters().items():
    description = model.description(name)
    print(f'{description:20} {name} = {value}')

print(model.materials())

print(model.physics())

print(model.studies())


# Modifying parameters

print(model.parameter('r0'))

r0 = model.parameter('r0', evaluate=True)
t_air = model.parameter('t_air', evaluate=True)

(x, y, z, E) = model.evaluate(['x', 'y', 'z', 'ewfd.normE'])

def plot_efield(r0, t_air, x, y, z, E):
    radius = np.sqrt(x**2 + y**2 + z**2)

    # 3. Create a mask to keep only the points inside the air and inner sphere
    # We want everything where radius <= (r0 + t_air)
    valid_region = radius <= (float(r0) + float(t_air))

    # 4. Filter your data arrays using the mask
    x_core = x[valid_region]
    y_core = y[valid_region]
    z_core = z[valid_region]
    E_core = E[valid_region]

    # 5. Plot the filtered 3D scatter
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    sc = ax.scatter(x_core, y_core, z_core, c=E_core, cmap='viridis', s=1, alpha=0.3)

    plt.colorbar(sc, label='Electric Field Norm (V/m)', pad=0.1)
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_zlabel('z (m)')
    ax.set_title('3D Electric Field (PML Excluded)')

    # Keeps the sphere looking spherical
    ax.set_box_aspect([1, 1, 1])

    plt.show()

plot_efield(r0, t_air, x, y, z, E)

model.parameter('r0', '200[nm]')

print(model.parameter('r0'))

print(model.geometries())


# Running simulations

# Build the mesh
model.mesh()

model.solve()

(x, y, z, E) = model.evaluate(['x', 'y', 'z', 'ewfd.normE'])

r0 = model.parameter('r0', evaluate=True)

# plot_efield(r0, t_air, x, y, z, E)

print(E.max())

imax = E.argmax()

print(x[imax], y[imax], z[imax])

model.save('scattering_nanosphere_solved.mph')





