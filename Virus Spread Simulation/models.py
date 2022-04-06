import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import random

#Style sheet
plt.style.use('ggplot')
plt.rcParams['legend.title_fontsize'] = 'x-small'


def SIR(sbx_healthy, sbx_infected, sbx_days, sbx_propagation, sbx_r_chance,chbx_ids,chbx_offline,chbx_HostFire):

        #Starting Susceptible ----------------------------------------------------#
        N0 = sbx_healthy.value()

        # Initial number of infected ---------------------------------------------#
        I0 = sbx_infected.value()

        #Total Population --------------------------------------------------------#
        P0 = I0 + N0

        # Days to run ------------------------------------------------------------#
        D0 = sbx_days.value()

        # Propagation Rate With Check Box edits ----------------------------------#
        beta = int(sbx_propagation.value()) / 100
        if chbx_ids.isChecked():
            # Contact rate
            beta = (beta * (random.uniform(0.65, 0.75)))

        if chbx_HostFire.isChecked():
            # Contact rate
            beta = (beta * (random.uniform(0.65, 0.75)))

        # recovery rate --------------------------------------------------------#
        gamma = int(sbx_r_chance.value()) / 1000

        # Recovered individuals With Check Box edits
        if chbx_offline.isChecked():
            R0 = sbx_healthy.value() - (sbx_healthy.value() / (random.uniform(1.3, 1.5)))
        else:
            R0 = 0

        # work out susceptible --------------------------------------------------#
        S0 = N0 - I0 - R0

        # A grid of time points -------------------------------------------------#
        t = np.linspace(0, D0, D0)

        # The SIR model differential equations ----------------------------------#
        def deriv(y, t, N0, beta, gamma):
            S, I, R = y
            dSdt = -(beta * S * I / N0)
            dIdt = (beta * S * I) / N0 - (gamma * I)
            dRdt = gamma * I
            return dSdt, dIdt, dRdt

        # Initial conditions vector ---------------------------------------------#
        y0 = S0, I0, R0
        # Integrate the SIR equations over the time grid, t.
        ret = odeint(deriv, y0, t, args=(N0, beta, gamma))
        S, I, R = ret.T

        # --------------------------------------------------------GRAPHS-------------------------------------------------------------#

        # Plot the data ---------------------------------------------------------#
        fig, axs = plt.subplots(2, 2,figsize=(15.3, 7.9))

        # TOP LEFT plot ---------------------------------------------------------#
        axs[0, 0].set_title("Timeline Overview",fontweight="bold")
        try:
            plt.setp(axs[0, 0], xlabel="Time (Hours)")
            plt.setp(axs[0, 0], ylabel="Total Susceptible Devices")
            axs[0, 0].grid()
            axs[0, 0].plot(t, S, label='Unaffected Devices', color='#1F77B4')
            axs[0, 0].plot(t, I, linestyle='--', label='Infected', color='#FF7F0E')
            axs[0, 0].plot(t, R, label='Recovered & Protected', color='#32A62E')
            axs[0, 0].axvline(I.argmax(axis=0), linestyle=':', color='silver')
            axs[0, 0].text(I.argmax(axis=0) + 3, np.amax(N0*0.15), 'Peak Infected By Hour: {}'.format(int((I.argmax(axis=0)))), color='black',rotation=90)

            legend = axs[0, 0].legend()
            legend.get_frame().set_alpha(0.5)
            for spine in ('top', 'right'):
                axs[0, 0].spines[spine].set_visible(False)

            axs[0, 0].spines['bottom'].set_color('black')
            axs[0, 0].spines['left'].set_color('black')
            axs[0, 0].legend(['Unaffected', 'Infected', 'Recovered and Protected'], loc='best',ncol=1, fancybox=True)

        except Exception as e:
            print(e)

        # TOP Right plot  ---------------------------------------------------------#
        axs[0, 1].set_title("Status Distribution on Day {}".format(int(D0/24)), fontweight="bold")
        try:
            labels = 'Unaffected', 'Infected', 'Recovered and Protected'
            colors = ['#1F77B4', '#FF7F0E', '#32A62E']
            sizes = [S[-1] / P0 * 100, I[-1] / P0 * 100, R[-1] / P0 * 100]
            labels = [f'{l} | {s:0.1f}%' for l, s in zip(labels, sizes)]

            axs[0, 1].pie(np.abs(sizes), wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': '#f0f0f0'},
                          pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)
            axs[0, 1].legend(labels, loc="best")
            axs[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        except Exception as e:
            print(e)

        # Bottom Right plot  ---------------------------------------------------------#
        axs[1, 1].set_title("Change in Infected Per Hour".format(D0), fontweight="bold")
        try:
            axs[1, 1].grid()
            IDiff = np.diff(I)
            upper = 1
            lower = -1

            Iupper = np.ma.masked_where(IDiff < upper, IDiff)
            Ilower = np.ma.masked_where(IDiff > lower, IDiff)

            axs[1, 1].plot(np.delete(t, 0), Iupper, color='#DC143C')
            axs[1, 1].axhline(0, linestyle=':', color='silver')
            axs[1, 1].plot(np.delete(t, 0), Ilower, color='#32A62E')
            axs[1, 1].legend(['Increasing Infected','Zero Change','Decreasing  Infected'], loc='best',ncol=1, fancybox=True)

            plt.setp(axs[1, 1], xlabel="Time (Hours)")
            plt.setp(axs[1, 1], ylabel="Change in Infected")

            axs[1, 1].spines['bottom'].set_color('black')
            axs[1, 1].spines['left'].set_color('black')
            for spine in ('top', 'right'):
                axs[1, 1].spines[spine].set_visible(False)

        except Exception as e:
            print(e)

        # Bottom Left plot  ---------------------------------------------------------#
        try:
            axs[1, 0].set_title("Total Infections Per Hour", fontweight="bold")
            axs[1, 0].grid()

            plt.setp(axs[1, 0], xlabel="Time (Hours)")
            plt.setp(axs[1, 0], ylabel="Total Infected Devices")

            upper = N0/2
            lower = N0/4

            Iupper = np.ma.masked_where(I < upper, I)
            Ilower = np.ma.masked_where(I > lower, I)
            Imiddle = np.ma.masked_where((I < lower) | (I > upper), I)

            axs[1, 0].plot(t, Iupper, color='black')
            axs[1, 0].plot(t,Imiddle, color='#DC143C')
            axs[1, 0].plot(t, Ilower, color='#FF7F0E')

            z = np.polyfit(t, I, 1)
            p = np.poly1d(z)

            axs[1, 0].plot(t, p(t), color='silver',linestyle='-.')
            axs[1, 0].legend(['>50%','25%-50%','0-25%','Trendline'], loc='best',ncol=1, fancybox=True,title='% of Susceptible Infected')
            axs[1, 0].spines['bottom'].set_color('black')
            axs[1, 0].spines['left'].set_color('black')
            axs[1, 0].axhline(N0 / 2, linestyle=':', color='silver')
            axs[1, 0].axhline(N0 / 4, linestyle=':', color='silver')

            for spine in ('top', 'right'):
                axs[1, 0].spines[spine].set_visible(False)


        except Exception as e:
            print(e)

        # Show ---------------------------------------------------------#

        plt.tight_layout()
        plt.savefig("fig_temp.png",transparent=True)
        plt.close('all')

        # END----------------------------------------------------------#

def SIRD(sbx_healthy, sbx_infected, sbx_days, sbx_propagation, sbx_r_chance,sbx_mortality,chbx_ids,chbx_offline,chbx_HostFire):
        # Starting Susceptible ----------------------------------------------------#
        N0 = sbx_healthy.value()

        # Initial number of infected ---------------------------------------------#
        I0 = sbx_infected.value()

        # Total Population --------------------------------------------------------#
        P0 = I0 + N0

        # Days to run ------------------------------------------------------------#
        D0 = sbx_days.value()

        # Propagation Rate With Check Box edits ----------------------------------#
        beta = int(sbx_propagation.value()) / 100
        beta = int(sbx_propagation.value()) / 100
        if chbx_ids.isChecked():
            # Contact rate
            beta = (beta * (random.uniform(0.65, 0.75)))

        if chbx_HostFire.isChecked():
            # Contact rate
            beta = (beta * (random.uniform(0.65, 0.75)))

        # recovery rate --------------------------------------------------------#
        gamma = int(sbx_r_chance.value()) / 1000

        # recovered individuals (random.uniform(1.3, 1.8)
        if chbx_offline.isChecked():
            R0 = sbx_healthy.value() - (sbx_healthy.value() / (random.uniform(1.3, 1.5)))
        else:
            R0 = 0

        # mortality ------------------------------------------------------------#
        mu = int(sbx_mortality.value()) / 1000

        # start Dead individuals -----------------------------------------------#
        Dd0 = 0

        # work out susceptible --------------------------------------------------#
        S0 = N0 - I0 - R0

        # A grid of time points -------------------------------------------------#
        t = np.linspace(0, D0, D0)

        # The SIRD model differential equations ---------------------------------#
        def deriv(y, t, N0, beta, gamma,mu):
            S, I, R, D = y
            dSdt = -(beta * S * I) / N0
            dIdt = (beta * S * I) / N0 - (gamma * I) - (mu * I)
            dRdt = gamma * I
            dDdt = mu * I
            return dSdt, dIdt, dRdt, dDdt

        # Initial conditions vector ---------------------------------------------#
        y0 = S0, I0, R0, Dd0
        # Integrate the SIRD equations over the time grid, t.
        ret = odeint(deriv, y0, t, args=(N0, beta, gamma, mu))
        S, I, R, D = ret.T

        # --------------------------------------------------------GRAPHS-------------------------------------------------------------#

        # Plot the data
        fig, axs = plt.subplots(2, 2,figsize=(15.3, 7.9))

        # TOP LEFT plot ---------------------------------------------------------#
        axs[0, 0].set_title("Timeline Overview",fontweight="bold")
        try:
            plt.setp(axs[0, 0], xlabel="Time (Hours)")
            plt.setp(axs[0, 0], ylabel="Total Susceptible Devices")
            axs[0, 0].grid()
            axs[0, 0].plot(t, S, label='Unaffected', color='#1F77B4')
            axs[0, 0].plot(t, I, linestyle='--', label='Infected', color='#FF7F0E')
            axs[0, 0].plot(t, R, label='Recovered & protected', color='#32A62E')
            axs[0, 0].plot(t, D, label='Irrecoverable', color='#DC143C')

            legend = axs[0, 0].legend()
            legend.get_frame().set_alpha(0.5)

            axs[0, 0].axvline(I.argmax(axis=0), linestyle=':', color='silver')
            axs[0, 0].text(I.argmax(axis=0) + 3, np.amax(N0 * 0.15),
                           'Peak Infected By Hour: {}'.format(int((I.argmax(axis=0)))), color='black', rotation=90)

            axs[0, 0].spines['bottom'].set_color('black')
            axs[0, 0].spines['left'].set_color('black')

            for spine in ('top', 'right'):
                axs[0, 0].spines[spine].set_visible(False)

            axs[0, 0].legend(['Unaffected', 'Infected', 'Recovered and Protected','Irrecoverable'], loc='best',
                             ncol=1, fancybox=True)

        except Exception as e:
            print(e)

        # TOP Right plot  ---------------------------------------------------------#
        axs[0, 1].set_title("Status Distribution on Day {}".format(int(D0/24)), fontweight="bold")
        try:
            labels = 'Unaffected', 'Infected', 'Recovered and Protected', 'Irrecoverable'
            colors = ['#1F77B4', '#FF7F0E', '#32A62E','#DC143C']
            sizes = [S[-1] / P0 * 100, I[-1] / P0 * 100, R[-1] / P0 * 100, D[-1]/N0*100]
            labels = [f'{l} | {s:0.1f}%' for l, s in zip(labels, sizes)]

            axs[0, 1].pie(np.abs(sizes), wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': '#f0f0f0'},
                          pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)

            axs[0, 1].legend(labels, loc="best")
            axs[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        except Exception as e:
            print(e)

        # Bottom Right plot  ---------------------------------------------------------#

        axs[1, 1].set_title("Change in Infected Per Hour".format(D0), fontweight="bold")
        try:
            axs[1, 1].grid()
            IDiff = np.diff(I)
            upper = 1
            lower = -1

            Iupper = np.ma.masked_where(IDiff < upper, IDiff)
            Ilower = np.ma.masked_where(IDiff > lower, IDiff)

            axs[1, 1].plot(np.delete(t, 0), Iupper, color='#DC143C')
            axs[1, 1].axhline(0, linestyle=':', color='silver')
            axs[1, 1].plot(np.delete(t, 0), Ilower, color='#32A62E')
            axs[1, 1].legend(['Increasing Infected', 'Zero Change', 'Decreasing  Infected'], loc='best',
                             ncol=1, fancybox=True)

            plt.setp(axs[1, 1], xlabel="Time (Hours)")
            plt.setp(axs[1, 1], ylabel="Change in Infected")

            axs[1, 1].spines['bottom'].set_color('black')
            axs[1, 1].spines['left'].set_color('black')

            for spine in ('top', 'right'):
                axs[1, 1].spines[spine].set_visible(False)

        except Exception as e:
            print(e)

        # Bottom Left plot  ---------------------------------------------------------#
        try:
            axs[1, 0].set_title("Total Infections Per Hour", fontweight="bold")
            axs[1, 0].grid()

            plt.setp(axs[1, 0], xlabel="Time (Hours)")
            plt.setp(axs[1, 0], ylabel="Total Infected Devices")

            upper = N0/2
            lower = N0/4


            Iupper = np.ma.masked_where(I < upper, I)
            Ilower = np.ma.masked_where(I > lower, I)
            Imiddle = np.ma.masked_where((I < lower) | (I > upper), I)

            axs[1, 0].plot(t, Iupper, color='black')
            axs[1, 0].plot(t,Imiddle, color='#DC143C')
            axs[1, 0].plot(t, Ilower, color='#FF7F0E')

            z = np.polyfit(t, I, 1)
            p = np.poly1d(z)
            axs[1, 0].plot(t, p(t), color='silver',linestyle='-.')

            axs[1, 0].legend(['>50%','25%-50%','0-25%','Trendline'], loc='best',ncol=1, fancybox=True,title='% of Susceptible Infected')
            axs[1, 0].spines['bottom'].set_color('black')
            axs[1, 0].spines['left'].set_color('black')
            axs[1, 0].axhline(N0 / 2, linestyle=':', color='silver')
            axs[1, 0].axhline(N0 / 4, linestyle=':', color='silver')

            for spine in ('top', 'right'):
                axs[1, 0].spines[spine].set_visible(False)

        except Exception as e:
            print(e)


        # Show ---------------------------------------------------------#
        plt.tight_layout()
        plt.savefig("fig_temp.png",transparent=True)
        plt.close('all')

        # END----------------------------------------------------------#

def SIS(sbx_healthy, sbx_infected, sbx_days, sbx_propagation, sbx_r_chance,chbx_ids,chbx_offline,chbx_HostFire):
        # Starting Susceptible ----------------------------------------------------#
        N0 = sbx_healthy.value()

        # Initial number of infected ---------------------------------------------#
        I0 = sbx_infected.value()

        # Total Population --------------------------------------------------------#
        P0 = I0 + N0

        # Days to run ------------------------------------------------------------#
        D0 = sbx_days.value()

        # Propagation Rate With Check Box edits ----------------------------------#
        beta = int(sbx_propagation.value()) / 100
        if chbx_ids.isChecked():
            # Contact rate
            beta = (beta * (random.uniform(0.65, 0.75)))

        if chbx_HostFire.isChecked():
            # Contact rate
            beta = (beta * (random.uniform(0.65, 0.75)))

        # recovery rate --------------------------------------------------------#
        gamma = int(sbx_r_chance.value()) / 1000

        # Recovered individuals With Check Box edits
        if chbx_offline.isChecked():
            R0 = sbx_healthy.value() - (sbx_healthy.value() / (random.uniform(1.3, 1.5)))
        else:
            R0 = 0

        # work out susceptible --------------------------------------------------#
        S0 = N0 - I0 - R0

        # A grid of time points -------------------------------------------------#
        t = np.linspace(0, D0, D0)

        # The SIS model differential equations ----------------------------------#
        def deriv(y, t, N0, beta, gamma):
            S, I  = y
            dSdt = -(beta * S * I) / N0 + (gamma * I)
            dIdt = (beta * S * I) / N0 - (gamma * I)
            return dSdt, dIdt

        # Initial conditions vector ---------------------------------------------#
        y0 = S0, I0

        # Integrate the SIR equations over the time grid, t.
        ret = odeint(deriv, y0, t, args=(N0, beta, gamma))
        S, I = ret.T

        # --------------------------------------------------------GRAPHS-------------------------------------------------------------#

        # Plot the data ---------------------------------------------------------#
        fig, axs = plt.subplots(2, 2,figsize=(15.3, 7.9))

        # TOP LEFT plot ---------------------------------------------------------#
        axs[0, 0].set_title("Timeline Overview",fontweight="bold")
        try:
            plt.setp(axs[0, 0], xlabel="Time (Hours)")
            plt.setp(axs[0, 0], ylabel="Total Susceptible Devices")
            axs[0, 0].grid()
            axs[0, 0].plot(t, S, label='Unaffected Devices', color='#1F77B4')
            axs[0, 0].plot(t, I, linestyle='--', label='Infected', color='#FF7F0E')

            legend = axs[0, 0].legend()
            legend.get_frame().set_alpha(0.5)

            axs[0, 0].spines['bottom'].set_color('black')
            axs[0, 0].spines['left'].set_color('black')
            axs[0, 0].axvline(I.argmax(axis=0), linestyle=':', color='silver')
            axs[0, 0].text(I.argmax(axis=0) + 3, np.amax(N0 * 0.15),'Peak Infected By Hour: {}'.format(int((I.argmax(axis=0)))), color='black', rotation=90)

            for spine in ('top', 'right'):
                axs[0, 0].spines[spine].set_visible(False)

            axs[0, 0].legend(['Unaffected', 'Infected'], loc='best',
                             ncol=1, fancybox=True)

        except Exception as e:
            print(e)

        # TOP Right plot  ---------------------------------------------------------#
        axs[0, 1].set_title("Status Distribution on Day {}".format(int(D0/24)),fontweight="bold")
        try:
            labels = 'Unaffected', 'Infected'
            colors = ['#1F77B4', '#FF7F0E']
            sizes = [S[-1]/P0*100, I[-1]/P0*100]
            labels = [f'{l} | {s:0.1f}%' for l, s in zip(labels, sizes)]
            axs[0, 1].pie(np.abs(sizes), wedgeprops={'width': 0.4, 'linewidth': 1, 'edgecolor': '#f0f0f0'},pctdistance=0.8, labeldistance=1.07, startangle=90, colors=colors)
            axs[0, 1].legend(labels, loc="best")
            axs[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        except Exception as e:
            print(e)

        # Bottom Right plot  ---------------------------------------------------------#

        axs[1, 1].set_title("Change in Infected Per Hour".format(D0), fontweight="bold")
        try:
            axs[1, 1].grid()

            IDiff = np.diff(I)

            upper = 1
            lower = -1

            Iupper = np.ma.masked_where(IDiff < upper, IDiff)
            Ilower = np.ma.masked_where(IDiff > lower, IDiff)

            axs[1, 1].plot(np.delete(t, 0), Iupper, color='#DC143C')
            axs[1, 1].axhline(0, linestyle=':', color='silver')
            axs[1, 1].plot(np.delete(t, 0), Ilower, color='#32A62E')
            axs[1, 1].legend(['Increasing Infected', 'Zero Change', 'Decreasing  Infected'], loc='best',ncol=1, fancybox=True)

            plt.setp(axs[1, 1], xlabel="Time (Hours)")
            plt.setp(axs[1, 1], ylabel="Change in Infected")

            axs[1, 1].spines['bottom'].set_color('black')
            axs[1, 1].spines['left'].set_color('black')

            for spine in ('top', 'right'):
                axs[1, 1].spines[spine].set_visible(False)

        except Exception as e:
            print(e)

        # Bottom Left plot  ---------------------------------------------------------#
        try:
            axs[1, 0].set_title("Total Infections Per Hour", fontweight="bold")
            axs[1, 0].grid()

            plt.setp(axs[1, 0], xlabel="Time (Hours)")
            plt.setp(axs[1, 0], ylabel="Total Infected Devices")

            upper = N0/2
            lower = N0/4

            Iupper = np.ma.masked_where(I < upper, I)
            Ilower = np.ma.masked_where(I > lower, I)
            Imiddle = np.ma.masked_where((I < lower) | (I > upper), I)

            axs[1, 0].plot(t, Iupper, color='black')
            axs[1, 0].plot(t,Imiddle, color='#DC143C')
            axs[1, 0].plot(t, Ilower, color='#FF7F0E')

            z = np.polyfit(t, I, 1)
            p = np.poly1d(z)

            axs[1, 0].plot(t, p(t), color='silver',linestyle='-.')
            axs[1, 0].legend(['>50%','25%-50%','0-25%','Trendline'], loc='best',ncol=1, fancybox=True,title='% of Susceptible Infected')
            axs[1, 0].spines['bottom'].set_color('black')
            axs[1, 0].spines['left'].set_color('black')
            axs[1, 0].axhline(N0 / 2, linestyle=':', color='silver')
            axs[1, 0].axhline(N0 / 4, linestyle=':', color='silver')


            for spine in ('top', 'right'):
                axs[1, 0].spines[spine].set_visible(False)

        except Exception as e:
            print(e)

        # Show ---------------------------------------------------------#

        plt.tight_layout()
        plt.savefig("fig_temp.png",transparent=True)
        plt.close('all')


        # END----------------------------------------------------------#