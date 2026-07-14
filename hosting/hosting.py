from huggingface_hub import HfApi
import os
huf_id = os.getenv("PGP_HUG_FACE_ID")

api = HfApi(token=os.getenv("PGP_HUG_FACE_WRITE_TKN"))

api.upload_folder(
    folder_path="deployment",     # the local folder containing your files
    repo_id=f"{huf_id}/Machine-Failure-Prediction",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
