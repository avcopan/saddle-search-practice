import autode as ade

ade.Config.n_cores = 1
ade.Config.ll_tmp_dir = "./tmp"

print("get_lmethod:", ade.methods.get_lmethod())
print("get_hmethod:", ade.methods.get_hmethod())

h2 = ade.Molecule(smiles='[H][H]')

h2.optimise(method=ade.methods.get_lmethod())

h2.optimise(method=ade.methods.get_hmethod())

h2.energy

