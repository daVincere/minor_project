#!/usr/bin/env python

# ---- MODULE DOCSTRING

__doc__ = """



# ---- IMPORT MODULES

try:
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
except:
    raise ImportError("Install 'matplotlib' to plot convergence results.")

# ---- CONVERGENCE PLOT

def ConvergencePlot(cost):
    """

    Monitors convergence.

    Parameters:
    ----------

        :param dict cost: mean and best cost over cycles/generations as returned
                          by an optimiser.

    """

    font = FontProperties();
    font.set_size('larger');
    labels = ["Best Cost Function", "Mean Cost Function"]
    plt.figure(figsize=(12.5, 4));
    plt.plot(range(len(cost["best"])), cost["best"], label=labels[0]);
    plt.scatter(range(len(cost["mean"])), cost["mean"], color='red', label=labels[1]);
    plt.xlabel("Iteration #");
    plt.ylabel("Value [-]");
    plt.legend(loc="best", prop = font);
    plt.xlim([0,len(cost["mean"])]);
    plt.grid();
    plt.show();

# ---- END
