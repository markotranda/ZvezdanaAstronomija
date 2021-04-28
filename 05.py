import numpy as np

def ukupna_magnituda(magnitude):
    # const c
    c = 2.51188643150958
    magnituda_ukupna = np.sum(magnitude)
    magnituda_grupe = magnituda_ukupna - 2.5*np.log(np.sum(c**(magnituda_ukupna - magnitude)))
    return magnituda_grupe


def main():
    m = [5, 6, 10, 7, 3, 1, 10]
    print(ukupna_magnituda(m))  


if __name__ == "__main__":
    main()