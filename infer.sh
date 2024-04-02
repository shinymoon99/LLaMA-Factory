# Export the NCCL_P2P_DISABLE and NCCL_IB_DISABLE variables
# export NCCL_P2P_DISABLE="1"
# export NCCL_IB_DISABLE="1"
# deepspeed --num_gpus 4 src/train_bash.py \
#     --deepspeed ./examples/deepspeed/ds_z3_config.json \
#     --ddp_timeout 180000000 \
#     --stage sft \
#     --do_predict \
#     --model_name_or_path /root/autodl-tmp/llama2-7b_hf \
#     --dataset ECI \
#     --template default \
#     --finetuning_type lora \
#     --output_dir  ./output/ECIhardprompt \
#     --per_device_eval_batch_size 1 \
#     --max_samples 100 \
#     --predict_with_generate \
#     --fp16
accelerate launch --config_file examples/accelerate/single_config.yaml src/train_bash.py \
    --ddp_timeout 180000000 \
    --stage sft \
    --do_predict \
    --model_name_or_path /root/autodl-tmp/Llama-2-chat-7b-hf \
    --dataset ECI_sum \
    --template default \
    --finetuning_type lora \
    --output_dir  ./output/ECIhardprompt \
    --per_device_eval_batch_size 1 \
    --max_samples 100 \
    --predict_with_generate \
    --fp16