#Uncomment the test argument if you don't want to train the model (only for testing)
#Set demo to True to test the model on individual samples
TF_XLA_FLAGS=--tf_xla_cpu_global_jit \
XLA_FLAGS=--xla_hlo_profile \
CUDA_VISIBLE_DEVICES=1 \
python train_model.py \
    --corpus /Path-to-Corpus-File \
    --ecores /Path-to-ResNeXt-Features \
    --tag    /Path-to-Tag_Feats-File \
    --ref    /Path-to-Ref-File \
    --demo   False
#    --test   /Path-to-Saved-Model \
    > test.log
