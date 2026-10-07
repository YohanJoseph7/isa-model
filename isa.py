def density(h):
    """Returns ISA air density in kg/m^3 at altitude h in metres."""
    rho_SL = 1.225
    return rho_SL * (1 - 2.2558e-5 * h) ** 4.2561

def temperature(h):
    """Returns ISA temperature in Kelvin at altitude h in metres."""
    T0 = 288.15
    L  = 0.0065
    return T0 - L * h
