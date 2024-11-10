import torch

model_path = '../snapshot/SESR_S/model/model_best.pt'
model_data = torch.load(model_path)
print(model_data)

# 检查内容类型
if isinstance(model_data, dict) and "state_dict" in model_data:
    print("文件只包含模型参数。")
elif isinstance(model_data, torch.nn.Module):
    print("文件包含模型结构和参数。")
else:
    print("文件格式不明确，请检查文件内容。")