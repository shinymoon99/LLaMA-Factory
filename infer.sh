deepspeed --num_gpus 2 src/train_bash.py \
    --deepspeed ./examples/deepspeedds_z2_config.json \
    --ddp_timeout 180000000 \ \
    --stage sft \
    --do_predict \
    --model_name_or_path /root/autodl-tmp/llama2-7b_hf \
#    --adapter_name_or_path path_to_checkpoint \
    --dataset ECI \
    --template default \
    --finetuning_type lora \
    --output_dir  ./output/ECIhardprompt \
    --per_device_eval_batch_size 1 \
    --max_samples 100 \
    --predict_with_generate \
    --fp16