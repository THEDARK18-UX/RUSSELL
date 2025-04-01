import streamlit as st

def balance_combustion(formula):
    import re
    match = re.match(r'C(\d*)H(\d*)', formula)
    if not match:
        return "Formato incorrecto. Usa CxHy"
    
    C = int(match.group(1)) if match.group(1) else 1
    H = int(match.group(2)) if match.group(2) else 1
    
    # Balanceo basado en proporciones estequiométricas
    CO2 = C
    H2O = H // 2
    O2 = (CO2 * 2 + H2O) / 2
    
    return f"{formula} + {O2} O2 → {CO2} CO2 + {H2O} H2O"

st.title("Balanceo de Combustión de Hidrocarburos")
formula = st.text_input("Ingresa la fórmula del hidrocarburo (Ejemplo: C2H6)")
if formula:
    resultado = balance_combustion(formula)
    st.write(resultado)
