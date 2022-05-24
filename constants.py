"""
ns -> NUM_SEQUENCES
loss(true, pred, 0.1) -> LAMBDA = 0.1, loss(true, pred, loss_lambda = LAMBDA)
for i in range(128) -> BATCH_SIZE = 128, for i in range(BATCH_SIZE)
rna = {'A', 'U', 'G', 'C'} -> RNA_NUCLEOBASE = {'A', 'U', 'G', 'C'}
m = 10 -> MATRIX_SIZE = 10
make_split(seq, 4) -> SPLIT_SIZE = 4, make_split(seq, split = SPLIT_SIZE)
t = 60 -> TIMESTAMP = 60
while i <= 6: -> BACKBONE_LEN = 6, while i <= BACKBONE_LEN
s = 3 -> STEP_SIZE = 3
nn -> NUM_NUCLEOTIDES
len_mol -> MOLECULE_LEN
"""
