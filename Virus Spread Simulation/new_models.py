import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import random
from matplotlib.gridspec import GridSpec

#Style sheet
plt.style.use('ggplot')


def SIR(sbx_healthy, sbx_infected, sbx_days, sbx_propagation, sbx_r_chance,chbx_firewall,chbx_disconnected):
    #Starting Susceptible
    N0 = sbx_healthy.value()

    # Initial number of infected
    I0 = sbx_infected.value()
    #Total Population
    P0 = I0 + N0

    # Days to run
    D0 = sbx_days.value()

    if chbx_firewall.isChecked():
        # Contact rate
        beta = int(sbx_propagation.value()) / (random.uniform(200, 210))
    else:
        # Contact rate
        beta = int(sbx_propagation.value()) / 100


    # recovery rate
    gamma = int(sbx_r_chance.value()) / 1000

    # recovered individuals
    if chbx_disconnected.isChecked():
        R0 = sbx_healthy.value() - (sbx_healthy.value() / (random.uniform(1.1, 1.8)))
    else:
        R0 = 0
    # work out susceptible
    S0 = N0 - I0 - R0

    # A grid of time points (in days)
    t = np.linspace(0, D0, D0)

    # The SIR model differential equations

    def deriv(y, t, N0, beta, gamma):
        S, I, R = y
        dSdt = -(beta * S * I / N0)
        dIdt = (beta * S * I) / N0 - (gamma * I)
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    # Initial conditions vector
    y0 = S0, I0, R0

    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N0, beta, gamma))
    S, I, R = ret.T

    # ------------------------------------GRAPHS----------------------------#

    def format_axes(fig):
        for i, ax in enumerate(fig.axes):
            ax.text(0.5, 0.5, "ax%d" % (i + 1), va="center", ha="center")
            ax.tick_params(labelbottom=False, labelleft=False)

    fig = plt.figure(figsize=(15.3, 7.9))

    gs = GridSpec(3, 3, figure=fig)
    ax1 = fig.add_subplot(gs[0, :])
    ax2 = fig.add_subplot(gs[1, :-1])
    ax3 = fig.add_subplot(gs[1:, -1])
    ax4 = fig.add_subplot(gs[-1, 0])
    ax5 = fig.add_subplot(gs[-1, -2])
    format_axes(fig)

    # TOP ---------------------------------------------------------
    ax1.set_title("Timeline Overview", fontweight="bold")
    try:

        plt.setp(ax1, xlabel="Time (Days)")
        plt.setp(ax1, ylabel="Total Devices")
        ax1.grid()

        ax1.plot(t, S, label='Unaffected Devices', color='tab:blue')
        ax1.plot(t, I, linestyle='--', label='Infected', color='tab:orange')
        ax1.plot(t, R, label='Recovered & Protected', color='tab:green')

        legend = ax1.legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right'):
            ax1.spines[spine].set_visible(False)

        ax1.spines['bottom'].set_color('black')
        ax1.spines['left'].set_color('black')

        ax1.legend(['Unaffected', 'Infected', 'Recovered and Protected'], loc='best',
                   ncol=1, fancybox=True)
    except Exception as e:
        print(e)

    # middle ---------------------------------------------------------
    ax2.set_title("Infections over {} Days".format(365), fontweight="bold")
    try:
        ax2.grid()
        plt.setp(ax2, xlabel="Time (Days)")
        plt.setp(ax2, ylabel="Total Infected Devices")

        ax2.plot(t, I, color='black', linestyle='--')
        ax2.bar(t, I, width=2, label='Infected', color='tab:orange')

        ax2.spines['bottom'].set_color('black')
        ax2.spines['left'].set_color('black')

        for spine in ('top', 'right'):
            ax2.spines[spine].set_visible(False)

    except Exception as e:
        print(e)


    # Bottom Right plot---------------------------------------------------------

    ax3.set_title("Change in Infected per day".format(D0), fontweight="bold")
    try:
        ax3.grid()

        IDiff = np.diff(I)

        upper = 1
        lower = -1

        Iupper = np.ma.masked_where(IDiff < upper, IDiff)
        Ilower = np.ma.masked_where(IDiff > lower, IDiff)

        ax3.plot(np.delete(t, 0), Iupper, color='crimson')

        ax3.plot(t, 0 * t, linestyle=':', color='silver')

        ax3.plot(np.delete(t, 0), Ilower, color='tab:green')

        ax3.legend(['Increasing Infected', 'Zero', 'Decreasing  Infected'], loc='best',
                   ncol=1, fancybox=True)

        plt.setp(ax3, xlabel="Time (Days)")
        plt.setp(ax3, ylabel="Change in Infected")

        ax3.spines['bottom'].set_color('black')
        ax3.spines['left'].set_color('black')

        for spine in ('top', 'right'):
            ax3.spines[spine].set_visible(False)

    except Exception as e:
        print(e)

    # bottom left ---------------------------------------------------------
    ax4.set_title("Distribution on day {} (Half-way)".format(365 / 2), fontweight="bold")
    try:
        labels = 'Unaffected', 'Infected', 'Recovered and Protected'

        colors = ['tab:blue', 'tab:orange', 'tab:green']

        sizes = [S[-1] / P0 * 100, I[-1] / P0 * 100, R[-1] / P0 * 100]

        labels = [f'{l} | {s:0.1f}%' for l, s in zip(labels, sizes)]

        ax4.pie(np.abs(sizes), wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': 'white'},
                pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)

        ax4.legend(labels, loc="best")

        ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    except Exception as e:
        print(e)

    # bottom middle ---------------------------------------------------------
    ax5.set_title("Distribution on day {}".format(365), fontweight="bold")
    try:
        labels = 'Unaffected', 'Infected', 'Recovered and Protected'

        colors = ['tab:blue', 'tab:orange', 'tab:green']

        sizes = [S[-1] / P0 * 100, I[-1] / P0 * 100, R[-1] / P0 * 100]

        labels = [f'{l} | {s:0.1f}%' for l, s in zip(labels, sizes)]

        ax5.pie(np.abs(sizes), wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': 'white'},
                pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)

        ax5.legend(labels, loc="best")

        ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    except Exception as e:
        print(e)

    # --------------------------------------------------------------------------------------------------------------------

    #plt.subplots_adjust(left=0.06, bottom=0.055, right=0.98, top=0.97, wspace=0.2, hspace=0.2)
    plt.tight_layout()
    plt.savefig("fig_temp.png",transparent=True)

def SIRD(sbx_healthy, sbx_infected, sbx_days, sbx_propagation, sbx_r_chance,sbx_mortality,chbx_firewall,chbx_disconnected):

    #Starting Susceptible
    N0 = sbx_healthy.value()
    # Initial number of infected
    I0 = sbx_infected.value()

    # Total Population
    P0 = I0 + N0

    # Days to run
    D0 = sbx_days.value()

    if chbx_firewall.isChecked():
        # Contact rate
        beta = int(sbx_propagation.value()) / (random.uniform(165, 170))
    else:
        # Contact rate
        beta = int(sbx_propagation.value()) / 100

    # recovery rate
    gamma = int(sbx_r_chance.value()) / 1000

    #mortality
    mu = int(sbx_mortality.value()) / 1000

    # recovered individuals
    if chbx_disconnected.isChecked():
        R0 = sbx_healthy.value() - (sbx_healthy.value() / (random.uniform(1.1, 1.8)))
    else:
        R0 = 0
    # start Dead individuals
    Dd0 = 0
    # work out susceptible
    S0 = N0 - I0 - R0
    # A grid of time points (in days)
    t = np.linspace(0, D0, D0)

    def deriv(y, t, N0, beta, gamma,mu):
        S, I, R, D = y
        dSdt = -(beta * S * I) / N0
        dIdt = (beta * S * I) / N0 - (gamma * I) - (mu * I)
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
    axs[0, 0].set_title("Timeline Overview",fontweight="bold")
    try:

        plt.setp(axs[0, 0], xlabel="Time (Days)")
        plt.setp(axs[0, 0], ylabel="Total Devices")
        axs[0, 0].grid()

        axs[0, 0].plot(t, S, label='Unaffected', color='tab:blue')
        axs[0, 0].plot(t, I, linestyle='--', label='Infected', color='tab:orange')
        axs[0, 0].plot(t, R, label='Recovered & protected', color='tab:green')
        axs[0, 0].plot(t, D, label='Irrecoverable', color='crimson')

        legend = axs[0, 0].legend()
        legend.get_frame().set_alpha(0.5)

        axs[0, 0].spines['bottom'].set_color('black')
        axs[0, 0].spines['left'].set_color('black')

        for spine in ('top', 'right'):
            axs[0, 0].spines[spine].set_visible(False)

        axs[0, 0].legend(['Unaffected', 'Infected', 'Recovered and Protected','Irrecoverable'], loc='best',
                         ncol=1, fancybox=True)
    except Exception as e:
        print(e)

    # TOP Right plot---------------------------------------------------------
    axs[0, 1].set_title("Distribution on day {}".format(D0), fontweight="bold")
    try:

        labels = 'Unaffected', 'Infected', 'Recovered and Protected', 'Irrecoverable'
        colors = ['tab:blue', 'tab:orange', 'tab:green','crimson']

        sizes = [S[-1] / P0 * 100, I[-1] / P0 * 100, R[-1] / P0 * 100, D[-1]/N0*100]

        labels = [f'{l} | {s:0.1f}%' for l, s in zip(labels, sizes)]

        axs[0, 1].pie(np.abs(sizes), wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': 'white'},
                      pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)

        axs[0, 1].legend(labels, loc="best")

        axs[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    except Exception as e:
        print(e)

    # Bottom Right plot---------------------------------------------------------

    axs[1, 1].set_title("Change in Infected per day".format(D0), fontweight="bold")
    try:
        axs[1, 1].grid()

        IDiff = np.diff(I)

        upper = 1
        lower = -1

        Iupper = np.ma.masked_where(IDiff < upper, IDiff)
        Ilower = np.ma.masked_where(IDiff > lower, IDiff)

        axs[1, 1].plot(np.delete(t, 0), Iupper, color='crimson')

        axs[1, 1].plot(t, 0 * t, linestyle=':', color='silver')

        axs[1, 1].plot(np.delete(t, 0), Ilower, color='tab:green')

        axs[1, 1].legend(['Increasing Infected', 'Zero', 'Decreasing  Infected'], loc='best',
                         ncol=1, fancybox=True)

        plt.setp(axs[1, 1], xlabel="Time (Days)")
        plt.setp(axs[1, 1], ylabel="Change in Infected")

        axs[1, 1].spines['bottom'].set_color('black')
        axs[1, 1].spines['left'].set_color('black')

        for spine in ('top', 'right'):
            axs[1, 1].spines[spine].set_visible(False)

    except Exception as e:
        print(e)

    except Exception as e:
        print(e)
    # Bottom Left plot----------------------------------------------------------

    try:
        axs[1, 0].set_title("Infections over {} Days".format(D0), fontweight="bold")
        axs[1, 0].grid()

        plt.setp(axs[1, 0], xlabel="Time (Days)")
        plt.setp(axs[1, 0], ylabel="Total Infected Devices")

        axs[1, 0].plot(t, I, color='black',linestyle='--')
        axs[1, 0].bar(t, I,width=1.1, label='Infected', color='tab:orange')

        axs[1, 0].spines['bottom'].set_color('black')
        axs[1, 0].spines['left'].set_color('black')

        for spine in ('top', 'right'):
            axs[1, 0].spines[spine].set_visible(False)


    except Exception as e:
        print(e)


    # --------------------------------------------------------------------------------------------------------------------
    plt.tight_layout()
    plt.savefig("fig_temp.png",transparent=True)

def SIS(sbx_healthy, sbx_infected, sbx_days, sbx_propagation, sbx_r_chance,chbx_firewall,chbx_disconnected):
    #Starting Susceptible
    N0 = sbx_healthy.value()
    # Initial number of infected
    I0 = sbx_infected.value()
    #Total Population
    P0 = I0 + N0
    # Days to run
    D0 = sbx_days.value()

    if chbx_firewall.isChecked():
        # Contact rate
        beta = int(sbx_propagation.value()) / (random.uniform(190, 200))
    else:
        # Contact rate
        beta = int(sbx_propagation.value()) / 100

    # recovery rate
    gamma = int(sbx_r_chance.value()) / 1000
    # recovered individuals
    # recovered individuals
    if chbx_disconnected.isChecked():
        R0 = sbx_healthy.value() - (sbx_healthy.value() / (random.uniform(1.1, 1.8)))
    else:
        R0 = 0
    # work out susceptible
    S0 = N0 - I0 - R0
    # A grid of time points (in days)
    t = np.linspace(0, D0, D0)

    # The SIR model differential equations
    def deriv(y, t, N0, beta, gamma):
        S, I  = y
        dSdt = -(beta * S * I) / N0 + (gamma * I)
        dIdt = (beta * S * I) / N0 - (gamma * I)
        return dSdt, dIdt

    # Initial conditions vector
    y0 = S0, I0

    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N0, beta, gamma))
    S, I = ret.T

    # ------------------------------------GRAPHS----------------------------#

    # Plot the data
    fig, axs = plt.subplots(2, 2,figsize=(15.3, 7.9))

    # TOP LEFT plot---------------------------------------------------------
    axs[0, 0].set_title("Timeline Overview",fontweight="bold")
    try:
        plt.setp(axs[0, 0], xlabel="Time (Days)")
        plt.setp(axs[0, 0], ylabel="Total Devices")
        axs[0, 0].grid()

        axs[0, 0].plot(t, S, label='Unaffected Devices', color='tab:blue')
        axs[0, 0].plot(t, I, linestyle='--', label='Infected', color='tab:orange')

        legend = axs[0, 0].legend()
        legend.get_frame().set_alpha(0.5)

        axs[0, 0].spines['bottom'].set_color('black')
        axs[0, 0].spines['left'].set_color('black')

        for spine in ('top', 'right'):
            axs[0, 0].spines[spine].set_visible(False)

        axs[0, 0].legend(['Unaffected', 'Infected'], loc='best',
                         ncol=1, fancybox=True)
    except Exception as e:
        print(e)

    # TOP Right plot---------------------------------------------------------
    axs[0, 1].set_title("Distribution on day {}".format(D0),fontweight="bold")
    try:

        labels = 'Unaffected', 'Infected'

        colors = ['tab:blue', 'tab:orange']

        sizes = [S[-1]/P0*100, I[-1]/P0*100]


        labels = [f'{l} | {s:0.1f}%' for l, s in zip(labels, sizes)]

        axs[0, 1].pie(np.abs(sizes), wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': 'white'},
                      pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)

        axs[0, 1].legend(labels, loc="best")

        axs[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    except Exception as e:
        print(e)

    # Bottom Right plot---------------------------------------------------------

    axs[1, 1].set_title("Change in Infected per day".format(D0), fontweight="bold")
    try:
        axs[1, 1].grid()

        IDiff = np.diff(I)

        upper = 1
        lower = -1

        Iupper = np.ma.masked_where(IDiff < upper, IDiff)
        Ilower = np.ma.masked_where(IDiff > lower, IDiff)

        axs[1, 1].plot(np.delete(t, 0), Iupper, color='crimson')

        axs[1, 1].plot(t, 0 * t, linestyle=':', color='silver')

        axs[1, 1].plot(np.delete(t, 0), Ilower, color='tab:green')

        axs[1, 1].legend(['Increasing Infected', 'Zero', 'Decreasing  Infected'], loc='best',
                         ncol=1, fancybox=True)

        plt.setp(axs[1, 1], xlabel="Time (Days)")
        plt.setp(axs[1, 1], ylabel="Change in Infected")

        axs[1, 1].spines['bottom'].set_color('black')
        axs[1, 1].spines['left'].set_color('black')

        for spine in ('top', 'right'):
            axs[1, 1].spines[spine].set_visible(False)

    except Exception as e:
        print(e)

    # Bottom Left plot----------------------------------------------------------
    try:
        axs[1, 0].set_title("Infections over {} Days".format(D0), fontweight="bold")
        axs[1, 0].grid()

        plt.setp(axs[1, 0], xlabel="Time (Days)")
        plt.setp(axs[1, 0], ylabel="Total Infected Devices")

        axs[1, 0].plot(t, I, color='black',linestyle='--')
        axs[1, 0].bar(t, I,width=1.1, label='Infected', color='tab:orange')

        axs[1, 0].spines['bottom'].set_color('black')
        axs[1, 0].spines['left'].set_color('black')

        for spine in ('top', 'right'):
            axs[1, 0].spines[spine].set_visible(False)


    except Exception as e:
        print(e)

    # --------------------------------------------------------------------------------------------------------------------

    #plt.subplots_adjust(left=0.06, bottom=0.055, right=0.98, top=0.97, wspace=0.2, hspace=0.2)
    plt.tight_layout()
    plt.savefig("fig_temp.png",transparent=True)

def SEIR(sbx_healthy, sbx_infected, sbx_days, sbx_hibernation, sbx_propagation, sbx_r_chance,chbx_firewall,chbx_disconnected):
    #Starting Susceptible
    N0 = sbx_healthy.value()

    # Initial number of infected
    I0 = sbx_infected.value()
    #Total Population
    P0 = I0 + N0

    # Days to run
    D0 = sbx_days.value()

    if chbx_firewall.isChecked():
        # Contact rate
        beta = int(sbx_propagation.value()) / (random.uniform(200, 210))
    else:
        # Contact rate
        beta = int(sbx_propagation.value()) / 100

    E0 = sbx_hibernation.value()

    # recovery rate
    gamma = int(sbx_r_chance.value()) / 1000

    # recovered individuals
    if chbx_disconnected.isChecked():
        R0 = sbx_healthy.value() - (sbx_healthy.value() / (random.uniform(1.1, 1.8)))
    else:
        R0 = 0
    # work out susceptible
    S0 = N0 - I0 - R0

    # A grid of time points (in days)
    t = np.linspace(0, D0, D0)

    # The SIR model differential equations

    def deriv(y, t, N0, beta, gamma):
        S, E, I, R = y

        dSdt = 0.005 * N0 - 0.005 * S - beta * I * S / N0

        dEdt = beta * I * S / N0 - (0.005 + E0) * E

        dIdt = E0 * E - (gamma + 0.005) * I

        dRdt = gamma * I - 0.005 * R

        return dSdt,dEdt, dIdt, dRdt

    # Initial conditions vector
    y0 = S0, I0, R0

    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N0, beta, gamma))
    S, I, R = ret.T

    # ------------------------------------GRAPHS----------------------------#

    # Plot the data
    fig, axs = plt.subplots(2, 2,figsize=(15.3, 7.9))

    # TOP LEFT plot---------------------------------------------------------
    axs[0, 0].set_title("Timeline Overview",fontweight="bold")
    try:

        plt.setp(axs[0, 0], xlabel="Time (Days)")
        plt.setp(axs[0, 0], ylabel="Total Devices")
        axs[0, 0].grid()

        axs[0, 0].plot(t, S, label='Unaffected Devices', color='tab:blue')
        axs[0, 0].plot(t, I, linestyle='--', label='Infected', color='tab:orange')
        axs[0, 0].plot(t, R, label='Recovered & Protected', color='tab:green')


        legend = axs[0, 0].legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            axs[0, 0].spines[spine].set_visible(False)

        axs[0, 0].legend(['Unaffected', 'Infected', 'Recovered and Protected'], loc='best',
                         ncol=1, fancybox=True)
    except Exception as e:
        print(e)

    # TOP Right plot---------------------------------------------------------
    axs[0, 1].set_title("Distribution on day {}".format(D0), fontweight="bold")
    try:
        labels = 'Unaffected', 'Infected', 'Recovered and Protected'

        colors = ['tab:blue', 'tab:orange', 'tab:green']

        sizes = [S[-1] / P0 * 100, I[-1] / P0 * 100, R[-1] / P0 * 100]

        labels = [f'{l} | {s:0.1f}%' for l, s in zip(labels, sizes)]

        axs[0, 1].pie(np.abs(sizes), wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': 'white'},
                      pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)

        axs[0, 1].legend(labels, loc="best")

        axs[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    except Exception as e:
        print(e)

    # Bottom Right plot---------------------------------------------------------

    axs[1, 1].set_title(" dsf", fontweight="bold")
    try:
        print()
    except Exception as e:
        print(e)

    # Bottom Left plot----------------------------------------------------------
    try:
        axs[1, 0].set_title("Infections over {} Days".format(D0), fontweight="bold")
        axs[1, 0].grid()

        plt.setp(axs[1, 0], xlabel="Time (Days)")
        plt.setp(axs[1, 0], ylabel="Total Infected Devices")

        axs[1, 0].plot(t, I, color='black',linestyle='--')
        axs[1, 0].bar(t, I,width=1, label='Infected', color='tab:orange')


        for spine in ('top', 'right', 'bottom', 'left'):
            axs[1, 0].spines[spine].set_visible(False)


    except Exception as e:
        print(e)

    # --------------------------------------------------------------------------------------------------------------------

    #plt.subplots_adjust(left=0.06, bottom=0.055, right=0.98, top=0.97, wspace=0.2, hspace=0.2)
    plt.tight_layout()
    plt.savefig("fig_temp.png",transparent=True)