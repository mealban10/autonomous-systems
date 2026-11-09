import torch
import torch_pointcloud as tp

print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))

print("\nLoading pretrained PointPillars model...")

model, info = tp.create_model(
    "pointpillars.kitti.openpcdet",
    task="detection",
    pretrained=True,
    return_info=True,
)

model = model.cuda().eval()

print("\nModel loaded successfully!")
print("Model:", type(model).__name__)
print("Model classes:", info["weights"]["classes"])
print("Device:", next(model.parameters()).device)
