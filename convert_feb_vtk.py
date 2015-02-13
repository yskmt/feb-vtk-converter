import sys

import read_xplt as rx
import write_vtk as wv


# INPUT
if int(len(sys.argv) < 3):
    print "Number of arguments wrong!"
    sys.exit(1)

workdir = str(sys.argv[1])
filename = str(sys.argv[2])
nstate = int(sys.argv[3])  # read this state

if workdir[-1] is not '/':
    workdir += '/'


for nst in [nstate]:  # range(num_states):

    rx.read_xplt(workdir, filename, nst, rx.TAGS)

    # MA
    ndfiles = ['nodes_%d' % nst]
    elfiles = ['elements_%d_0' % nst, 'elements_%d_1' % nst]

    vtkfile = 'res_%d.vtu' % nst

    nodes, elems, dom_n_elems \
        = wv.load_geom(workdir, ndfiles, elfiles)
    node_data, elem_data, dom_elem_types, \
        item_formats, item_names, item_def_doms, data_dims\
        = wv.load_data(workdir, nst, len(elfiles))

    wv.write_vtk(workdir, nodes, elems, dom_n_elems, node_data,
                 elem_data, dom_elem_types, item_formats, item_names,
                 item_def_doms, data_dims, vtkfile)