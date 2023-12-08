import streamlit as st
from numpy.random import RandomState
from numpy.random import normal
from numpy.random import uniform
from numpy.random import poisson
from numpy.random import binomial
from central_limit_theorem import get_sample_mean
from central_limit_theorem import plot_histogram


rng = RandomState(999)

def main():
    st.title("Experiment: Central Limit Theorem")
    st.write("### Experiment setup")
    col1, col2 = st.columns(2)
    with col1:
        n_samples = st.slider("Number of samples", min_value=1, max_value=500, value=1, step=5)
    with col2:
        n_times = st.slider("Number of repeats", min_value=1, max_value=500, value=1, step=5)

    params = {}
    with st.sidebar:
        options = ["Normal", "Uniform", "Poisson", "Binomial"]
        distribution = st.selectbox("Choose a distribution", options)

        st.write("Choose the distribution parameters")
        if distribution == "Normal":
            params["loc"] = st.slider("Mean", min_value=-100, max_value=100, value=0)
            params["scale"] = st.slider("Standard deviation", min_value=1, max_value=5, value=1)
            sampler = rng.normal

        elif distribution == "Uniform":
            params["low"] = st.slider("Min", min_value=1, max_value=100, value=50)
            params["high"] = st.slider("Max", min_value=params["low"]+1, max_value=101, value=params["low"]+1)
            sampler = rng.uniform

        elif distribution == "Poisson":
            params["lam"] = st.slider("Lambda", min_value=0.01, max_value=10.0, value=0.5)
            sampler = rng.poisson

        elif distribution == "Binomial":
            params["p"] = st.slider("Probability", min_value=0.01, max_value=1.0, value=0.5)
            params["n"] = n_samples
            sampler = rng.binomial

        samples_of_mean = [
            get_sample_mean(sampler, params, n_samples)
            for _ in range(n_times)
        ]
        fig = plot_histogram(samples_of_mean)

    st.pyplot(fig)
    

if __name__ == "__main__":
    main()
