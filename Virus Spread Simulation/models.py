import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

def SIR(sbx_healthy, sbx_infected, sbx_days, sbx_propagation, sbx_r_chance):

    N0 = sbx_healthy.value()
    # Initial number of infected
    I0 = sbx_infected.value()
    # Days to run
    D0 = sbx_days.value()

    # Contact rate
    beta = sbx_propagation.value() / 100
    # recovery rate
    gamma = sbx_r_chance.value() / 100

    # recovered individuals
    R0 = 0

    # work out susceptible
    S0 = N0 - I0 - R0
    # A grid of time points (in days)
    t = np.linspace(0, D0, D0)

    # The SIR model differential equations
    def deriv(y, t, N0, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N0
        dIdt = beta * S * I / N0 - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    # Initial conditions vector
    y0 = S0, I0, R0
    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N0, beta, gamma))
    S, I, R = ret.T

    # ------------------------------------GRAPHS----------------------------#

    # Plot the data
    fig, axs = plt.subplots(2, 2)
    # TOP LEFT plot---------------------------------------------------------
    plt.setp(axs[0, 0], xlabel="Time (Days)")
    plt.setp(axs[0, 0], ylabel="Population (Devices)")
    axs[0, 0].grid()

    axs[0, 0].plot(t, S, 'b', label='Susceptible', color='tab:blue')
    axs[0, 0].plot(t, I, 'r', linestyle='--', label='Infected', color='tab:orange')
    axs[0, 0].plot(t, R, 'g', label='Recovered & protected', color='tab:green')

    legend = axs[0, 0].legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        axs[0, 0].spines[spine].set_visible(False)

    axs[0, 0].legend(['Susceptible', 'Infected', 'Recovered & Protected'], loc='lower center',
                     ncol=1, fancybox=True, bbox_to_anchor=(0.87, 0.70))

    # TOP Right plot---------------------------------------------------------

    labels = 'Susceptible', 'Infected', 'Recovered & protected'
    colors = ['tab:blue', 'tab:orange', 'tab:green']

    sizes = [S[-1], I[-1], R[-1]]

    axs[0, 1].pie(sizes, labels=labels, wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': 'white'},
                  autopct='%1.1f%%', pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)

    axs[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Bottom Right plot---------------------------------------------------------

    # axs[1, 1].set_title("",fontweight="bold")

    # Bottom Left plot----------------------------------------------------------

    # axs[1, 0].set_title("", fontweight="bold")

    # --------------------------------------------------------------------------------------------------------------------

    plt.show()