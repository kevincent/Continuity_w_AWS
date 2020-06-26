#define parameters
fName =
f11 =
cont6path = 

sim_len = 100
dt = 0.1
counter = 10

#Load .cont6 file
self.Load_File(cont6path, log=0)

#Set Conductivity
mat = self.stored_data.conductivityEquations.obj
mat['variables'].setIcByName("f11",[['value', f11]])
mat['variables'].setIcByName("f22",[['value', f11]])
mat['variables'].setIcByName("f33",[['value', f11]])
self.stored_data.store(mat, modified = True)

#send to server and calculate the mesh
self.Send(None, log=0)
self.CalcMesh([('Calculate', None), ('Do not Calculate', None), ('Do not Calculate', None), ('linear', None)], log=0)

#Run EP
self.SinitElectrophys(log=0)
self.SintElectrophys({
        'fileName': fName, \
        'useTrilinos': 0, \
        'useCuda': 0,\
        'tstart': 0.0, 'dtout': dt, 'tlen': sim_len, \
        'solutions':  {'writeFile': 0, 'counter': counter, 'tableResult': 0, 'renderResult': 0}, \
        'aps': {'writeFile': 1, 'counter': counter, 'tableResult': 0, 'renderResult': 0,'node_list': 'all'}}, log=0)
