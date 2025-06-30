from modelscope import snapshot_download

model_dir = snapshot_download("Qwen/Qwen3-8B", cache_dir="/home/why/models/Qwen3/Qwen3-8B", revision="master")
