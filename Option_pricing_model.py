import streamlit as st

def calculate_option_price(N, S, X, u, d, r):
    p = round((1 + r - d) / (u - d), 3)
    
    option_prices = [0] * (N + 1)
    for k in range(N + 1):
        option_prices[k] = max(S * (u ** k) * (d ** (N - k)) - X, 0)

    for i in range(N - 1, -1, -1):
        for k in range(i + 1):
            option_prices[k] = (1 / (1 + r)) * (p * option_prices[k + 1] + (1 - p) * option_prices[k])

    option_price = option_prices[0]
    return round(option_price, 3)
st.title("Binomial Option Pricing Calculator")
N_enter = st.number_input("Enter the Number of Periods (N):", min_value=1, max_value=500, step=1)
N = st.slider("Select the Number of Periods (N):", min_value=1, max_value=500, step=1, value=N_enter)

N = N = st.slider("Select the Number of Periods (N):", min_value=1, max_value=30, step=1)
S = st.number_input("Enter the Current Market Price of the Asset (S):", min_value=0.00, step=0.01)
X = st.number_input("Enter the Strike Price of the Asset (X):", min_value=0.00, step=0.01)
u = st.number_input("Enter the Up-factor (u):", min_value=0.000, step=0.001)
d = st.number_input("Enter the Down-factor (d):", min_value=0.000, step=0.001)
r = st.number_input("Enter the Risk Free Interest Rate per Period (r) in %:", min_value=-100.00, step=0.01) / 100

if st.button("Calculate"):
    option_price = calculate_option_price(N, S, X, u, d, r)
    st.write(f"The European option price at time T=0 is: {option_price}")

