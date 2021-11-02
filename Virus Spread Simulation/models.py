import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

def SIR(sbx_healthy, sbx_infected, sbx_days, sbx_propagation, sbx_r_chance):
    #Starting Susceptible
    N0 = sbx_healthy.value()
    # Initial number of infected
    I0 = sbx_infected.value()
    #Total Population
    P0 = I0 + N0

    # Days to run
    D0 = sbx_days.value()
    # Contact rate
    beta = int(sbx_propagation.value()) / 100
    # recovery rate
    gamma = int(sbx_r_chance.value()) / 100

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
    fig, axs = plt.subplots(2, 2,figsize=(15.3, 7.9))
    # TOP LEFT plot---------------------------------------------------------
    axs[0, 0].set_title("Timeline",fontweight="bold")
    try:
        plt.setp(axs[0, 0], xlabel="Time (Days)")
        plt.setp(axs[0, 0], ylabel="Population (Devices)")
        axs[0, 0].grid()

        axs[0, 0].plot(t, S, label='Susceptible', color='tab:blue')
        axs[0, 0].plot(t, I, linestyle='--', label='Infected', color='tab:orange')
        axs[0, 0].plot(t, R, label='Recovered & protected', color='tab:green')

        legend = axs[0, 0].legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            axs[0, 0].spines[spine].set_visible(False)

        axs[0, 0].legend(['Susceptible', 'Infected', 'Recovered'], loc='best',
                         ncol=1, fancybox=True)
    except Exception as e:
        print(e)

    # TOP Right plot---------------------------------------------------------
    axs[0, 1].set_title("Final Stats on day {}".format(D0),fontweight="bold")
    try:

        labels = 'Susceptible', 'Infected', 'Recovered'

        colors = ['tab:blue', 'tab:orange', 'tab:green']

        sizes = [S[-1]/P0*100, I[-1]/P0*100, R[-1]/P0*100]


        labels = [f'{l} | {s:0.1f}%' for l, s in zip(labels, sizes)]

        axs[0, 1].pie(sizes, wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': 'white'},
                      pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)

        axs[0, 1].legend(labels, loc="best")

        axs[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    except Exception as e:
        print(e)

    # Bottom Right plot---------------------------------------------------------

    axs[1, 1].set_title("TBD",fontweight="bold")

    # Bottom Left plot----------------------------------------------------------

    axs[1, 0].set_title("TBD", fontweight="bold")

    # --------------------------------------------------------------------------------------------------------------------

    #plt.subplots_adjust(left=0.06, bottom=0.055, right=0.98, top=0.97, wspace=0.2, hspace=0.2)
    plt.tight_layout()
    plt.savefig("fig_temp.png",transparent=True)


def SIRD(sbx_healthy, sbx_infected, sbx_days, sbx_propagation, sbx_r_chance,sbx_mortality):
    #Starting Susceptible
    N0 = sbx_healthy.value()
    # Initial number of infected
    I0 = sbx_infected.value()

    # Total Population
    P0 = I0 + N0

    # Days to run
    D0 = sbx_days.value()
    # Contact rate
    beta = int(sbx_propagation.value()) / 100
    # recovery rate
    gamma = int(sbx_r_chance.value()) / 100

    #mortality
    mu = int(sbx_mortality.value()) / 100
    #mu = 1 / 100


    # start recovered individuals
    R0 = 0
    # start Dead individuals
    Dd0 = 0
    # work out susceptible
    S0 = N0 - I0 - R0
    # A grid of time points (in days)
    t = np.linspace(0, D0, D0)

    def deriv(y, t, N0, beta, gamma,mu):
        S, I, R, D = y
        dSdt = -beta * S * I / N0
        dIdt = beta * S * I / N0 - gamma * I - mu * I
        dRdt = gamma * I
        dDdt = mu * I
        return dSdt, dIdt, dRdt, dDdt

    # Initial conditions vector
    y0 = S0, I0, R0, Dd0
    # Integrate the SIRD equations over the time grid, t.

    ret = odeint(deriv, y0, t, args=(N0, beta, gamma, mu))
    S, I, R, D = ret.T


    # ------------------------------------GRAPHS----------------------------#

    # Plot the data
    fig, axs = plt.subplots(2, 2,figsize=(15.3, 7.9))


    # TOP LEFT plot---------------------------------------------------------
    axs[0, 0].set_title("Timeline", fontweight="bold")
    try:
        plt.setp(axs[0, 0], xlabel="Time (Days)")
        plt.setp(axs[0, 0], ylabel="Population (Devices)")
        axs[0, 0].grid()

        axs[0, 0].plot(t, S, label='Susceptible', color='tab:blue')
        axs[0, 0].plot(t, I, linestyle='--', label='Infected', color='tab:orange')
        axs[0, 0].plot(t, R, label='Recovered & protected', color='tab:green')
        axs[0, 0].plot(t, D, label='Dead', color='crimson')

        legend = axs[0, 0].legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            axs[0, 0].spines[spine].set_visible(False)

        axs[0, 0].legend(['Susceptible', 'Infected', 'Recovered','Dead'], loc='best',
                         ncol=1, fancybox=True)
    except Exception as e:
        print(e)

    # TOP Right plot---------------------------------------------------------
    axs[0, 1].set_title("Final Stats on day {}".format(D0), fontweight="bold")
    try:
        labels = 'Susceptible', 'Infected', 'Recovered', 'Dead'
        colors = ['tab:blue', 'tab:orange', 'tab:green','crimson']

        sizes = [S[-1] / P0 * 100, I[-1] / P0 * 100, R[-1] / P0 * 100, D[-1]/N0*100]

        labels = [f'{l} | {s:0.1f}%' for l, s in zip(labels, sizes)]

        axs[0, 1].pie(sizes, wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': 'white'},
                      pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)

        axs[0, 1].legend(labels, loc="best")

        axs[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    except Exception as e:
        print(e)

    # Bottom Right plot---------------------------------------------------------

    axs[1, 1].set_title("TBD", fontweight="bold")

    # Bottom Left plot----------------------------------------------------------

    axs[1, 0].set_title("TBD", fontweight="bold")

    # --------------------------------------------------------------------------------------------------------------------
    plt.tight_layout()
    plt.savefig("fig_temp.png",transparent=True)