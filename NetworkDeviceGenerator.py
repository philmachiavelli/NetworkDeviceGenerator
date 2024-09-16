import random
import string
from tabulate import tabulate
from operator import itemgetter


def criar_modelos(nets=1, subnets=1):
    apps_devices = list()

    if nets > 254 and subnets > 254:
        print("Erro. Número inválido de redes e/ou subnets.")
        return apps_devices

    for sub_index in range(1, subnets + 1):

        for net_index in range(1, nets + 1):
            device = dict()

            # Fabricantes
            device["fabricante"] = (random.choice(["Cisco", "Palo Alto", "Fortnet", "Arista", "Juniper"]))

            # Modelos
            device["modelo"] = (random.choice(["R1", "R2", "R3", "R5"])
                                + random.choice(["_Alpha_", "_Beta_"])
                                + random.choice(string.ascii_letters)
                                )

            # OS
            device["os"] = (random.choice(["2.1", "2.2", "1.93", "4.01"])
                            + random.choice(string.ascii_letters)
                            )

            # IP´s
            device["ip"] = f"192.168.{str(net_index)}.{str(sub_index)}"

            apps_devices.append(device)

    return apps_devices

# MAIN program
if __name__ == "__main__":

    redes = int(input("Quantas redes deseja? "))
    subredes = int(input("Quantas sub-redes deseja? "))
    print("\n---------- LISTA DE EQUIPAMENTOS ----------")
    # pprint(criar_modelos())
    classificados = sorted(criar_modelos(redes, subredes), key=itemgetter("ip"))
    print(tabulate(classificados, headers="keys"))
