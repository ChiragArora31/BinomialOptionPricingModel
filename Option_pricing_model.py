import streamlit as st

def calculate_option_price(N, S, X, u, d, r, option_type):
    p = round((1 + r - d) / (u - d), 3)
    
    option_prices = [0] * (N + 1)
    for k in range(N + 1):
        if option_type == 'Call':
            option_prices[k] = max(S * (u ** k) * (d ** (N - k)) - X, 0)
        elif option_type == 'Put':
            option_prices[k] = max(X - S * (u ** k) * (d ** (N - k)), 0)

    for i in range(N - 1, -1, -1):
        for k in range(i + 1):
            option_prices[k] = (1 / (1 + r)) * (p * option_prices[k + 1] + (1 - p) * option_prices[k])

    option_price = option_prices[0]
    return round(option_price, 3)

st.title("Binomial Option Pricing Calculator")
option_type = st.radio("Select Option Type:", ('Call', 'Put'))

N_enter = st.number_input("Enter the Number of Periods (N):", min_value=1, max_value=1000, step=1)

S = st.number_input("Enter the Current Market Price of the Asset (S):", min_value=0.00, step=0.01, format="%.4f")
X = st.number_input("Enter the Strike Price of the Asset (X):", min_value=0.00, step=0.01, format="%.4f")
u = st.number_input("Enter the Up-factor (u):", min_value=0.000, step=0.001)
d = st.number_input("Enter the Down-factor (d):", min_value=0.000, step=0.001)
r = st.number_input("Enter the Risk Free Interest Rate per Period (r) in %:", step=0.0001, format="%.4f") / 100

if st.button("Calculate"):
    option_price = calculate_option_price(N_enter, S, X, u, d, r, option_type)
    if option_type == 'Call':
        st.write(f"The European call option price at time T=0 is: {option_price}")
    elif option_type == 'Put':
        st.write(f"The European put option price at time T=0 is: {option_price}")
