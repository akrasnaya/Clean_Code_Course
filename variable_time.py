"""
1. conf = {   
              'description': description,
              'folder' : "../../experiments/",
              'logging': True,
              'ratio': 0.8,
              'dim_model': 15,
              'min_length': 4,
              'max_length': 256,
              'batch_size': 128,
              'max_data': 4500,
              'fold_num': 6
              }
Самое раннее связывание, так как conf - словарь с константами, который мы объявляем в самом начале эксперимента

2. batch_size = conf['batch_size']
Связывание на уровне компиляции

3. rna_seq = RNA.create_empty_seq()
Связывание во время выполнения программы, метод create_empty_seq() создает пустую последовательность длины, установленной в конфиге

"""
