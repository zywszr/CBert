CUDA_VISIBLE_DEVICES=0,1 python -W ignore rl_quantize.py     \
 --suffix test_run                  \
 --preserve_ratio 0.1               \
 --n_worker 32                      \
 --pregenerated_data training/      \
 --bert_model bert-base-uncased     \
 --do_lower_case                    \
 --train_batch_size 32              \
 --train_episode 5000               \
 --bert_val_size 5000               
       
