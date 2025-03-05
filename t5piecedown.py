from huggingface_hub import hf_hub_download
hf_hub_download(repo_id="google/t5-v1_1-base", filename="spiece.model", local_dir=".")