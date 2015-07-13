import openbabel as ob
def conv(inchi):
	conv = ob.OBConversion()
	conv.SetInAndOutFormats("inchi", "smi")
	mol = ob.OBMol()
	conv.ReadString(mol, "{}".format(inchi))
	smiles = conv.WriteString(mol)
	return smiles
if __name__ == "__main__":
    conv(inchi)