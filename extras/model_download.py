from huggingface_hub import snapshot_download
import os
from dotenv import load_dotenv

load_dotenv()

HF_KEY= os.getenv("HF_KEY")
model_id = "luxetveritas/DeepSeek-R1-Medical-COT"  # Replace with the ID of the model you want to download

snapshot_download(repo_id=model_id, local_dir="lux", token=HF_KEY)
