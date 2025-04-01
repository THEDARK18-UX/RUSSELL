import streamlit as st
from sympy import symbols, Eq, solve

def balance_combustion(formula):
    # Extraer número de carbonos e hidrógenos
    import re
    match = re.match(r'C(\d*)H(\d*)', formula)
    if not match:
        return "Formato incorrecto. Usa CxHy"
    
    C = int(match.group(1)) if match.group(1) else 1
    H = int(match.group(2)) if match.group(2) else 1
    O = symbols('O')
    
    # Balancear ecuaciones
    x, y, z = symbols('x y z')
    eq1 = Eq(x, C)   # Carbono
    eq2 = Eq(2*y, H) # Hidrógeno
    eq3 = Eq(2*z, x + y)  # Oxígeno
    sol = solve((eq1, eq2, eq3), (x, y, z))
    
    return f"{formula} + {sol[z]} O2 → {sol[x]} CO2 + {sol[y]} H2O"

st.title("Balanceo de Combustión de Hidrocarburos")
formula = st.text_input("Ingresa la fórmula del hidrocarburo (Ejemplo: C2H6)")
if formula:
    resultado = balance_combustion(formula)
    st.write(resultado)
