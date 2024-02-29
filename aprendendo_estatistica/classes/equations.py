import streamlit as st

class StatisticsEquations:
    @staticmethod
    def mean():
        return st.latex(r"\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i")

    @staticmethod
    def median():
        return st.latex(r"Me = \begin{cases} x_{\frac{n+1}{2}}, & \text{se } n \text{ é ímpar} \\ \frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2}, & \text{se } n \text{ é par} \end{cases}")

    @staticmethod
    def mode():
        return st.latex(r"\text{Moda} = \text{valor que mais se repete}")

    @staticmethod
    def range():
        return st.latex(r"\text{Amplitude} = x_{\text{máximo}} - x_{\text{mínimo}}")

    @staticmethod
    def variance():
        return st.latex(r"\text{Variância} = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2")

    @staticmethod
    def standard_deviation():
        return st.latex(r"\text{Desvio Padrão} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}")

    @staticmethod
    def interquartile_range():
        return st.latex(r"\text{Intervalo Interquartil} = IQR = Q_3 - Q_1")

    @staticmethod
    def quartile_1():
        return st.latex(r"Q_1 = x_{\frac{n+1}{4}}")

    @staticmethod
    def quartile_3():
        return st.latex(r"Q_3 = x_{\frac{3(n+1)}{4}}")
