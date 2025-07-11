# Exercice 2
def interfaces_for_ospf_routers(router_count):
    """
    Retourne le nombre d'interfaces nécessaires dans une zone OSPF
    à accès multiple où chaque routeur doit avoir une interface active.
    """
    if router_count < 1:
        return 0
    return router_count

def total_ospf_neighbors(router_count):
    """
    Retourne le nombre de sessions adjacentes OSPF (DR/BDR incluses).
    """
    return (router_count * (router_count - 1)) // 2

# Exemple d’utilisation
if __name__ == "__main__":
    routers = int(input("Nombre de routeurs dans la zone OSPF : "))
    print(f"Interfaces nécessaires : {interfaces_for_ospf_routers(routers)}")
    print(f"Nombre d'adjacences OSPF : {total_ospf_neighbors(routers)}")
