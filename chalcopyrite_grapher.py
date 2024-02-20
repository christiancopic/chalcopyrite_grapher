import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np 

def main():

    # Change to args
    MOBILITY = True
    RESISTIVITY = False
    BULK_CONC = False
    MOBILITY_CDF = True
    RESISTIVITY_CDF = True
    BULK_CONC_CDF = True

    cwd = os.getcwd()
    file_data = []
    file_name = []
    for file in os.listdir(cwd + '/data'):
        if(file[-5:] != '.hall'):
            continue
        df = pd.read_csv(cwd + '/data/' + file, sep='\t', lineterminator='\n', skiprows=4)
        df = df.replace({r'\r': ''}, regex=True)
        file_data.append(df)
        print(df)
        file_name.append(file[:-5])
    
    if MOBILITY:
        mobility(file_data, file_name)
    if RESISTIVITY:
        resistivity(file_data, file_name)
    if BULK_CONC:
        bulk_conc(file_data, file_name)
    if MOBILITY_CDF:
        mobility_cdf(file_data, file_name)
    if RESISTIVITY_CDF:
        resistivity_cdf(file_data, file_name)
    if BULK_CONC_CDF:
        bulk_conc_cdf(file_data, file_name)


def mobility(file_data, file_name):
    for df in file_data:
        plt.semilogy(df['No'], abs(df['Mobility']), marker='o')
    plt.legend(file_name)
    plt.xlabel('Sample Number')
    plt.ylabel('Mobility ($cm^2/Vs$)')
    plt.title('Mobility')
    plt.show()

def resistivity(file_data, file_name):
    for df in file_data:
        plt.plot(df['No'], abs(df['Resistivity']), marker='o')
    plt.legend(file_name)
    plt.xlabel('Sample Number')
    plt.ylabel('Resistivity ($\Omega cm$)')
    plt.title('Resistivity')
    plt.show()

def bulk_conc(file_data, file_name):
    for df in file_data:
        plt.semilogy(df['No'], abs(df['Bulk_Con.']), marker='o')
    plt.legend(file_name)
    plt.xlabel('Sample Number')
    plt.ylabel('Bulk Concentration ($/cm^3$)')
    plt.title('Bulk Concentration')
    plt.show()

def mobility_cdf(file_data, file_name):
    for df in file_data:
        N = len(abs(df['Mobility']))
        x = np.sort(abs(df['Mobility'])) 
        y = np.arange(N) / float(N) 
        plt.semilogx(x, y, marker='o') 

        #plt.hist(abs(df['Mobility']), density=True, cumulative=True, label='CDF',
        #    histtype='step', alpha=0.8, color='k')
    plt.legend(file_name)
    plt.xlabel('Mobility ($cm^2/Vs$)')
    plt.ylabel('CDF')
    plt.title('Mobility CDF')
    plt.show()

def resistivity_cdf(file_data, file_name):
    for df in file_data:
        N = len(abs(df['Resistivity']))
        x = np.sort(abs(df['Resistivity'])) 
        y = np.arange(N) / float(N) 
        plt.plot(x, y, marker='o') 
    plt.legend(file_name)
    plt.xlabel('Resistivity ($\Omega cm$)')
    plt.ylabel('CDF')
    plt.title('Resistivity CDF')
    plt.show()

def bulk_conc_cdf(file_data, file_name):
    for df in file_data:
        N = len(abs(df['Bulk_Con.']))
        x = np.sort(abs(df['Bulk_Con.'])) 
        y = np.arange(N) / float(N) 
        plt.semilogx(x, y, marker='o') 
    plt.legend(file_name)
    plt.xlabel('Bulk Concentration ($/cm^3$)')
    plt.ylabel('CDF')
    plt.title('Bulk Concentration CDF')
    plt.show()

if __name__ == '__main__':
    main()