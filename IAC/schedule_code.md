gcloud compute resource-policies create instance-schedule vm-schedule \
  --region=us-central1 \
  --vm-start-schedule="23:55" \
  --timezone="Asia/Singapore" \
  --description="Start VM at 6:55pm SGT daily" \
  --daily