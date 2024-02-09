import os
import pandas as pd
from matplotlib import pyplot as plt

def main():

    # Change to args
    MOBILITY = True
    RESISTIVITY = True
    BULK_CONC = True

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


def mobility(file_data, file_name):
    for df in file_data:
        plt.plot(df['No'], abs(df['Mobility']), marker='o')
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


if __name__ == '__main__':
    main()