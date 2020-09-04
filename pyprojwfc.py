import types

params = {'prefix': 'slab_si_tc_70',
          'outdir': '../si_tc/bgw/wfn/tmp/',
          'filpdos': 'pdos.dat',
          'filproj': 'proj.dat',
          'tdosinboxes': True,
          'plotboxes': True}

fft_grid = [80, 120, 720]
num_elements = [1, 1, 50]
num_blocks = 1
num_nodes = [0, 0, 0]
rem_nodes = [0, 0, 0]

for j, item in enumerate(num_elements):
    num_blocks *= item
    num_nodes[j] = fft_grid[j] // num_elements[j]
    rem_nodes[j] = fft_grid[j] % num_elements[j]

text_data = ['&projwfc']

for key, value in params.items():
    if type(value) == bool:
        if value:
            value = '.true.'
        else:
            value = '.false.'
        text_data.append('  {} = {}'.format(key, value))
    else:
        text_data.append('  {} = \'{}\''.format(key, value))

text_data.append('  ' + 'n_proj_boxes' + ' = ' + str(num_blocks))

ind = 0

for j1 in range(num_elements[0]):
    for j2 in range(num_elements[1]):
        for j3 in range(num_elements[2]):
            ind += 1
            if j1 == num_elements[0] - 1:
                text_data.append('  irmin(1, {}) = {}'.format(ind, num_nodes[0] * j1))
                text_data.append('  irmax(1, {}) = {}'.format(ind, num_nodes[0] * (j1 + 1) + rem_nodes[0]))
            else:
                text_data.append('  irmin(1, {}) = {}'.format(ind, num_nodes[0] * j1))
                text_data.append('  irmax(1, {}) = {}'.format(ind, num_nodes[0] * (j1 + 1)))

            if j2 == num_elements[1] - 1:
                text_data.append('  irmin(2, {}) = {}'.format(ind, num_nodes[1] * j2))
                text_data.append('  irmax(2, {}) = {}'.format(ind, num_nodes[1] * (j2 + 1) + rem_nodes[1]))
            else:
                text_data.append('  irmin(2, {}) = {}'.format(ind, num_nodes[1] * j2))
                text_data.append('  irmax(2, {}) = {}'.format(ind, num_nodes[1] * (j2 + 1)))

            if j1 == num_elements[2] - 1:
                text_data.append('  irmin(3, {}) = {}'.format(ind, num_nodes[2] * j3))
                text_data.append('  irmax(3, {}) = {}'.format(ind, num_nodes[2] * (j3 + 1) + rem_nodes[2]))
            else:
                text_data.append('  irmin(3, {}) = {}'.format(ind, num_nodes[2] * j3))
                text_data.append('  irmax(3, {}) = {}'.format(ind, num_nodes[2] * (j3 + 1)))

text_data.append('/')
text_data = '\n'.join(text_data)

with open('projwfc.in', 'w') as file:
    file.write(text_data)
